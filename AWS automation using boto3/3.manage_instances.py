# Python script to start and stop EC2 instances based on the user-provided instance tags, start time, and stop time (providing inputs to the functions).
import boto3
import argparse
import time
from datetime import datetime
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Function to parse command-line arguments
def parse_arguments():
    """
    Parses the command-line arguments.
    --region: AWS region where the EC2 instances are located.
    --start-time: The time (in HH:MM format) to start the EC2 instances.
    --stop-time: The time (in HH:MM format) to stop the EC2 instances.
    --tags: The tags in JSON format (e.g., {"Key": "Value"}) that will be used to filter EC2 instances.
    """
    parser = argparse.ArgumentParser(description="AWS EC2 Instance Start/Stop Script")
    parser.add_argument('--region', required=True, help='AWS region (e.g., us-east-1, eu-west-1)')
    parser.add_argument('--start-time', required=True, help='Time to start the instance in HH:MM format')
    parser.add_argument('--stop-time', required=True, help='Time to stop the instance in HH:MM format')
    parser.add_argument('--tags', required=True, help='Tags of the instance in JSON format (e.g., {"Key": "Value"})')
    return parser.parse_args()

# Function to get EC2 instances based on tags
def get_instances_by_tags(region, tags):
    """
    Filters EC2 instances by the provided tags and fetches those instances from the specified region.
    It uses the DescribeInstances API call to filter instances by tag and fetch their details.
    """
    ec2 = boto3.client('ec2', region_name=region)
    try:
        # Create filter parameters to match EC2 instances based on the provided tags
        filters = [{'Name': f'tag:{key}', 'Values': [value]} for key, value in tags.items()]
        
        # Describe instances with the filters for the specified region
        response = ec2.describe_instances(Filters=filters)
        
        instances = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instances.append(instance)  # Append the matching instances
        
        return instances
    except NoCredentialsError:
        print("No AWS credentials found. Please configure your AWS credentials.")
        return []
    except PartialCredentialsError:
        print("Incomplete AWS credentials. Please ensure both Access Key and Secret Key are configured.")
        return []
    except Exception as e:
        print(f"Error fetching instances by tags: {e}")
        return []

# Function to start an EC2 instance
def start_instance(instance_id, region):
    """
    Starts the EC2 instance identified by the instance_id in the specified AWS region.
    Calls the StartInstances API to start the instance.
    """
    ec2 = boto3.client('ec2', region_name=region)
    try:
        ec2.start_instances(InstanceIds=[instance_id])
        print(f"Instance {instance_id} started.")
    except Exception as e:
        print(f"Error starting instance {instance_id}: {e}")

# Function to stop an EC2 instance
def stop_instance(instance_id, region):
    """
    Stops the EC2 instance identified by the instance_id in the specified AWS region.
    Calls the StopInstances API to stop the instance.
    """
    ec2 = boto3.client('ec2', region_name=region)
    try:
        ec2.stop_instances(InstanceIds=[instance_id])
        print(f"Instance {instance_id} stopped.")
    except Exception as e:
        print(f"Error stopping instance {instance_id}: {e}")

# Function to check the current time against the start or stop time
def is_time_to_run(target_time):
    """
    Compares the current time with the target time (start or stop time).
    Returns True if the current time matches the target time, else False.
    """
    current_time = datetime.now().strftime('%H:%M')
    return current_time == target_time

# Main function to control instance start/stop based on time and tags
def manage_instance(region, start_time, stop_time, tags):
    """
    Manages EC2 instances based on the provided tags, start time, and stop time.
    This function continuously checks the current time and starts or stops instances based on the given times.
    """
    # Get instances based on the tags provided
    instances = get_instances_by_tags(region, tags)
    
    # Loop to keep checking the time and control instances
    while True:
        # Check if it's time to start the instances
        if is_time_to_run(start_time):
            for instance in instances:
                start_instance(instance['InstanceId'], region)
        
        # Check if it's time to stop the instances
        if is_time_to_run(stop_time):
            for instance in instances:
                stop_instance(instance['InstanceId'], region)

        # Wait for 60 seconds before checking the time again to avoid overwhelming the system
        time.sleep(60)

# Entry point of the script
if __name__ == '__main__':
    # Parse command-line arguments to get region, start time, stop time, and tags
    args = parse_arguments()

    # Convert tags input to a dictionary (from string to actual dictionary)
    try:
        tags = eval(args.tags)  # Convert the tags string input into a dictionary format
        if not isinstance(tags, dict):
            raise ValueError("Tags should be a dictionary in the format {'Key': 'Value'}")
    except Exception as e:
        print(f"Error parsing tags: {e}")
        exit(1)

    # Start managing EC2 instances based on the provided region, times, and tags
    manage_instance(args.region, args.start_time, args.stop_time, tags)

'''
Example Output:
(myenv) ubuntu@ip-172-31-86-180:/opt$ python3 tp.py --region us-east-1 --start-time 14:31 --stop-time 14:33 --tags '{"Name": "master"}' &      [2] 3674
(myenv) ubuntu@ip-172-31-86-180:/opt$
(myenv) ubuntu@ip-172-31-86-180:/opt$ Instance i-0ed4ace044521ae54 started.

(myenv) ubuntu@ip-172-31-86-180:/opt$ date
Mon Dec  9 14:31:49 IST 2024
(myenv) ubuntu@ip-172-31-86-180:/opt$ Instance i-0ed4ace044521ae54 stopped.

(myenv) ubuntu@ip-172-31-86-180:/opt$ date
Mon Dec  9 14:33:52 IST 2024
(myenv) ubuntu@ip-172-31-86-180:/opt$


For more detailed output, please refer to screenshots in /AWS automation using boto3/readme.md
'''
