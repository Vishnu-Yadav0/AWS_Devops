import json
import boto3

def lambda_handler(event, context):
    # Initialize clients
    config = boto3.client('config')
    ec2 = boto3.client('ec2')
    
    # Parse the event
    invoking_event = json.loads(event['invokingEvent'])
    configuration_item = invoking_event['configurationItem']
    resource_id = configuration_item['resourceId']
    resource_type = configuration_item['resourceType']
    
    # Example: Log the tags of the resource
    if resource_type == 'AWS::EC2::Instance':
        tags = configuration_item.get('tags', {})
        print(f'Resource ID: {resource_id}')
        print(f'Tags: {tags}')
        
        # Add custom logic here to handle tag monitoring
        # For example, notify if a specific tag is missing or incorrect
        required_tag_key = 'Environment'
        if required_tag_key not in tags:
            print(f'Tag {required_tag_key} is missing from resource {resource_id}')
            # You can add code to send an alert, update the tag, etc.

    return {
        'statusCode': 200,
        'body': json.dumps('Tag monitoring completed successfully')
    }

if __name__ == '__main__':
    lambda_handler()