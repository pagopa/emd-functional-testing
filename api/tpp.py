import requests
from conf.configuration import settings
from api import bearer_token

class TppAPI:

    def __init__(self):
        self.environment = settings.TARGET_ENV
        self.domain = f'{settings.domain[self.environment]}{settings.endpoints.base_path}{settings.endpoints.tpp.base_path}'
        self.domain_mil = f'{settings.domain_mil[self.environment]}{settings.endpoints.base_path_tpp}{settings.endpoints.base_path}{settings.endpoints.tpp.base_path}'
        self.content_type = 'application/json'

    def save_tpp(self, tpp):
        url = f'{self.domain}/save'
        headers = { 'Content-Type': self.content_type, 'Authorization': f'Bearer {bearer_token.richiesta_con_token("token_tpp")}'}
        return requests.request("POST", url, headers=headers, data=tpp, verify=False)

    def get_tpp_by_entity_id(self, entity_id):
        url = f'{self.domain_mil}/entityId/{entity_id}'
        headers = { 'Content-Type': self.content_type, 'Authorization': f'Bearer {bearer_token.richiesta_con_token("token_tpp")}'}
        return requests.request("GET", url, headers=headers, verify=False)

    def update_tpp(self, tpp):
        url = f'{self.domain}/update'
        headers = {'Content-Type': self.content_type,'Authorization': f'Bearer {bearer_token.richiesta_con_token("token_tpp")}'}
        return requests.request("PUT", url, headers=headers, data=tpp, verify=False)

    def update_status_tpp(self, tpp):
        url = f'{self.domain_mil}'
        headers = {'Content-Type': self.content_type,'Authorization': f'Bearer {bearer_token.richiesta_con_token("token_tpp")}'}
        return requests.request("PUT", url, headers=headers, data=tpp, verify=False)

    def get_tpp_info(self, tpp):
        url = f'{self.domain}/{tpp}'
        headers = {'Content-Type': self.content_type,'Authorization': f'Bearer {bearer_token.richiesta_con_token("token_tpp")}'}
        return requests.request("GET", url, headers=headers, verify=False)

    def delete_tpp(self, tpp):
        url = f'{self.domain_mil}/test/delete/{tpp}'
        headers = {'Content-Type': self.content_type,'Authorization': f'Bearer {bearer_token.richiesta_con_token("token_tpp")}'}
        return requests.request("DELETE", url, headers=headers, verify=False)
