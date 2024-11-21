import boto3
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def update_environment_tags():
    ec2 = boto3.client('ec2')

    # Describe all instances
    instances = ec2.describe_instances()
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            tags = {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])}
            
            # Extract the Name tag
            name_tag = tags.get('Name', '')
            if name_tag:
                # Extract environment from Name tag (assuming the format is applicationname-environment)
                if '-' in name_tag:
                    environment = name_tag.split('-')[-1].strip()
                else:
                    logger.warning(f'Instance {instance_id} has Name tag without expected format: {name_tag}')
                    continue

                logger.info(f'Updating Environment tag for instance {instance_id} to {environment}')

                # Update or add the Environment tag
                ec2.create_tags(
                    Resources=[instance_id],
                    Tags=[{'Key': 'Environment', 'Value': environment}]
                )
                logger.info(f'Environment tag updated for instance {instance_id} to {environment}')
            else:
                logger.warning(f'Instance {instance_id} does not have a Name tag')

if __name__ == '__main__':
    update_environment_tags()
