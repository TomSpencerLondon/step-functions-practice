response = 1
# print(f"{{\"executionArn\": {response}}}");
f"{{\"executionArn\": \"{response['executionArn']}\" }}"
#
# {"version": "2.0", "routeKey": "GET /executionStatus", "rawPath": "/executionStatus",
#  "rawQueryString": "executionArn=123",
#  "headers": {"accept": "*/*", "accept-encoding": "gzip, deflate, br", "content-length": "2",
#              "content-type": "application/json", "host": "r0yq9rcnu0.execute-api.eu-west-1.amazonaws.com",
#              "postman-token": "bbd01e21-5805-486b-8a24-d412d4d3abeb", "user-agent": "PostmanRuntime/7.28.4",
#              "x-amzn-trace-id": "Root=1-6181a2de-2521fe521ffc39d42beb8f03", "x-forwarded-for": "2.30.14.65",
#              "x-forwarded-port": "443", "x-forwarded-proto": "https"},
#  "queryStringParameters": {"executionArn": "123"},
#  "requestContext": {"accountId": "706054169063", "apiId": "r0yq9rcnu0",
#                     "domainName": "r0yq9rcnu0.execute-api.eu-west-1.amazonaws.com", "domainPrefix": "r0yq9rcnu0",
#                     "http": {"method": "GET", "path": "/executionStatus", "protocol": "HTTP/1.1",
#                              "sourceIp": "2.30.14.65", "userAgent": "PostmanRuntime/7.28.4"},
#                     "requestId": "IMZiuidYjoEEJxA=", "routeKey": "GET /executionStatus", "stage": "$default",
#                     "time": "02/Nov/2021:20:43:10 +0000", "timeEpoch": 1635885790039}, "body": "{}",
#  "isBase64Encoded": false}
