result = {
    "Count": 2,
    "Items": [
        {
            "state_id": "111",
            "question_id": "1.1",
            "game_id": "haim"
        },
        {
            "state_id": "111.2",
            "question_id": "1.2",
            "game_id": "haim"
        }
    ],
    "ScannedCount": 2,
    "ResponseMetadata": {
        "RetryAttempts": 0,
        "HTTPStatusCode": 200,
        "RequestId": "9TUFCLOD3BC8OCRC65G5EROM6NVV4KQNSO5AEMVJF66Q9ASUAAJG",
        "HTTPHeaders": {
            "x-amzn-requestid": "9TUFCLOD3BC8OCRC65G5EROM6NVV4KQNSO5AEMVJF66Q9ASUAAJG",
            "content-length": "188",
            "server": "Server",
            "connection": "keep-alive",
            "x-amz-crc32": "4107467769",
            "date": "Tue, 20 Feb 2018 15:14:31 GMT",
            "content-type": "application/x-amz-json-1.0"
        }
    }
}

my_list = map(lambda x: x["question_id"], result["Items"])
print(my_list)
print("1.1" in my_list)

momo = {"asda":"asddsa"}
status = "finished" if momo is None else "in-progress"
print(status)