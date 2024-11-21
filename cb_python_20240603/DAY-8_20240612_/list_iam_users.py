import boto3

def list_iam_users():
    # Create an IAM client
    iam_client = boto3.client('iam')
    
    # Initialize a list to store user names
    users = []
    
    # Paginate through the IAM users
    paginator = iam_client.get_paginator('list_users')
    
    for page in paginator.paginate():
        for user in page['Users']:
            users.append(user['UserName'])
    
    return users

# Call the function and print the IAM users
iam_users = list_iam_users()

print("IAM Users:")
for user in iam_users:
    print(user)

