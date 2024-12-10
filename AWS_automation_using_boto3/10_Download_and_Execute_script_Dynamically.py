import requests  # Used for making HTTP requests (here to download the Python script from GitHub)
import boto3     # AWS SDK for Python, allows interaction with AWS services (e.g., checking credentials)

# URL of the Python script hosted on GitHub
url = "https://raw.githubusercontent.com/abhichavan1311/expleo/main/AWS_automation_using_boto3/8_create_IAM_role.py"

# Function to check if AWS credentials are available on the system
def debug_aws_credentials():
    """
    This function checks if valid AWS credentials are configured on the local machine.
    It uses the boto3 Session object to retrieve credentials and prints the status.
    """
    session = boto3.Session()  # Create a session object to access AWS resources
    credentials = session.get_credentials()  # Get the AWS credentials
    if credentials:
        print("AWS Credentials Found!")  # If credentials are found, print a success message
    else:
        print("No AWS credentials detected!")  # If no credentials are found, print an error message

# Call the AWS credentials check function to confirm availability
debug_aws_credentials()

# Function to download the Python script from the provided GitHub URL
def download_script():
    """
    This function downloads the Python script from the GitHub raw URL and returns the content of the script.
    If the download is successful, the script content is returned as a string.
    If the download fails, it prints an error message and returns None.
    """
    print(f"Downloading the script from {url}...")  # Print a message indicating the download attempt
    response = requests.get(url)  # Make a GET request to fetch the content of the script

    # Check if the request was successful (HTTP status code 200 indicates success)
    if response.status_code == 200:
        print("Script downloaded successfully.")  # Confirm the script has been downloaded successfully
        return response.text  # Return the content of the downloaded script
    else:
        print(f"Failed to fetch script. HTTP Status: {response.status_code}")  # Print an error if the download failed
        return None  # Return None to indicate failure

# Function to execute the dynamically downloaded Python script
def execute_script(script_content):
    """
    This function takes the content of a Python script (as a string) and executes it dynamically.
    It uses the 'exec' function to execute the code in the current Python environment.
    """
    print("Executing the dynamically downloaded script...")  # Print a message indicating script execution
    exec(script_content, globals())  # Execute the content of the script within the global namespace
    print("Script execution completed.")  # Print a message after execution is completed

# Main execution block
if __name__ == "__main__":
    """
    This block orchestrates the flow of downloading and executing the Python script:
    1. Downloads the script from the GitHub URL.
    2. Executes the downloaded script content if the download was successful.
    """
    script_content = download_script()  # Download the script content from the URL
    if script_content:  # If the script content was downloaded successfully
        execute_script(script_content)  # Execute the downloaded script
'''
Example Output:

ubuntu@ip-172-31-86-180:/opt$ sudo -E python3 dynamically_execute_script.py
AWS Credentials Found!
Downloading the script from https://raw.githubusercontent.com/abhichavan1311/expleo/main/AWS_automation_using_boto3/8_create_IAM_role.py...
Script downloaded successfully.
Executing the dynamically downloaded script...
Enter IAM role name (default LambdaExecutionRole): test_lambda_role
Enter tag key (leave empty to stop):
Role ARN: arn:aws:iam::010526261743:role/test_lambda_role
Attached CloudWatchFullAccess policy to the role: test_lambda_role
Created IAM Role ARN: arn:aws:iam::010526261743:role/test_lambda_role
Attached Policy ARN: arn:aws:iam::aws:policy/CloudWatchFullAccess
Script execution completed.
ubuntu@ip-172-31-86-180:/opt$

For more detailed output and explanation, please refer to screenshots in /AWS automation using boto3/readme.md
'''