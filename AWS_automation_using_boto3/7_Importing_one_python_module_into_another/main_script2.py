# Import the function to create the SNS topic and subscription
from sns_utils import create_sns_topic_and_subscription
import boto3

def publish_message_to_sns(topic_arn):
    """
    Publishes a test message to the specified SNS topic.
    """
    sns_client = boto3.client('sns')

    try:
        message = input("Enter the message you want to publish to the topic (default: 'Test SNS Message'): ") or "Test SNS Message"
        subject = input("Enter the subject for the message (default: 'SNS Notification'): ") or "SNS Notification"

        # Publish the message to the SNS topic
        response = sns_client.publish(
            TopicArn=topic_arn,
            Message=message,
            Subject=subject
        )

        print(f"Message published successfully! Message ID: {response['MessageId']}")
    except Exception as e:
        print(f"Error publishing message: {e}")

if __name__ == "__main__":
    # Step 1: Create the SNS topic and subscription
    topic_arn, subscription_arn = create_sns_topic_and_subscription()
    print(f"Topic ARN: {topic_arn}")
    print(f"Subscription ARN: {subscription_arn}")

    # Step 2: Publish a test message to the created SNS topic
    publish_message_to_sns(topic_arn)


    
'''
Example Output

ubuntu@ip-172-31-86-180:/opt$ python3 main_script2.py
Enter the topic name (default: 'FileUploadNotifications'):
Enter the display name (default: 'File Upload Notifications'):
Enter the Environment tag value (default: 'Production'):
Enter the Department tag value (default: 'IT'):
Enter the email endpoint for subscription (default: 'abhichavan1311@gmail.com'):
Topic ARN: arn:aws:sns:us-east-1:010526261743:FileUploadNotifications
Subscription ARN (Pending Confirmation): pending confirmation
Please check your email to confirm the subscription. The process will continue after confirmation.
Enter the token from the confirmation email: 2336412f37fb687f5d51e6e2425ba1f30845f21ad62e58ce9729fe1b72a6a0b0c492db6eade8d196aa875a4cf393fc14dc2134e33a5c12740a636918376544ceea688357c3f7d64e3dc18a8c8d3248b9914200ce42135e5106ba34e8210e3efaa324168edfbbbe35b59cedf25d87ac2b21fe67a3e3d4efaea12cef2cc3828c7b
Subscription confirmed successfully.
Confirmed Subscription ARN: arn:aws:sns:us-east-1:010526261743:FileUploadNotifications:726fd4b3-1dbc-4ad1-bb98-0af0a77fccfc
Topic ARN: arn:aws:sns:us-east-1:010526261743:FileUploadNotifications
Subscription ARN: arn:aws:sns:us-east-1:010526261743:FileUploadNotifications:726fd4b3-1dbc-4ad1-bb98-0af0a77fccfc
Enter the message you want to publish to the topic (default: 'Test SNS Message'): Hi, we have succesfully imported one python module into another
Enter the subject for the message (default: 'SNS Notification'): we have done it, good work team
Message published successfully! Message ID: 8389afcf-afca-5277-a7fe-f01e52874779


'''