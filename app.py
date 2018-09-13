import json
import base64
import logging


def lambda_handler(event, context):
    log = logging.getLogger(__name__)
    logging.getLogger().setLevel('INFO')

    try:
        auth_header_value = {v for k, v in event['headers'].items() if k.lower() == 'authorization'}.pop()
        base64_username_password = auth_header_value.split()[1]
        username_password = base64.standard_b64decode(base64_username_password).decode('utf8')
        password = username_password.split(':')[1]
        return {
            "statusCode": 200,
            "body": json.dumps({"secret": password})
        }
    except Exception as e:
        log.error("Error", e)
        return {
            "statusCode": 401,
        }
