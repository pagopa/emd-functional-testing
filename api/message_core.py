import requests
from conf.configuration import settings
from api.bearer_token import richiesta_con_token

class MessageCoreAPI:

    def __init__(self):
        self.environment = settings.environment
        self.domain = f'{settings.domain[self.environment]}{settings.endpoints.base_path}{settings.endpoints.message_core.base_path}'


    def send_message(self, payload):
        url = f'{self.domain}/{settings.endpoints.message_core.operations.send.endpoint}'
        headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {richiesta_con_token("token_send")}'}
        return  requests.request("POST", url, headers=headers, data=payload, verify=False)
