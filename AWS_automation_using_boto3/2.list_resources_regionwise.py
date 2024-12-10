import boto3  # Importing boto3, the AWS SDK for Python
import argparse  # Importing argparse for parsing command-line arguments
from botocore.exceptions import NoCredentialsError, PartialCredentialsError  # Importing AWS credential exceptions, if any related error occurs it will prompt defined message

# Function to parse command-line arguments
def parse_arguments():
    # Creating an ArgumentParser object to handle command-line arguments
    parser = argparse.ArgumentParser(description="AWS Resource Listing Script")
    # Adding the required '--region' argument which specifies the AWS region
    parser.add_argument('--region', required=True, help='AWS region (e.g., us-east-1, eu-west-1)')
    # Parsing and returning the arguments
    return parser.parse_args()

# Function to list EC2 instances in the specified region
def list_ec2_instances(region):
    # Creating an EC2 client with the specified region
    ec2 = boto3.client('ec2', region_name=region)
    try:
        # Describing instances and retrieving the response
        response = ec2.describe_instances()
        instances = response['Reservations']  # Extracting instances data from the response
        print("\nEC2 Instances:")
        # Looping through reservations and instances to print details
        for reservation in instances:
            for instance in reservation['Instances']:
                # Get the instance name from the tags (if available)
                instance_name = "No Name"  # Default value if no Name tag is found
                tags = instance.get('Tags', [])
                # Print all tags for the instance
                print(f"ID: {instance['InstanceId']} - State: {instance['State']['Name']}")
                print(f"Tags:")
                for tag in tags:
                    print(f"  {tag['Key']}: {tag['Value']}")
    except NoCredentialsError:
        print("No AWS credentials found. Please configure your AWS credentials.")
    except PartialCredentialsError:
        print("Incomplete AWS credentials. Please ensure both Access Key and Secret Key are configured.")
    except Exception as e:
        # Catching any exceptions and printing the error message
        print(f"Error listing EC2 instances: {e}")

# Function to list all S3 buckets in the specified region
def list_s3_buckets(region):
    # Creating an S3 client with the specified region
    s3 = boto3.client('s3', region_name=region)
    try:
        # Listing all the S3 buckets
        response = s3.list_buckets()
        buckets = response['Buckets']  # Extracting the bucket details
        print("\nS3 Buckets:")
        # Looping through each bucket and printing its name and tags
        for bucket in buckets:
            print(f"Name: {bucket['Name']}")
            # Get the tags for the bucket
            try:
                tags = s3.get_bucket_tagging(Bucket=bucket['Name'])['TagSet']
                print(f"Tags:")
                for tag in tags:
                    print(f"  {tag['Key']}: {tag['Value']}")
            except s3.exceptions.NoSuchTagSet:
                print("  No tags found for this bucket.")
    except NoCredentialsError:
        print("No AWS credentials found. Please configure your AWS credentials.")
    except PartialCredentialsError:
        print("Incomplete AWS credentials. Please ensure both Access Key and Secret Key are configured.")
    except Exception as e:
        # Catching any exceptions and printing the error message
        print(f"Error listing S3 buckets: {e}")

# Function to list all Lambda functions in the specified region
def list_lambdas(region):
    # Creating a Lambda client with the specified region
    lambda_client = boto3.client('lambda', region_name=region)
    try:
        # Listing all Lambda functions
        response = lambda_client.list_functions()
        functions = response['Functions']  # Extracting the function details
        print("\nLambda Functions:")
        # Looping through each Lambda function and printing its name and tags
        for function in functions:
            function_name = function['FunctionName']
            print(f"Function Name: {function_name}")
            # Get the tags for the Lambda function
            try:
                tags = lambda_client.list_tags(Resource=function_name)['Tags']
                print(f"Tags:")
                for key, value in tags.items():
                    print(f"  {key}: {value}")
            except Exception as e:
                print(f"  Error fetching tags for {function_name}: {e}")
    except NoCredentialsError:
        print("No AWS credentials found. Please configure your AWS credentials.")
    except PartialCredentialsError:
        print("Incomplete AWS credentials. Please ensure both Access Key and Secret Key are configured.")
    except Exception as e:
        # Catching any exceptions and printing the error message
        print(f"Error listing Lambda functions: {e}")

# Function to list all RDS instances in the specified region
def list_rds_instances(region):
    # Creating an RDS client with the specified region
    rds = boto3.client('rds', region_name=region)
    try:
        # Describing all the RDS instances
        response = rds.describe_db_instances()
        db_instances = response['DBInstances']  # Extracting the DB instances details
        print("\nRDS Instances:")
        # Looping through each RDS instance and printing its identifier, status, and tags
        for db_instance in db_instances:
            db_instance_identifier = db_instance['DBInstanceIdentifier']
            print(f"DB Instance Identifier: {db_instance_identifier} - Status: {db_instance['DBInstanceStatus']}")
            # Get the tags for the DB instance
            try:
                tags = rds.list_tags_for_resource(ResourceName=db_instance['DBInstanceArn'])['TagList']
                print(f"Tags:")
                for tag in tags:
                    print(f"  {tag['Key']}: {tag['Value']}")
            except Exception as e:
                print(f"  Error fetching tags for {db_instance_identifier}: {e}")
    except NoCredentialsError:
        print("No AWS credentials found. Please configure your AWS credentials.")
    except PartialCredentialsError:
        print("Incomplete AWS credentials. Please ensure both Access Key and Secret Key are configured.")
    except Exception as e:
        # Catching any exceptions and printing the error message
        print(f"Error listing RDS instances: {e}")

# Main function that calls the functions for each AWS resource and lists them
def list_active_resources(region):
    # Calling each function to list resources for the specified region
    list_ec2_instances(region)
    list_s3_buckets(region)
    list_lambdas(region)
    list_rds_instances(region)

# Entry point of the script
if __name__ == '__main__':
    # Parse command-line arguments to get the region
    args = parse_arguments()

    # List all resources in the provided AWS region
    list_active_resources(args.region)

'''
Below we have shown 3 output with different regions or scenarios

Example Output:

output1:
(myenv) ubuntu@ip-172-31-86-180:/opt$ python3 tp2.py --region us-east-1

EC2 Instances:
ID: i-0ed4ace044521ae54 - State: stopped
Tags:
  Name: master
ID: i-0c561cec229abb411 - State: running
Tags:
  Name: AWS_AUTOMATION

S3 Buckets:
Name: tpabhi
Tags:
  env: production

Lambda Functions:

RDS Instances:

Output2:
(myenv) ubuntu@ip-172-31-86-180:/opt$ python3 tp2.py
usage: tp2.py [-h] --region REGION
tp2.py: error: the following arguments are required: --region

Output3:
(myenv) ubuntu@ip-172-31-86-180:/opt$ python3 tp2.py --help
usage: tp2.py [-h] --region REGION

AWS Resource Listing Script

options:
  -h, --help       show this help message and exit
  --region REGION  AWS region (e.g., us-east-1, eu-west-1)
(myenv) ubuntu@ip-172-31-86-180:/opt$

Note: For detailed output refer screenshots in /AWS automation using boto3/readme.md

'''
