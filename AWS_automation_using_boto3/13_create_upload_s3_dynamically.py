import boto3
import os
import json

def get_user_input(prompt, default_value=None):
    """
    Prompts the user for input and uses the default_value if no input is provided.
    """
    user_input = input(f"{prompt} [{default_value}]: ").strip()
    return user_input if user_input else default_value

def create_s3_bucket(region, bucket_name):
    """
    Create an S3 bucket in the specified region.
    """
    s3 = boto3.client('s3', region_name=region)

    # If the region is 'us-east-1', do not specify the LocationConstraint
    if region == "us-east-1":
        s3.create_bucket(Bucket=bucket_name)
    else:
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': region}
        )

    print(f"S3 bucket '{bucket_name}' created in region '{region}'.")

def disable_block_public_policy(bucket_name):
    """
    Disable the BlockPublicAccess setting on the S3 bucket to allow public access.
    """
    s3 = boto3.client('s3')

    # Disable the BlockPublicAcls and IgnorePublicAcls settings to allow public access
    s3.put_public_access_block(
        Bucket=bucket_name,
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': False,
            'IgnorePublicAcls': False,
            'BlockPublicPolicy': False,
            'RestrictPublicBuckets': False
        }
    )

    print(f"Public access disabled for bucket '{bucket_name}'.")

def set_bucket_public_access(bucket_name):
    """
    Set the S3 bucket's policy to allow public access to the uploaded file.
    """
    s3 = boto3.client('s3')

    # Bucket Policy for public read access
    bucket_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "PublicReadGetObject",
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": f"arn:aws:s3:::{bucket_name}/*"
            }
        ]
    }

    # Apply the policy
    s3.put_bucket_policy(
        Bucket=bucket_name,
        Policy=json.dumps(bucket_policy)
    )

    print(f"Bucket policy updated to allow public access to objects in '{bucket_name}'.")

def upload_file_to_s3(bucket_name, file_path, object_key):
    """
    Upload a file to the S3 bucket.
    """
    s3 = boto3.client('s3')

    # Upload the file
    s3.upload_file(file_path, bucket_name, object_key)

    print(f"File '{file_path}' uploaded to S3 bucket '{bucket_name}' as '{object_key}'.")

if __name__ == "__main__":
    # Step 1: Get bucket region, bucket name, and key
    region = get_user_input("Enter the region for the S3 bucket", "us-east-1")
    bucket_name = get_user_input("Enter the name for the S3 bucket", "abhishek-1234hsgsg")
    object_key = get_user_input("Enter the key for the object in S3 (e.g., class)", "class")

    # Step 2: Ask for the key value
    key_value = input(f"Enter the value for the key '{object_key}': ").strip()

    # Step 3: Create the S3 bucket
    create_s3_bucket(region, bucket_name)

    # Step 4: Disable BlockPublicPolicy for the bucket to allow public access
    disable_block_public_policy(bucket_name)

    # Step 5: Set the bucket policy for public access
    set_bucket_public_access(bucket_name)

    # Step 6: Ask for the file to upload
    file_path = input("Enter the full path of the file to upload: ").strip()

    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist. Exiting.")
        exit(1)

    # Step 7: Upload the file to S3
    upload_file_to_s3(bucket_name, file_path, object_key)

'''
Example Output:
ubuntu@ip-172-31-86-180:/opt/new$ python3 s3_upload.py
Enter the region for the S3 bucket [us-east-1]:
Enter the name for the S3 bucket [abhishek-1234hsgsg]:
Enter the key for the object in S3 (e.g., class) [class]:
Enter the value for the key 'class': kucl2.2
S3 bucket 'abhishek-1234hsgsg' created in region 'us-east-1'.
Public access disabled for bucket 'abhishek-1234hsgsg'.
Bucket policy updated to allow public access to objects in 'abhishek-1234hsgsg'.
Enter the full path of the file to upload: unnati.txt
File 'unnati.txt' uploaded to S3 bucket 'abhishek-1234hsgsg' as 'class'.
ubuntu@ip-172-31-86-180:/opt/new$ sudo cat s3_upload.py

'''