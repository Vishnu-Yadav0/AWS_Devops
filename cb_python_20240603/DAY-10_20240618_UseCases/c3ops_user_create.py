import boto3
import json

def lambda_handler(event, context):
    # Initialize the IAM client
    iam_client = boto3.client('iam')

    # Extract the username from the event
    username = event.get('username')
    
    if not username:
        return {
            'statusCode': 400,
            'body': json.dumps('Username parameter is required')
        }

    try:
        # Create a new IAM user
        response = iam_client.create_user(
            UserName=username
        )
        
        # Return the user creation response
        return {
            'statusCode': 200,
            'body': json.dumps(response)
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error creating user: {str(e)}")
        }

