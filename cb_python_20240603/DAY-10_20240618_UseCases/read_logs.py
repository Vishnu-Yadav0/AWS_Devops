import boto3
import datetime
from datetime import datetime, timezone

client = boto3.client('cloudtrail')

end_time = datetime.now(timezone.utc)

start_time_epoch = end_time.timestamp() - (7 * 24 * 60 * 60)

print(end_time)

print(start_time_epoch)

# Convert the start time from epoch to datetime
start_time = datetime.fromtimestamp(start_time_epoch, tz=timezone.utc)

print(start_time)


# Function to print events related to S3 service
def print_s3_events(start_time, end_time):
    try:
        # Paginate through the events
        paginator = client.get_paginator('lookup_events')
        response_iterator = paginator.paginate(
            StartTime=start_time,
            EndTime=end_time,
            LookupAttributes=[
                {
                    'AttributeKey': 'EventSource',
                    'AttributeValue': 's3.amazonaws.com'
                }
            ]
        )
        
        # Iterate over the pages of events
        for page in response_iterator:
            for event in page['Events']:
                print(f"Event ID: {event['EventId']}")
                print(f"Event Name: {event['EventName']}")
                print(f"Event Time: {event['EventTime']}")
                print(f"User: {event['Username']}")
                print(f"Request Parameters: {event['CloudTrailEvent']}")
                print("-" * 60)
    
    except Exception as e:
        print(f"Error retrieving S3 events: {str(e)}")

# Call the function
print_s3_events(start_time, end_time)