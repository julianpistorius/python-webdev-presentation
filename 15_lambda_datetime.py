from datetime import datetime
import json

print('Loading function')


def lambda_handler(event, context):
    print('Received event: ' + json.dumps(event, indent=2))
    return {'current_time': str(datetime.now())}
