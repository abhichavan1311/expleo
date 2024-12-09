import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Function to prompt the user for inputs with default values
def get_user_input():
    # Default values for each parameter
    default_region = "us-east-1"
    default_ami_id = "ami-0e2c8caa4b6378d8c"
    default_instance_type = "t2.micro"
    default_key_name = "useast1"
    default_security_group_id = "sg-0985e5338e2bd7ffe"
    default_tag_name = "test-abhi"

    # Prompt for each value and use the default if nothing is entered
    region = input(f"Enter AWS region (default {default_region}): ").strip() or default_region
    ami_id = input(f"Enter AMI ID (default {default_ami_id}): ").strip() or default_ami_id
    instance_type = input(f"Enter instance type (default {default_instance_type}): ").strip() or default_instance_type
    key_name = input(f"Enter your EC2 Key Pair name (default {default_key_name}): ").strip() or default_key_name
    security_group_id = input(f"Enter your Security Group ID (default {default_security_group_id}): ").strip() or default_security_group_id
    tag_name = input(f"Enter a name tag for your instance (default {default_tag_name}): ").strip() or default_tag_name

    # Return all values as a tuple
    return region, ami_id, instance_type, key_name, security_group_id, tag_name

# Function to create an EC2 instance using the provided parameters
def create_ec2_instance(region, ami_id, instance_type, key_name, security_group_id, tag_name):
    try:
        # Initialize a session using Boto3
        ec2 = boto3.client('ec2', region_name=region)

        # Launch an EC2 instance
        response = ec2.run_instances(
            ImageId=ami_id,                  # AMI ID for the instance
            InstanceType=instance_type,      # Instance type (e.g., t2.micro)
            MinCount=1,                      # Min number of instances to launch
            MaxCount=1,                      # Max number of instances to launch
            KeyName=key_name,                # EC2 Key Pair for SSH access
            SecurityGroupIds=[security_group_id],  # Security Group ID
            TagSpecifications=[             # Tagging the EC2 instance
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': tag_name  # Name tag for the EC2 instance
                        }
                    ]
                }
            ]
        )

        # Instance ID of the launched instance
        instance_id = response['Instances'][0]['InstanceId']
        print(f"EC2 Instance with ID {instance_id} launched successfully.")

        return instance_id

    except NoCredentialsError:
        print("No AWS credentials found. Please configure your AWS credentials.")
    except PartialCredentialsError:
        print("Incomplete AWS credentials. Please ensure both Access Key and Secret Key are configured.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to drive the script
if __name__ == "__main__":
    # Get user input for AWS parameters
    region, ami_id, instance_type, key_name, security_group_id, tag_name = get_user_input()

    # Create EC2 instance with the provided inputs
    create_ec2_instance(region, ami_id, instance_type, key_name, security_group_id, tag_name)

'''
Example Output:

(myenv) ubuntu@ip-172-31-86-180:/opt$ python3 create_instance.py
Enter AWS region (default us-east-1):
Enter AMI ID (default ami-0e2c8caa4b6378d8c):
Enter instance type (default t2.micro):
Enter your EC2 Key Pair name (default useast1):
Enter your Security Group ID (default sg-0985e5338e2bd7ffe):
Enter a name tag for your instance (default test-abhi):
EC2 Instance with ID i-0362141162e2c0fca launched successfully.
(myenv) ubuntu@ip-172-31-86-180:/opt$ cat create_instance.py

For more detailed output, please refer to screenshots in /AWS automation using boto3/readme.md
'''