import boto3
import json  # Importing json to handle the trust policy properly

def get_user_input():
    # Default values for IAM role creation
    default_role_name = "LambdaExecutionRole"
    
    # Prompt for the IAM role name
    role_name = input(f"Enter IAM role name (default {default_role_name}): ").strip() or default_role_name

    # Ask for multiple tags
    tags = []
    while True:
        tag_key = input("Enter tag key (leave empty to stop): ").strip()
        if not tag_key:  # Stop if the user doesn't enter a tag key
            break
        tag_value = input(f"Enter value for tag key '{tag_key}': ").strip()
        tags.append({'Key': tag_key, 'Value': tag_value})

    return role_name, tags

def create_iam_role(role_name, tags):
    # Create an IAM client
    iam_client = boto3.client('iam')

    # Define trust relationship policy (trusting AWS Lambda service)
    trust_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "lambda.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }

    # Convert the trust policy to a JSON string
    trust_policy_json = json.dumps(trust_policy)

    # Create the IAM role
    response = iam_client.create_role(
        RoleName=role_name,
        AssumeRolePolicyDocument=trust_policy_json,  # Pass JSON string here
        Description=f"Role for Lambda function with access to CloudWatch",
    )
    role_arn = response['Role']['Arn']
    print(f"Role ARN: {role_arn}")

    # Add tags to the IAM role
    if tags:
        iam_client.tag_role(
            RoleName=role_name,
            Tags=tags
        )
        print(f"Tags added to the role: {tags}")

    # Attach the managed policy to the IAM role for full CloudWatch access
    policy_response = iam_client.attach_role_policy(
        RoleName=role_name,
        PolicyArn="arn:aws:iam::aws:policy/CloudWatchFullAccess"
    )
    policy_arn = "arn:aws:iam::aws:policy/CloudWatchFullAccess"
    print(f"Attached CloudWatchFullAccess policy to the role: {role_name}")

    # Return the ARNs of the resources
    return role_arn, policy_arn

if __name__ == "__main__":
    role_name, tags = get_user_input()
    role_arn, policy_arn = create_iam_role(role_name, tags)
    
    # Print the ARNs of the created resources
    print(f"Created IAM Role ARN: {role_arn}")
    print(f"Attached Policy ARN: {policy_arn}")


'''
Example Output:

ubuntu@ip-172-31-86-180:/opt$ python3 create_iam_role.py
Enter IAM role name (default LambdaExecutionRole):
Enter tag key (leave empty to stop): env
Enter value for tag key 'env': prod
Enter tag key (leave empty to stop): created_by
Enter value for tag key 'created_by': abhishek_chavan
Enter tag key (leave empty to stop):
Role ARN: arn:aws:iam::010526261743:role/LambdaExecutionRole
Tags added to the role: [{'Key': 'env', 'Value': 'prod'}, {'Key': 'created_by', 'Value': 'abhishek_chavan'}]
Attached CloudWatchFullAccess policy to the role: LambdaExecutionRole
Created IAM Role ARN: arn:aws:iam::010526261743:role/LambdaExecutionRole
Attached Policy ARN: arn:aws:iam::aws:policy/CloudWatchFullAccess
ubuntu@ip-172-31-86-180:/opt$

For more detailed output, please refer to screenshots in /AWS automation using boto3/readme.md


'''