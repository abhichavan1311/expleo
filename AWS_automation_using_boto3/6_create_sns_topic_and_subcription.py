import boto3
import time
import subprocess
import json

# Create an SNS client
sns_client = boto3.client('sns')

# Prompt the user for input and provide default values if no input is provided
name = input("Enter the topic name (default: 'FileUploadNotifications'): ") or 'FileUploadNotifications'

# Input for the Display Name attribute
display_name = input("Enter the display name (default: 'File Upload Notifications'): ") or 'File Upload Notifications'

# Input for tags
env_tag = input("Enter the Environment tag value (default: 'Production'): ") or 'Production'
dept_tag = input("Enter the Department tag value (default: 'IT'): ") or 'IT'

# Input for the endpoint (email) to subscribe to the SNS topic
endpoint = input("Enter the email endpoint for subscription (default: 'abhichavan1311@gmail.com'): ") or 'abhichavan1311@gmail.com'

# Create the topic with the provided or default values
response = sns_client.create_topic(
    Name=name,
    Attributes={
        'DisplayName': display_name
    },
    Tags=[
        {'Key': 'Environment', 'Value': env_tag},
        {'Key': 'Department', 'Value': dept_tag}
    ]
)

# Print the response which contains the topic ARN
topic_arn = response['TopicArn']
print("Topic ARN:", topic_arn)

# Now, subscribe the provided endpoint (email) to the topic
subscription_response = sns_client.subscribe(
    TopicArn=topic_arn,
    Protocol='email',
    Endpoint=endpoint  
)

# Get the subscription ARN (it will initially be in 'pending confirmation' state)
subscription_arn = subscription_response['SubscriptionArn']
print(f"Subscription ARN (Pending Confirmation): {subscription_arn}")

# Wait for the user to confirm the subscription manually (since this is an email subscription)
print("Please check your email to confirm the subscription. The process will continue after confirmation.")
token = input("Enter the token from the confirmation email: ")

# Confirm the subscription using the token
try:
    confirmation_response = sns_client.confirm_subscription(
        TopicArn=topic_arn,
        Token=token,
        AuthenticateOnUnsubscribe='false'
    )
    print("Subscription confirmed successfully.")
except Exception as e:
    print(f"Error confirming subscription: {e}")
    exit(1)

# Add a delay of 15 seconds to allow the subscription ARN to be created
time.sleep(15)

# Execute "aws sns list-subscriptions" command to fetch all subscriptions
try:
    result = subprocess.run(
        ["aws", "sns", "list-subscriptions"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode != 0:
        print(f"Error executing AWS CLI command: {result.stderr}")
        exit(1)

    # Parse the output of the AWS CLI command
    subscriptions = json.loads(result.stdout)['Subscriptions']

    # Look for the matching endpoint and extract the SubscriptionArn
    confirmed_subscription_arn = None
    for subscription in subscriptions:
        if subscription['Endpoint'] == endpoint:
            confirmed_subscription_arn = subscription['SubscriptionArn']
            break

    if not confirmed_subscription_arn:
        print("Failed to fetch a confirmed SubscriptionArn.")
        exit(1)

    print(f"Confirmed Subscription ARN: {confirmed_subscription_arn}")
except Exception as e:
    print(f"Error fetching subscription ARN: {e}")
    exit(1)

'''
Example Output:

(myenv) ubuntu@ip-172-31-86-180:/opt$ python3 sns_topic.py
Enter the topic name (default: 'FileUploadNotifications'):
Enter the display name (default: 'File Upload Notifications'):
Enter the Environment tag value (default: 'Production'):
Enter the Department tag value (default: 'IT'):
Enter the email endpoint for subscription (default: 'abhichavan1311@gmail.com'):
Topic ARN: arn:aws:sns:us-east-1:010526261743:FileUploadNotifications
Subscription ARN (Pending Confirmation): pending confirmation
Please check your email to confirm the subscription. The process will continue after confirmation.
Enter the token from the confirmation email: 2336412f37fb687f5d51e6e2425ba1f30845f3382f4eb5847aafbb779650988dfd16b53365ead90cab8915893cea07669acaafe3dcc1240ad4ed1480e740e5a24f97d876996006664d1ef3c2814897bd8415c88eda2aec6388dc6ca5fb63600338ffebc3778f4aa2209b657ff684d04cd8b1eb95403511f62e905a20e6426606
Subscription confirmed successfully.
Confirmed Subscription ARN: arn:aws:sns:us-east-1:010526261743:FileUploadNotifications:288604f3-f815-4e31-8a3f-fb7d84aae131
(myenv) ubuntu@ip-172-31-86-180:/opt$

For more detailed output, please refer to screenshots in /AWS automation using boto3/readme.md
'''
