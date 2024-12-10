# Import the function to create the SNS topic and subscription
from AWS_automation_using_boto3.7_calling_one_module_into_other_code.create_sns_topic_and_subcription import create_sns_topic_and_subscription
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
