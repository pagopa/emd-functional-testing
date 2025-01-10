import requests

from api.bearer_token import bearer_token
from conf.configuration import settings


def get_tpp(tpp):
    try:
        environment = settings.environment
        domain = settings.domain[environment] + settings.endpoints.base_path
        url = f'{domain}{settings.endpoints.tpp.base_path}/{tpp}'
        print(f'[TPP_API][GET_TPP] {url}')
        token = bearer_token()
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }

        response = requests.request("GET", url, headers=headers, verify=False)
        print(f'[TPP_API][GET_TPP] {response}')
        return response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
