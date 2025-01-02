import time
import boto3
import json

def get_account_id(iam):
    """Fetches the AWS account ID dynamically."""
    sts = boto3.client('sts')
    response = sts.get_caller_identity()
    return response['Account']

def create_policy(iam, policy_name, policy_document):
    try:
        # Check if the policy already exists
        iam.get_policy(PolicyArn=f"arn:aws:iam::{get_account_id(iam)}:policy/{policy_name}")
        print(f"Policy '{policy_name}' already exists.")
    except iam.exceptions.NoSuchEntityException:
        # Create the policy if it does not exist
        print(f"Creating policy '{policy_name}'...")
        iam.create_policy(
            PolicyName=policy_name,
            PolicyDocument=policy_document
        )

def attach_policy_to_user(iam, user_name, policy_arn):
    try:
        iam.attach_user_policy(
            UserName=user_name,
            PolicyArn=policy_arn
        )
        print(f"Policy '{policy_arn}' attached to user '{user_name}'.")
    except iam.exceptions.NoSuchEntityException as e:
        print(f"Error attaching policy: {str(e)}")

def wait_for_policy(iam, policy_name, account_id, wait_time=60, retry_interval=10):
    """
    Waits for the policy to be created. Retries continuously until created.
    """
    while True:
        try:
            # Check if the policy exists
            policy_arn = f"arn:aws:iam::{account_id}:policy/{policy_name}"
            response = iam.get_policy(PolicyArn=policy_arn)
            print(f"Policy '{policy_name}' is now available. ARN: {policy_arn}")
            return policy_arn
        except iam.exceptions.NoSuchEntityException:
            print(f"Policy '{policy_name}' not found. Retrying in {retry_interval} seconds...")
            time.sleep(retry_interval)

def main():
    # Setup
    iam = boto3.client('iam')
    account_id = get_account_id(iam)  # Get the AWS account ID
    user_name = input("Enter the username: ").strip()
    region = input("Enter the allowed region for resource creation: ").strip()

    # Unique policy name
    policy_name = f"RestrictS3CreationTo{region}-{int(time.time())}"

    # Policy document (example)
    policy_document = json.dumps({
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "s3:CreateBucket",
                "Resource": f"arn:aws:s3:::*",
                "Condition": {
                    "StringEquals": {
                        "aws:RequestedRegion": region
                    }
                }
            }
        ]
    })

    # Create policy if it doesn't exist
    create_policy(iam, policy_name, policy_document)

    # Wait for 60 seconds before checking for the policy
    print("Waiting 60 seconds before checking for the policy...")
    time.sleep(60)

    # Wait and retry to check for the policy
    policy_arn = wait_for_policy(iam, policy_name, account_id)

    # Attach the policy to user
    attach_policy_to_user(iam, user_name, policy_arn)

if __name__ == "__main__":
    boto3.set_stream_logger(name='botocore', level='DEBUG')  # Enable debug logging
    main()

'''
to verify if this script is working or not, please refer task no 15- check_user_access where I have created script to check user access
'''

