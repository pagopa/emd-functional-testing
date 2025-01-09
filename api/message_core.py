import requests
import json

from conf.configuration import settings
from api.bearer_token import bearer_token

def send_messge(payload):
    environment = settings.environment
    domain = settings.domain[environment] + settings.endpoints.base_path
    url = f'{domain}{settings.endpoints.message_core.base_path}{settings.endpoints.message_core.send.base_path}'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {bearer_token()}'
    }

    return requests.request(settings.endpoints.message_core.operations.send.method, url, headers=headers, data=payload)



