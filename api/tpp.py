import requests
from conf.configuration import settings
from api.bearer_token import richiesta_con_token

class TppAPI:

    def __init__(self):
        self.environment = settings.environment
        self.domain = f'{settings.domain[self.environment]}{settings.endpoints.base_path}{settings.endpoints.tpp.base_path}'
        self.domain_mil = f'{settings.domain_mil[self.environment]}{settings.endpoints.base_path_tpp}{settings.endpoints.base_path}{settings.endpoints.tpp.base_path}'

    def save_tpp(self, tpp):
        url = f'{self.domain}/save'
        headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {richiesta_con_token("token_send")}'}
        return requests.request("POST", url, headers=headers, data=tpp, verify=False)

    def get_tpp_by_entity_id(self, entity_id):
        url = f'{self.domain_mil}/entityId/{entity_id}'
        headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {richiesta_con_token("token_send")}'}
        return requests.request("GET", url, headers=headers, verify=False)

    def update_tpp(self, tpp):
        url = f'{self.domain}/update'
        headers = {'Content-Type': 'application/json','Authorization': f'Bearer {richiesta_con_token("token_send")}'}
        return requests.request("PUT", url, headers=headers, data=tpp, verify=False)

    def update_status_tpp(self, tpp):
        url = f'{self.domain_mil}'
        headers = {'Content-Type': 'application/json','Authorization': f'Bearer {richiesta_con_token("token_send")}'}
        return requests.request("PUT", url, headers=headers, data=tpp, verify=False)

    def get_tpp_info(self, tpp):
        url = f'{self.domain}/{tpp}'
        headers = {'Content-Type': 'application/json','Authorization': f'Bearer {richiesta_con_token("token_send")}'}
        return requests.request("GET", url, headers=headers, verify=False)

    def delete_tpp(self, tpp):
        url = f'{self.domain}/delete/{tpp}'
        url = f'http://10.11.0.106:8080/emd/tpp/test/delete/{tpp}'
        headers = {'Content-Type': 'application/json','Authorization': f'Bearer {richiesta_con_token("token_send")}'}
        return requests.request("DELETE", url, headers=headers, verify=False)
