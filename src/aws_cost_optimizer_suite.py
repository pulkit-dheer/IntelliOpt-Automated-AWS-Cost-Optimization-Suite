"""
aws_cost_optimizer_suite.py

This module provides functionality for optimizing AWS costs by analyzing
EC2 instance CPU utilization, managing EBS snapshots, and cleaning up 
orphaned security groups.

The main functionalities include:
- Fetching regions in AWS.
- Scan all EC2 instances with tag "staging" or "dev".
- Analyzing CPU utilization to stop underutilized instances.
- Managing EBS snapshots based on attachment status.
- Deleting orphaned security groups.

"""

import datetime
import boto3


class AWSCostOptimizerSuite:
    """A suite for optimizing AWS costs by managing EC2 instances and security groups."""

    def __init__(self, threshold=10.0):
        self.ec2 = boto3.client('ec2')
        self.start_time = datetime.datetime.now() - datetime.timedelta(days=1)
        self.end_time = datetime.datetime.now()
        self.threshold = threshold


    def get_regions(self):
        """Fetch all available regions."""
        regions = self.ec2.describe_regions()
        return [region['RegionName'] for region in regions['Regions']]


    def get_compute_usage(self, instance_id, region):
        """Fetch CPU utilization data for a given instance."""
        cloudwatch_client = boto3.client('cloudwatch', region_name=region)
        try:
            cpu_data = cloudwatch_client.get_metric_statistics(
                Namespace='AWS/EC2',
                MetricName='CPUUtilization',
                Dimensions=[{'Name': 'InstanceId','Value': instance_id}],
                StartTime=self.start_time,
                EndTime=self.end_time,
                Period=3600,
                Statistics=['Average'],
            )
            return cpu_data['Datapoints']

        except Exception as e:
            print(f"Error fetching CPU data for instance {instance_id}: {e}")
            return []


    def stop_instances(self, instance_id, region):
        """Stop an EC2 instance."""
        try:
            ec2 = boto3.client('ec2', region_name=region)
            ec2.stop_instances(InstanceIds=[instance_id])
            print(f"Stopped instance: {instance_id} in region: {region}")
        except Exception as e:
            print(f"Error stopping instance {instance_id}: {e}")


    def analyze_cpu_utilization(self, datapoints, instance_id, region):
        """Analyze CPU utilization data and determine if instance is underutilized."""

        if not datapoints:
            print(f"No datapoints available for instance {instance_id}")
            return
        total_count = len(datapoints)

        low_utilization_count = sum(1 for data in datapoints if data['Average'] < self.threshold)

        if total_count > 0:
            low_utilization_percentage = (low_utilization_count / total_count) * 100
        else:
            low_utilization_percentage = 0

        if low_utilization_percentage < self.threshold:
            self.stop_instances(instance_id, region)


        print(f"Instance {instance_id} has CPU Utilization Percentage: "
      f"{low_utilization_percentage:.2f}%")




    def snapshot_optimizer(self, region):
        """Optimize EBS snapshots in a given region."""
        ec2 = boto3.client('ec2', region_name=region)
        snapshots = ec2.describe_snapshots(OwnerIds=['self'])

        for snapshot in snapshots['Snapshots']:
            snapshot_id = snapshot['SnapshotId']
            volume_id = snapshot.get('VolumeId')
            if not volume_id:
                ec2.delete_snapshot(SnapshotId=snapshot_id)
                print(f"EBS snapshot {snapshot_id} is deleted as it is not attached to any volume.")
            else:
                try:
                    all_volumes = ec2.describe_volumes(VolumeIds=[volume_id])
                    for volume in all_volumes['Volumes']:
                        if not volume['Attachments']:
                            ec2.delete_snapshot(SnapshotId=snapshot_id)
                            print(f"EBS snapshot {snapshot_id} is deleted as it is not " 
                                  f"attached to any running instance's volume.")

                except Exception as e:
                    if e.response['Error']['Code'] == "InvalidVolume.NotFound":
                        ec2.delete_snapshot(SnapshotId=snapshot_id)
                        print(f"EBS snapshot {snapshot_id} is deleted as the associated volume was not found.")


    def optimize_ec2_instances(self, region):
        """Optimize EC2 instances based on their CPU utilization."""
        ec2 = boto3.client('ec2', region_name=region)
        print(f"Checking instances in region: {region}")

        filters = [{'Name': 'instance-state-name', 'Values': ['running']}]
        all_ec2_data = ec2.describe_instances(Filters=filters)


        for reservation in all_ec2_data['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                if 'Tags' in instance:
                    for tag in instance['Tags']:
                        if tag['Key'] == 'Environment' and tag['Value'] in ['staging', 'dev']:
                            print(f"Instance ID: {instance_id} has the following tags: {tag['Value']}")
                            datapoints = self.get_compute_usage(instance_id, region)
                            self.analyze_cpu_utilization(datapoints, instance_id, region)

                else:
                    print(f"Instance ID: {instance_id} is not in staging or dev.")



    def delete_orphaned_sgs(self, orphaned_sg_ids, region):
        """Deleting all Orphaned Security Groups"""
        ec2 = boto3.client('ec2', region_name=region)

        for sg_id in orphaned_sg_ids:
            try:
                ec2.delete_security_group(GroupId=sg_id)
                print(f"Orphaned Security Group: {sg_id} in {region} is Deleted.")
            except Exception as e:
                print(f"Failed to delete Security Group: {sg_id} in {region}. "
                    f"Error {str(e)}")



    def get_security_groups(self, region):
        """Listing all the orphaned security gruops"""
        ec2 = boto3.client('ec2', region_name=region)
        all_sgs = ec2.describe_security_groups()

        all_sgs_set = set()
        default_sg_set = set()
        for sg in all_sgs['SecurityGroups']:
            sg_id = sg['GroupId']
            all_sgs_set.add(sg_id)
            sg_name = sg.get('GroupName', 'default')

            if sg_name == 'default':
                default_sg_set.add(sg_id)

        instances = ec2.describe_instances()
        associated_sg_ids = set()
        for reservation in instances['Reservations']:
            for instance in reservation['Instances']:
                for sg in instance.get('SecurityGroups', []):
                    associated_sg_ids.add(sg['GroupId'])


        orphaned_sg_ids = all_sgs_set - associated_sg_ids - default_sg_set
        self.delete_orphaned_sgs(orphaned_sg_ids, region)



def lambda_handler(event, context):
    """Lambda function handler for AWS Cost Optimization."""

    # For debugging purposes
    print("Event:", event)
    print("Context:", context)
    optimizer = AWSCostOptimizerSuite()

    regions = optimizer.get_regions()
    for region in regions:
        optimizer.snapshot_optimizer(region)
        optimizer.optimize_ec2_instances(region)
        optimizer.get_security_groups(region)
