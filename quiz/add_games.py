import os
import boto3
import json
from auth0.v3.authentication.users import Users
dynamodb = boto3.resource('dynamodb')
import uuid


def create_game(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE_GAMES'])
    post_body = json.loads(event['body'])
    user_id = "some_user"
    x_access_token = event['headers'].get("x-access-token")
    if x_access_token is not None:
        domain = 'fuzeday-ultron.auth0.com'
        u = Users(domain=domain)
        user_info = json.loads(u.userinfo(x_access_token))
        if user_info is not None:
            user_id = user_info['name']

    game_id = uuid.uuid4()
    item = {
        'game_id': str(game_id),
        'user_id': user_id,
        'quiz': post_body['quiz']
    }

    table.put_item(Item=item)

    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response
