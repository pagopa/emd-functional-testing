import requests

from api.bearer_token import bearer_token
from conf.configuration import settings




def send_messge(payload):
    try:
        environment = settings.environment
        domain = settings.domain[environment] + settings.endpoints.base_path
        url = f'{domain}{settings.endpoints.message_core.base_path}{settings.endpoints.message_core.operations.send.endpoint}'
        token = bearer_token()
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }

        response = requests.request("POST", url, headers=headers, data=payload, verify=False)
        print(response)
        return response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

