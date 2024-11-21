import boto3
import json

def list_iam_entities():
    iam_client = boto3.client('iam')
    
    # Fetching IAM Users
    users = iam_client.list_users()
    user_list = users['Users']
    
    # Fetching IAM Roles
    roles = iam_client.list_roles()
    role_list = roles['Roles']
    
    # Fetching IAM Policies
    policies = iam_client.list_policies(Scope='Local')
    policy_list = policies['Policies']
    
    return user_list, role_list, policy_list

def generate_html(users, roles, policies):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AWS IAM Summary</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            h1 { color: #333; }
            h2 { color: #555; }
            ul { list-style-type: none; }
            li { margin-bottom: 10px; }
            .section { margin-bottom: 20px; }
        </style>
    </head>
    <body>
        <h1>AWS IAM Summary</h1>
        <div class="section">
            <h2>IAM Users</h2>
            <ul>
    """
    
    # Add IAM users to HTML
    for user in users:
        html_content += f"<li>{user['UserName']} (Created on: {user['CreateDate']})</li>"
    
    html_content += """
            </ul>
        </div>
        <div class="section">
            <h2>IAM Roles</h2>
            <ul>
    """
    
    # Add IAM roles to HTML
    for role in roles:
        html_content += f"<li>{role['RoleName']} (ARN: {role['Arn']})</li>"
    
    html_content += """
            </ul>
        </div>
        <div class="section">
            <h2>IAM Policies</h2>
            <ul>
    """
    
    # Add IAM policies to HTML
    for policy in policies:
        html_content += f"<li>{policy['PolicyName']} (ARN: {policy['Arn']})</li>"
    
    html_content += """
            </ul>
        </div>
    </body>
    </html>
    """
    
    return html_content

def lambda_handler(event, context):
    # Get IAM data
    users, roles, policies = list_iam_entities()
    
    # Generate HTML content
    html_page = generate_html(users, roles, policies)
    
    # Return the HTML content
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html',
        },
        'body': html_page
    }


if __name__ == "__main__":
    users, roles, policies = list_iam_entities()
    html_page = generate_html(users, roles, policies)
    with open("iam_summary.html", "w") as file:
        file.write(html_page)
    print("HTML page generated successfully: iam_summary.html")
