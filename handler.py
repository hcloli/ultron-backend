from auth0.v3.authentication.users import Users
import json


def hello(event, context):
    domain = 'fuzeday-ultron.auth0.com'
    u = Users(domain=domain)
    user_info = json.loads(u.userinfo('n66HltzIlr9ekRZSSZupiv-G7TdnikSA'))

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "user_info": user_info,
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
