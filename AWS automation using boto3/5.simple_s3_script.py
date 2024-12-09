import boto3

# Initialize the S3 client
client = boto3.client('s3')

response = client.create_bucket(
    ACL='private',  # Select an appropriate ACL
    Bucket='test-abhi-shdgdgjs',  # Replace with your bucket name
    ObjectLockEnabledForBucket=True,  # Enable object lock if needed
    ObjectOwnership='BucketOwnerPreferred'  # Select object ownership type
)

# Print the response (for debugging purposes)
print(response)


'''
Example Output:

(myenv) ubuntu@ip-172-31-86-180:/opt$ python3 tp3.py
{'ResponseMetadata': {'RequestId': '9PYGNVJBW19QKJDX', 'HostId': 'XL8pBR3PC5Cn90xDE3Q2320PhYgu6BBqOBnylHH47fv3Z3schJZYwgga3gbUm3UWLzLUETDy2JU=', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amz-id-2': 'XL8pBR3PC5Cn90xDE3Q2320PhYgu6BBqOBnylHH47fv3Z3schJZYwgga3gbUm3UWLzLUETDy2JU=', 'x-amz-request-id': '9PYGNVJBW19QKJDX', 'date': 'Mon, 09 Dec 2024 11:48:57 GMT', 'location': '/test-abhi-shdgdgjs', 'content-length': '0', 'server': 'AmazonS3'}, 'RetryAttempts': 0}, 'Location': '/test-abhi-shdgdgjs'}

'''