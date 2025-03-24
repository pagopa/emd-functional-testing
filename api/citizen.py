import requests
from conf.configuration import settings
from api.bearer_token import richiesta_con_token

class CitizenAPI:

    def __init__(self):
        self.environment = settings.environment
        self.domain = f'{settings.domain[self.environment]}{settings.endpoints.base_path}{settings.endpoints.citizen.base_path}'
        self.domain_mil = f'{settings.domain_mil[self.environment]}{settings.endpoints.base_path_citizen}{settings.endpoints.base_path}{settings.endpoints.citizen.base_path}'

    def save_consent(self, citizen, tpp):
        url = f'{self.domain}/{citizen}/{tpp}'
        headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {richiesta_con_token("token_send")}'}
        return requests.request("POST", url, headers=headers, verify=False)

    def get_consent(self, citizen, tpp):
        url = f'{self.domain}/{citizen}/{tpp}'
        headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {richiesta_con_token("token_send")}'}
        return requests.request("GET", url, headers=headers, verify=False)


    def switch_state(self, citizen, tpp):
        url = f'{self.domain_mil}/{citizen}/{tpp}'
        headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {richiesta_con_token("token_send")}'}
        return requests.request("PUT", url, headers=headers, verify=False)

    def get_consent(self, citizen, tpp):
        url = f'{self.domain}/{citizen}/{tpp}'
        headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {richiesta_con_token("token_send")}'}
        return requests.request("GET", url, headers=headers, verify=False)

    def get_consent_list(self, citizen):
        url = f'{self.domain_mil}/list/{citizen}'
        headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {richiesta_con_token("token_send")}'}
        return requests.request("GET", url, headers=headers, verify=False)

    def get_consent_list_enabled(self, citizen):
        url = f'{self.domain_mil}/list/{citizen}/enabled'
        headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {richiesta_con_token("token_send")}'}
        return requests.request("GET", url, headers=headers, verify=False)

    def get_citizens_on_tpp(self, tpp):
        url = f'{self.domain}/{tpp}'
        headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {richiesta_con_token("token_send")}'}
        return requests.request("GET", url, headers=headers, verify=False)

    def delete_consents(self, citizen):
        url = f'{self.domain_mil}/test/delete/{citizen}'
        headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {richiesta_con_token("token_send")}'}
        return requests.request("DELETE", url, headers=headers, verify=False)

