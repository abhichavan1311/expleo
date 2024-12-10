import requests
import os
import boto3

# GitHub raw URL of the Python script
url = "https://raw.githubusercontent.com/abhichavan1311/expleo/main/AWS_automation_using_boto3/8_create_IAM_role.py"
local_file = "8_create_IAM_role.py"

def debug_aws_credentials():
    """Debugging function to check if AWS credentials are available."""
    session = boto3.Session()
    credentials = session.get_credentials()
    if credentials:
        print("AWS Credentials Found!")  # AWS credentials are available
    else:
        print("No AWS credentials detected!")  # AWS credentials are missing

debug_aws_credentials()  # Call the function to check AWS credentials

def download_script():
    """Downloads the Python script from the given URL in the same dir from where you running this script."""
    print(f"Downloading the script from {url}...")  # Print message for the start of the download process
    response = requests.get(url)  # Make an HTTP GET request to fetch the script

    if response.status_code == 200:  # Check if the request was successful (HTTP 200 OK)
        with open(local_file, "w") as file:  # Open a local file to save the downloaded script
            file.write(response.text)  # Write the script content to the file
        print(f"Script downloaded and saved to {local_file}")  # Confirmation message
    else:
        print(f"Failed to fetch script. HTTP Status: {response.status_code}")  # Error message if the request fails
        return False  # Return False if the download fails
    return True  # Return True if the script was successfully downloaded

def update_script(file_path):
    """Modifies the script if necessary."""
    print(f"Updating the script: {file_path}...")  # Print message before updating the script
    with open(file_path, "r") as file:  # Open the downloaded script for reading
        script_content = file.readlines()  # Read the script content line by line

    # Example modification (adding a print statement at the top)
    modified_content = []  # List to store modified content of the script
    for line in script_content:  # Loop through each line in the script
        if line.strip() == "import boto3":  # Check if the line contains 'import boto3'
            modified_content.append(line)  # Add the original line
            modified_content.append("print('Executing the modified IAM Role creation script')\n")  # Add a new print statement after the import
        else:
            modified_content.append(line)  # Add the other lines unchanged

    # Save the modified script back to the local file
    with open(file_path, "w") as file:
        file.writelines(modified_content)  # Write the modified content back to the file
    print("Script updated successfully.")  # Confirmation message that the script was updated

def execute_script(file_path):
    """Executes the local Python script."""
    print(f"Executing the script: {file_path}...")  # Print message before executing the script
    with open(file_path, "r") as file:  # Open the script for reading
        exec(file.read(), globals())  # Execute the script using exec()
    print("Script execution completed.")  # Confirmation message after execution

if __name__ == "__main__":
    # Main execution flow
    if download_script():  # Check if the script is downloaded successfully
        update_script(local_file)  # If downloaded, update the script as needed
        execute_script(local_file)  # After updating, execute the modified script

'''
Example Output:

ubuntu@ip-172-31-86-180:/opt$ sudo -E python3 Execute_script_from_github_url.py
AWS Credentials Found!
Downloading the script from https://raw.githubusercontent.com/abhichavan1311/expleo/main/AWS_automation_using_boto3/8_create_IAM_role.py...
Script downloaded and saved to 8_create_IAM_role.py
Updating the script: 8_create_IAM_role.py...
Script updated successfully.
Executing the script: 8_create_IAM_role.py...
Executing the modified IAM Role creation script
Enter IAM role name (default LambdaExecutionRole):
Enter tag key (leave empty to stop):
Role ARN: arn:aws:iam::010526261743:role/LambdaExecutionRole
Attached CloudWatchFullAccess policy to the role: LambdaExecutionRole
Created IAM Role ARN: arn:aws:iam::010526261743:role/LambdaExecutionRole
Attached Policy ARN: arn:aws:iam::aws:policy/CloudWatchFullAccess
Script execution completed.


Note: if you have doubt why we have used "sudo -E python3 Execute_script_from_github_url.py" while executing the script,refer /AWS automation using boto3/readme.md for more clarification

'''