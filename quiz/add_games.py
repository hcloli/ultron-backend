import os
import boto3
import json
dynamodb = boto3.resource('dynamodb')


def create_game(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE_GAMES'])

    item = {
        'game_id': '1',
        'user_id': '1',
        'type': 'interview'
    }

    table.put_item(Item=item)

    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response
