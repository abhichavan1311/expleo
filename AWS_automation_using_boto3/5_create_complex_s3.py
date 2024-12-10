import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Function to prompt the user for inputs with default values
def get_user_input():
    # Default values for each parameter
    default_bucket_name = "abhi-test-bucket-udd".lower().strip()
    default_region = "us-east-1"
    default_acl = "private"
    default_versioning = "False"
    default_encryption = "None"
    default_object_lock = "False"
    default_object_ownership = "BucketOwnerPreferred"

    # Prompt the user for each parameter
    bucket_name = input(f"Enter the S3 Bucket Name (default {default_bucket_name}): ").strip() or default_bucket_name
    region = input(f"Enter AWS region (default {default_region}): ").strip() or default_region
    acl = input(f"Enter ACL for the bucket (private, public-read, public-read-write, authenticated-read; default {default_acl}): ").strip() or default_acl
    versioning = input(f"Enable Versioning? (True/False, default {default_versioning}): ").strip() or default_versioning
    encryption = input(f"Choose encryption type (AES256, aws:kms, or None to disable encryption, default {default_encryption}): ").strip() or default_encryption
    object_lock = input(f"Enable Object Lock for the bucket? (True/False, default {default_object_lock}): ").strip().lower() or default_object_lock
    object_ownership = input(f"Set Object Ownership (BucketOwnerEnforced, ObjectWriter, BucketOwnerPreferred; default {default_object_ownership}): ").strip() or default_object_ownership

    # Convert boolean inputs to actual boolean values
    versioning = versioning.lower() == "true"

    # Prompt the user to enter multiple tags
    print("\nEnter tags for the bucket in the format 'Key=Value'. Type 'done' when finished.")
    tags = []
    while True:
        tag_input = input("Enter tag (or 'done' to finish): ").strip()
        if tag_input.lower() == "done":
            break
        if "=" in tag_input:
            key, value = tag_input.split("=", 1)
            tags.append({'Key': key.strip(), 'Value': value.strip()})
        else:
            print("Invalid format. Use 'Key=Value'.")

    # If no tags were provided, use a default tag
    if not tags:
        tags = [{'Key': 'Project', 'Value': 'Demo'}]

    return bucket_name, region, acl, versioning, encryption, object_lock, object_ownership, tags

# Function to create an S3 bucket with the provided parameters
def create_s3_bucket(bucket_name, region, acl, versioning, encryption, object_lock, object_ownership, tags):
    try:
        # Initialize a session using Boto3
        s3 = boto3.client('s3', region_name=region)

        s3.create_bucket(
            Bucket=bucket_name,
            ACL=acl,
            ObjectLockEnabledForBucket=object_lock.lower() == "true",
            ObjectOwnership=object_ownership
        )
        print(f"S3 Bucket '{bucket_name}' created successfully in region '{region}'.")

        # Block public access if requested
        if acl == "private":
            s3.put_public_access_block(
                Bucket=bucket_name,
                PublicAccessBlockConfiguration={
                    'BlockPublicAcls': True,
                    'IgnorePublicAcls': True,
                    'BlockPublicPolicy': True,
                    'RestrictPublicBuckets': True
                }
            )
            print("Public access blocked for the bucket.")

        # Enable versioning if requested
        if versioning:
            s3.put_bucket_versioning(
                Bucket=bucket_name,
                VersioningConfiguration={'Status': 'Enabled'}
            )
            print("Versioning enabled for the bucket.")

        # Set up server-side encryption if encryption is not disabled
        if encryption.lower() != "none":
            s3.put_bucket_encryption(
                Bucket=bucket_name,
                ServerSideEncryptionConfiguration={
                    'Rules': [
                        {
                            'ApplyServerSideEncryptionByDefault': {
                                'SSEAlgorithm': encryption
                            }
                        }
                    ]
                }
            )
            print(f"Server-side encryption set to '{encryption}' for the bucket.")
        else:
            print("Encryption is disabled for the bucket.")

        # Add tags to the bucket
        s3.put_bucket_tagging(
            Bucket=bucket_name,
            Tagging={
                'TagSet': tags
            }
        )
        print(f"Tags added to the bucket: {tags}")

        # Fetch the bucket location to confirm region and ARN
        location_response = s3.get_bucket_location(Bucket=bucket_name)
        bucket_region = location_response['LocationConstraint'] or 'us-east-1'  # Default region is 'us-east-1'
        
        # Construct the ARN
        bucket_arn = f"arn:aws:s3:::{bucket_name}"

        # Construct the endpoint URL
        endpoint_url = f"https://{bucket_name}.s3.{bucket_region}.amazonaws.com"

        # Output the ARN and endpoint
        print(f"S3 Bucket ARN: {bucket_arn}")
        print(f"S3 Bucket Endpoint: {endpoint_url}")

        return bucket_arn, endpoint_url

    except NoCredentialsError:
        print("No AWS credentials found. Please configure your AWS credentials.")
    except PartialCredentialsError:
        print("Incomplete AWS credentials. Please ensure both Access Key and Secret Key are configured.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to drive the script
if __name__ == "__main__":
    try:
        # Get user input for S3 bucket parameters
        bucket_name, region, acl, versioning, encryption, object_lock, object_ownership, tags = get_user_input()

        # Create the S3 bucket with the provided inputs and fetch the ARN and endpoint
        bucket_arn, endpoint_url = create_s3_bucket(bucket_name, region, acl, versioning, encryption, object_lock, object_ownership, tags)

        # Optionally, you can print the ARN and endpoint here as well
        print(f"Created S3 bucket with ARN: {bucket_arn}")
        print(f"Bucket endpoint: {endpoint_url}")
    except ValueError as e:
        print(f"Error: {e}")


'''
Example Output:

ubuntu@ip-172-31-86-180:/opt$ python3 s3_updated.py
Enter the S3 Bucket Name (default abhi-test-bucket-udd):
Enter AWS region (default us-east-1):
Enter ACL for the bucket (private, public-read, public-read-write, authenticated-read; default private):
Enable Versioning? (True/False, default False):
Choose encryption type (AES256, aws:kms, or None to disable encryption, default None):
Enable Object Lock for the bucket? (True/False, default False):
Set Object Ownership (BucketOwnerEnforced, ObjectWriter, BucketOwnerPreferred; default BucketOwnerPreferred):
Enter tags for the bucket in the format 'Key=Value'. Type 'done' when finished.
Enter tag (or 'done' to finish): env=prod
Enter tag (or 'done' to finish): created_by=Abhishek_Chavan
Enter tag (or 'done' to finish): done
S3 Bucket 'abhi-test-bucket-udd' created successfully in region 'us-east-1'.
Public access blocked for the bucket.
Encryption is disabled for the bucket.
Tags added to the bucket: [{'Key': 'env', 'Value': 'prod'}, {'Key': 'created_by', 'Value': 'Abhishek_Chavan'}]
S3 Bucket ARN: arn:aws:s3:::abhi-test-bucket-udd
S3 Bucket Endpoint: https://abhi-test-bucket-udd.s3.us-east-1.amazonaws.com
Created S3 bucket with ARN: arn:aws:s3:::abhi-test-bucket-udd
Bucket endpoint: https://abhi-test-bucket-udd.s3.us-east-1.amazonaws.com
ubuntu@ip-172-31-86-180:/opt$

'''