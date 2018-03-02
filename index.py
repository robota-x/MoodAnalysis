import json
import datetime
import boto3

def handler(event, context):
    votes_table = boto3.resource('dynamodb').Table(os.getenv('TABLE_NAME'))

    data = {
        'output': 'Hello World',
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'secret': votes_table.scan()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
