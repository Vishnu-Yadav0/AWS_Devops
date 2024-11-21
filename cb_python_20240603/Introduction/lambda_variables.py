import json

def lambda_handler(event, context):
    # Assigning values to variables
    a = 10
    b = "Hello"
    c = 3.14
    
    # Reassigning different types to the same variable
    a = "Python"
    
    # Return the results
    return {
        'statusCode': 200,
        'body': json.dumps({
            'a': a,
            'b': b,
            'c': c
        })
    }


'''
Response
{
  "statusCode": 200,
  "body": "{\"a\": \"Python\", \"b\": \"Hello\", \"c\": 3.14}"
}
'''