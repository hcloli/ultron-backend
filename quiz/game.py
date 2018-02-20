import os
import boto3
import json
from boto3.dynamodb.conditions import Key, Attr
from auth0.v3.authentication.users import Users
import uuid

dynamodb = boto3.resource('dynamodb')

def new_quiz(event, context):
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


def get_question(event, context):
    game_id = event['pathParameters']['quiz_id']
    print("Getting questions for game %s" % (game_id))

    quiz = json.load(open("questions/ultron.json"))
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE_SUBMITS'])
    result = table.query(
        IndexName="game_id-index",
        KeyConditionExpression=Key('game_id').eq(game_id)
    )
    print("---------------------")
    asked_questions = map(lambda x: x["question_id"], result["Items"])

    question_to_return = None
    for q in quiz["questions"]:
        if q["id"] not in asked_questions:
            question_to_return = q
            break

    if question_to_return is not None:
        del question_to_return["answer"]

    status = "finished" if question_to_return is None else "in-progress"
    ret = {
        "status": status,
        "question": question_to_return
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(ret)
    }
    return response


def submit_answer(event, context):
    question_id = event['pathParameters']['question_id']
    quiz_id = event['pathParameters']['quiz_id']
    post_body = json.loads(event['body'])
    answer_time = post_body["answerTime"]
    answer = post_body["answer"]

    state_id = str(uuid.uuid4())
    item = {
        "state_id": state_id,
        "game_id": quiz_id,
        "question_id": question_id,
        "answer": answer,
        "answerTime": answer_time
    }

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE_SUBMITS'])
    table.put_item(Item=item)

    response = {
        "statusCode": 200,
        "body": json.dumps({"state": "OK"})
    }
    return response


def get_history(event, context):
    response = {
        "statusCode": 200,
        "body": json.dumps({"state": "OK"})
    }
    return response


def get_result(event, context):
    response = {
        "statusCode": 200,
        "body": json.dumps({"state": "OK"})
    }
    return response
