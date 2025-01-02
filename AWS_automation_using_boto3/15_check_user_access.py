#check user access for s3 and ec2 services
import boto3
import json

def get_account_id(iam):
    """Fetches the AWS account ID."""
    sts = boto3.client('sts')
    identity = sts.get_caller_identity()
    return identity['Account']

def get_user_policies(iam, user_name):
    """Fetches the list of policies attached to the user."""
    policies = []
    # Get managed policies attached to the user
    response = iam.list_attached_user_policies(UserName=user_name)
    for policy in response['AttachedPolicies']:
        policies.append(policy['PolicyArn'])
    return policies

def evaluate_policy_for_action(policy_document, action, region):
    """Evaluates the policy document to check if it allows the given action in the specified region."""
    for statement in policy_document['Statement']:
        if statement['Effect'] == 'Allow' and action in statement['Action']:
            # Check for the region condition
            if 'Condition' in statement and 'StringEquals' in statement['Condition'] and \
                'aws:RequestedRegion' in statement['Condition']['StringEquals']:
                allowed_regions = statement['Condition']['StringEquals']['aws:RequestedRegion']
                if region in allowed_regions:
                    return True
    return False

def get_policy_document(iam, policy_arn):
    """Fetches the policy document for a specific policy ARN."""
    response = iam.get_policy(PolicyArn=policy_arn)
    policy_version = response['Policy']['DefaultVersionId']
    policy_document_response = iam.get_policy_version(
        PolicyArn=policy_arn,
        VersionId=policy_version
    )
    return policy_document_response['PolicyVersion']['Document']

def check_permissions(iam, user_name, service, region):
    """Check the permissions for the specified user based on attached policies."""
    actions = {
        "s3": ["s3:CreateBucket", "s3:ListBuckets", "s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
        "ec2": ["ec2:DescribeInstances", "ec2:StartInstances", "ec2:StopInstances", "ec2:TerminateInstances"]
    }
    
    if service not in actions:
        print(f"No predefined actions found for service '{service}'.")
        return
    
    actions_to_check = actions[service]
    permissions_found = False

    print(f"Checking permissions for user '{user_name}' on service '{service}' in region '{region}'...")
    
    policies = get_user_policies(iam, user_name)

    # Iterate over each policy attached to the user
    for policy_arn in policies:
        print(f"Checking policy: {policy_arn}")
        policy_document = get_policy_document(iam, policy_arn)
        
        for action in actions_to_check:
            if evaluate_policy_for_action(policy_document, action, region):
                print(f"User '{user_name}' is allowed to perform '{action}' in region '{region}'.")
                permissions_found = True
            else:
                print(f"User '{user_name}' is NOT allowed to perform '{action}' in region '{region}'.")

    if not permissions_found:
        print(f"User '{user_name}' does not have any permissions for the '{service}' service in region '{region}'.")

def main():
    # Setup
    iam = boto3.client('iam')
    user_name = input("Enter the username: ").strip()
    region = input("Enter the region you want to check permissions for: ").strip()
    service = input("Enter the service you want to check (e.g., s3, ec2): ").strip().lower()

    check_permissions(iam, user_name, service, region)

if __name__ == "__main__":
    boto3.set_stream_logger(name='botocore', level='DEBUG')  # Enable debug logging
    main()


'''example Output:
59013a0>
User 'abhishek_test' is NOT allowed to perform 'ec2:DescribeInstances' in region 'us-east-1'.
User 'abhishek_test' is NOT allowed to perform 'ec2:StartInstances' in region 'us-east-1'.
User 'abhishek_test' is NOT allowed to perform 'ec2:StopInstances' in region 'us-east-1'.
User 'abhishek_test' is NOT allowed to perform 'ec2:TerminateInstances' in region 'us-east-1'.
User 'abhishek_test' does not have any permissions for the 'ec2' service in region 'us-east-1'.
ubuntu@ip-172-31-86-180:/opt/new$

example output2:

User 'abhishek_test' is allowed to perform 's3:CreateBucket' in region 'us-east-1'.
User 'abhishek_test' is NOT allowed to perform 's3:ListBuckets' in region 'us-east-1'.
User 'abhishek_test' is NOT allowed to perform 's3:GetObject' in region 'us-east-1'.
User 'abhishek_test' is NOT allowed to perform 's3:PutObject' in region 'us-east-1'.
User 'abhishek_test' is NOT allowed to perform 's3:DeleteObject' in region 'us-east-1'.

'''