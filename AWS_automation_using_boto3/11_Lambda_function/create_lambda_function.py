import boto3
import json
import time

# Initialize the boto3 Lambda client
lambda_client = boto3.client('lambda')
iam_client = boto3.client('iam')

def get_user_input():
    # Default values for each parameter
    default_zip_file_path = 'lambda_code.zip'
    default_function_name = 'HelloWorldLambda'
    default_runtime = 'python3.8'
    default_handler = 'lambda_function.lambda_handler'
    default_timeout = 15
    default_memory_size = 128

    # Prompt the user for each parameter
    zip_file_path = input(f"Enter the path to your zip file (default {default_zip_file_path}): ").strip() or default_zip_file_path
    function_name = input(f"Enter the Lambda function name (default {default_function_name}): ").strip() or default_function_name
    runtime = input(f"Enter the runtime (default {default_runtime}): ").strip() or default_runtime
    handler = input(f"Enter the handler (default {default_handler}): ").strip() or default_handler
    timeout = input(f"Enter the timeout in seconds (default {default_timeout}): ").strip() or default_timeout
    memory_size = input(f"Enter the memory size in MB (default {default_memory_size}): ").strip() or default_memory_size

    # Convert timeout and memory_size to integers
    timeout = int(timeout)
    memory_size = int(memory_size)

    return zip_file_path, function_name, runtime, handler, timeout, memory_size

def create_lambda_execution_role():
    # Create the execution role with the correct trust policy
    assume_role_policy_document = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "lambda.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }

    role_name = "LambdaExecutionRole"
    
    try:
        # Create the IAM role with the correct trust relationship
        role = iam_client.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=json.dumps(assume_role_policy_document),
            Description="Role for Lambda function execution"
        )
        print(f"Role {role_name} created successfully.")

        # Attach the basic Lambda execution policy to the role
        iam_client.attach_role_policy(
            RoleName=role_name,
            PolicyArn="arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
        )
        print(f"Policy AWSLambdaBasicExecutionRole attached to {role_name}.")
        
        return role['Role']['Arn']
    except Exception as e:
        print(f"Error creating or configuring the IAM role: {e}")
        raise

def create_lambda_function_with_retries(zip_file_path, function_name, runtime, role_arn, handler, timeout, memory_size, retries=3, delay=10):
    """Creates the Lambda function with retries if an InvalidParameterValueException occurs."""
    params = {
        'FunctionName': function_name,
        'Runtime': runtime,
        'Role': role_arn,
        'Handler': handler,
        'Code': {
            'ZipFile': open(zip_file_path, 'rb').read()
        },
        'Timeout': timeout,
        'MemorySize': memory_size
    }

    for attempt in range(1, retries + 1):
        try:
            # Try creating the Lambda function
            response = lambda_client.create_function(**params)
            return response['FunctionArn'], response['FunctionName']
        except lambda_client.exceptions.InvalidParameterValueException as e:
            print(f"Error: {e}. Attempt {attempt} of {retries}. Retrying in {delay} seconds...")
            if attempt < retries:
                time.sleep(delay)
            else:
                print("Maximum retry attempts reached. Aborting Lambda creation.")
                raise

def wait_for_lambda_function_to_be_active(function_name, retries=3, delay=10):
    """Waits for the Lambda function to be in 'Active' state before invoking."""
    for attempt in range(1, retries + 1):
        try:
            # Get the function's state
            response = lambda_client.get_function(FunctionName=function_name)
            status = response['Configuration']['State']
            
            if status == 'Active':
                print(f"Lambda function {function_name} is now active.")
                return True
            else:
                print(f"Lambda function is still {status}. Retrying in {delay} seconds...")
                time.sleep(delay)
        except Exception as e:
            print(f"Error checking function status: {e}")
            if attempt < retries:
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                print("Maximum retries reached. Aborting.")
                raise

    return False

def invoke_lambda_function(function_name):
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType='RequestResponse'  # 'RequestResponse' for synchronous invocation
    )

    return response['Payload'].read().decode('utf-8')

if __name__ == "__main__":
    # Get user inputs for Lambda function creation
    zip_file_path, function_name, runtime, handler, timeout, memory_size = get_user_input()

    # Create the execution role for Lambda
    role_arn = create_lambda_execution_role()

    # Create Lambda function with retries if needed
    lambda_function_arn, lambda_function_name = create_lambda_function_with_retries(zip_file_path, function_name, runtime, role_arn, handler, timeout, memory_size)

    # Print the ARNs and relevant information
    print(f"Lambda Function ARN: {lambda_function_arn}")
    print(f"Lambda Function Name: {lambda_function_name}")
    print(f"Lambda Execution Role ARN: {role_arn}")

    # Wait for the Lambda function to become active
    if wait_for_lambda_function_to_be_active(lambda_function_name):
        # Optionally, invoke the function and print the result
        response = invoke_lambda_function(lambda_function_name)
        print("Lambda Response:", response)
    else:
        print("Lambda function did not become active in the expected time.")


'''
Example Output:

ubuntu@ip-172-31-86-180:/opt/lambda$ python3 create_lambda.py
Enter the path to your zip file (default lambda_code.zip):
Enter the Lambda function name (default HelloWorldLambda):
Enter the runtime (default python3.8):
Enter the handler (default lambda_function.lambda_handler):
Enter the timeout in seconds (default 15):
Enter the memory size in MB (default 128):
Role LambdaExecutionRole created successfully.
Policy AWSLambdaBasicExecutionRole attached to LambdaExecutionRole.
Error: An error occurred (InvalidParameterValueException) when calling the CreateFunction operation: The role defined for the function cannot be assumed by Lambda.. Attempt 1 of 3. Retrying in 10 seconds...
Lambda Function ARN: arn:aws:lambda:us-east-1:010526261743:function:HelloWorldLambda
Lambda Function Name: HelloWorldLambda
Lambda Execution Role ARN: arn:aws:iam::010526261743:role/LambdaExecutionRole
Lambda function is still Pending. Retrying in 10 seconds...
Lambda function HelloWorldLambda is now active.
Lambda Response: {"statusCode": 200, "body": "\"Hello, World!\""}
ubuntu@ip-172-31-86-180:/opt/lambda$

For more detailed output, please refer to screenshots in /AWS automation using boto3/readme.md
'''