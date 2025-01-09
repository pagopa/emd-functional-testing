import requests

from api.bearer_token import bearer_token
from conf.configuration import settings

def save_consent(citizen,tpp):
    try:
        environment = settings.environment
        domain = settings.domain[environment] + settings.endpoints.base_path
        url = f'{domain}{settings.endpoints.citizen.base_path}/{citizen}/{tpp}'
        token = bearer_token()
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }

        response = requests.request("POST", url, headers=headers, verify=False)
        print(response)
        return response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def get_consent(citizen,tpp):
    try:
        environment = settings.environment
        domain = settings.domain[environment] + settings.endpoints.base_path
        url = f'{domain}{settings.endpoints.citizen.base_path}/{citizen}/{tpp}'
        token = bearer_token()
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }

        response = requests.request("GET", url, headers=headers, verify=False)
        print(response)
        return response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def swithc_state(citizen, tpp):
        try:
            environment = settings.environment
            domain = settings.domain[environment] + settings.endpoints.base_path
            url = f'{domain}{settings.endpoints.citizen.base_path}/{citizen}/{tpp}'
            token = bearer_token()
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {token}'
            }

            response = requests.request("PUT", url, headers=headers, verify=False)
            print(response)
            return response
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

