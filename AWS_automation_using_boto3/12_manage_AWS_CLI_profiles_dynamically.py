import boto3
import configparser
import os

def get_aws_profiles():
    """
    Reads the AWS configuration file to fetch available profiles.
    If no profiles are found, returns 'default'.
    """
    aws_config_path = os.path.expanduser("~/.aws/config")
    profiles = []

    if os.path.exists(aws_config_path):
        config = configparser.ConfigParser()
        config.read(aws_config_path)

        for section in config.sections():
            if section.startswith("profile "):
                profiles.append(section.split("profile ")[-1])

    # If no profiles are found, use 'default' profile
    if not profiles:
        profiles = ['default']

    return profiles

def select_profile(profiles):
    """
    Prompt the user to select an AWS profile from the available list.
    If only 'default' is available, automatically select it.
    """
    if len(profiles) == 1 and profiles[0] == "default":
        print("\nOnly the default AWS profile is available.")
        return "default"
    
    print("\nAvailable AWS Profiles:")
    for idx, profile in enumerate(profiles):
        print(f"{idx + 1}. {profile}")

    choice = int(input("\nSelect a profile by entering the number: "))
    if 1 <= choice <= len(profiles):
        return profiles[choice - 1]
    else:
        print("Invalid selection. Exiting.")
        exit(1)

def perform_task_with_profile(profile_name):
    """
    Performs AWS tasks using the selected profile.
    If no profile is provided, it uses 'default'.
    """
    # Initialize session with the selected profile
    session = boto3.Session(profile_name=profile_name)

    # Example AWS service interaction (list S3 buckets)
    s3_client = session.client("s3")
    buckets = s3_client.list_buckets()["Buckets"]

    print(f"\nS3 Buckets for profile '{profile_name}':")
    for bucket in buckets:
        print(f"- {bucket['Name']}")

if __name__ == "__main__":
    # Step 1: Get available profiles
    profiles = get_aws_profiles()
    if not profiles:
        print("No AWS profiles found in the configuration file.")
        exit(1)

    # Step 2: Select a profile
    selected_profile = select_profile(profiles)

    # Step 3: Perform AWS tasks using the selected profile
    perform_task_with_profile(selected_profile)

'''
Example Output:
ubuntu@ip-172-31-86-180:/opt/new$ python3 manage_profile.py

Available AWS Profiles:
1. abhishek_python

Select a profile by entering the number: 1

S3 Buckets for profile 'abhishek_python':
- abhi-ahshdhdjdkk
ubuntu@ip-172-31-86-180:/opt/new$

Example Output2:
ubuntu@ip-172-31-86-180:/opt/new$ python3 manage_profile.py

Only the default AWS profile is available.

S3 Buckets for profile 'default':

'''