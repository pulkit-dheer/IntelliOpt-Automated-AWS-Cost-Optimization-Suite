import boto3
import logging

logging.basicConfig(level=logging.INFO)

ec2 = boto3.client('ec2')

regions = ec2.describe_regions()
all_region = []


for region in regions['Regions']:
    region_names = region['RegionName']
    all_region.append(region_names)






for region in all_region:
    regional_ec2_client = boto3.client('ec2', region_name=region)

    all_ec2_data = regional_ec2_client.describe_instances()

    # Iterate over each reservation
    for reservation in all_ec2_data['Reservations']:
        # Iterate over each instance in the reservation
        for instance in reservation['Instances']:
            # Check if the instance has tags
            if 'Tags' in instance:
                # Loop through each tag and print key-value pairs
                for tag in instance['Tags']:
                    if tag['Key'] == 'Environment' and tag['Value'] in ['staging', 'dev']:
                        print(f" - {tag['Key']}: {tag['Value']}")
                        print(f"Instance ID: {instance['InstanceId']} has the following tags:") 
            else:
                print(f"Instance ID: {instance['InstanceId']} has no tags.")






