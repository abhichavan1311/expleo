# Import the function to create the SNS topic and subscription
from sns_utils import create_sns_topic_and_subscription
import boto3

# Call the function
if __name__ == "__main__":
    topic_arn, subscription_arn = create_sns_topic_and_subscription()
    print(f"Topic ARN: {topic_arn}")
    print(f"Subscription ARN: {subscription_arn}")


'''
Example Output

ubuntu@ip-172-31-86-180:/opt$ python3 main_script.py
Enter the topic name (default: 'FileUploadNotifications'):
Enter the display name (default: 'File Upload Notifications'):
Enter the Environment tag value (default: 'Production'):
Enter the Department tag value (default: 'IT'):
Enter the email endpoint for subscription (default: 'abhichavan1311@gmail.com'):
Topic ARN: arn:aws:sns:us-east-1:010526261743:FileUploadNotifications
Subscription ARN (Pending Confirmation): pending confirmation
Please check your email to confirm the subscription. The process will continue after confirmation.
Enter the token from the confirmation email: 2336412f37fb687f5d51e6e2425ba1f30845f21ad62e58ce9492cde0e0a549482fdef1c714a14c92b1673137733d0d379029d74f09d0f6373eb3b7e44d79fcbc5466a617adcf004a89ac13525218fa04d5d88d243ff58e6374fbdf96bb126aa240d8e87910b702b004e6c27523bdcdebac16a5cc75f1df554ab8762fbe3c0117
Subscription confirmed successfully.
Confirmed Subscription ARN: arn:aws:sns:us-east-1:010526261743:FileUploadNotifications:e1560f66-6fe5-4d8e-8e8b-f890ecb76a48
Topic ARN: arn:aws:sns:us-east-1:010526261743:FileUploadNotifications
Subscription ARN: arn:aws:sns:us-east-1:010526261743:FileUploadNotifications:e1560f66-6fe5-4d8e-8e8b-f890ecb76a48


'''