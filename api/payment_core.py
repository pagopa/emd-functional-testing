import requests
from conf.configuration import settings
from api import bearer_token

class PaymentCoreAPI:

    def __init__(self):
        self.environment = settings.TARGET_ENV
        self.domain = f'{settings.domain[self.environment]}{settings.endpoints.base_path}{settings.endpoints.payment_core.base_path}'
        self.content_type = 'application/json'

    def retrieval_tokens(self, payload, tpp_name):
        url = f'{self.domain}/retrievalTokens'
        headers = { 'Content-Type': self.content_type, 'Authorization': f'Bearer {bearer_token.richiesta_con_token(tpp_name)}'}
        return requests.request("POST", url, headers=headers, data=payload, verify=False)


    def get_token(self, retrieval_id):
        url = f'{self.domain}/retrievalTokens/{retrieval_id}'
        headers = { 'Content-Type': self.content_type, 'Authorization': f'Bearer {bearer_token.richiesta_con_token("token_send")}'}
        return requests.request("GET", url, headers=headers, verify=False)

    def generate_deep_link(self, params):
        url = f'{self.domain}/retrievalTokens/{settings.endpoints.payment_core.operations.generateDeepLink.endpoint}'
        headers = {'Content-Type': self.content_type, 'Authorization': f'Bearer {bearer_token.richiesta_con_token("token_send")}'}
        return requests.request("GET", url, headers=headers, params=params, verify=False)