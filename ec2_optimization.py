import boto3
import logging
import datetime


# Configure logging
logging.basicConfig(level=logging.INFO)


class EC2Optimizer:
    def __init__(self):
        self.ec2 = boto3.client('ec2')
        self.start_time = datetime.datetime.now() - datetime.timedelta(days=1)
        self.end_time = datetime.datetime.now()
        self.threshold = 10.0 


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
            logging.error(f"Error fetching CPU data for instance {instance_id}: {e}")
            return []


    def stop_instances(self, instance_id, region):
        """Stop an EC2 instance."""
        try:
            ec2 = boto3.client('ec2', region_name=region)
            ec2.stop_instances(InstanceIds=[instance_id])
            logging.info(f"Stopped instance: {instance_id} in region: {region}")
        except Exception as e:
            logging.error(f"Error stopping instance {instance_id}: {e}")


    def analyze_cpu_utilization(self, datapoints, instance_id, region):
        """Analyze CPU utilization data and determine if instance is underutilized."""

        if not datapoints:
            logging.warning(f"No datapoints available for instance {instance_id}")
            return
        total_count = len(datapoints)

        low_utilization_count = sum(1 for data in datapoints if data['Average'] < self.threshold)

        low_utilization_percentage = (low_utilization_count / total_count ) * 100 if total_count > 0 else 0

        if low_utilization_percentage < self.threshold:
            self.stop_instances(instance_id, region)


        logging.info(f"Instance {instance_id} has CPU Utilization Percentage: {low_utilization_percentage:.2f}%")


    def optimize_ec2_instances(self):
        """Optimize EC2 instances based on their CPU utilization."""
        regions = self.get_regions()
        for region in regions:
            regional_ec2_client = boto3.client('ec2', region_name=region)
            logging.info(f"Checking instances in region: {region}")

            all_ec2_data = regional_ec2_client.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

            for reservation in all_ec2_data['Reservations']:
                for instance in reservation['Instances']:
                    instance_id = instance['InstanceId']
                    if 'Tags' in instance:
                        for tag in instance['Tags']:
                            if tag['Key'] == 'Environment' and tag['Value'] in ['staging', 'dev']:
                                logging.info(f"Instance ID: {instance_id} has the following tags: {tag['Value']}")
                                datapoints = self.get_compute_usage(instance_id, region)
                                self.analyze_cpu_utilization(datapoints, instance_id, region)

                    else:
                        logging.info(f"Instance ID: {instance_id} is not in staging or dev.")



    def snapshot_optimizer(self, region='ap-south-1'):
        ec2 = boto3.client('ec2', region_name=region)
        snapshots = ec2.describe_snapshots(OwnerIds=['self'])

        for snapshot in snapshots['Snapshots']:
            snapshot_id = snapshot['SnapshotId']
            volume_id = snapshot.get('VolumeId')

            if not volume_id:
                ec2.delete_snapshot(SnapshotId=snapshot_id)
    
 
if __name__ == "__main__":
    optimizer = EC2Optimizer()
    # optimizer.optimize_ec2_instances()
    optimizer.snapshot_optimizer()

