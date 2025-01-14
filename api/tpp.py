import requests

from api.bearer_token import bearer_token
from conf.configuration import settings


def get_tpp_info(tpp):
    try:
        environment = settings.environment
        domain = settings.domain[environment] + settings.endpoints.base_path
        url = f'{domain}{settings.endpoints.tpp.base_path}/{tpp}'
        print(f'[TPP_API][GET_TPP_INFO] {url}')
        token = bearer_token()
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }

        response = requests.request("GET", url, headers=headers, verify=False)
        print(f'[TPP_API][GET_TPP_INFO] {response}')
        return response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def get_tpp_token_info(tpp):
    try:
        environment = settings.environment
        domain = settings.domain[environment] + settings.endpoints.base_path
        url = f'{domain}{settings.endpoints.tpp.base_path}/{tpp}/token'
        print(f'[TPP_API][GET_TPP_TOKEN_INFO] {url}')
        token = bearer_token()
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }

        response = requests.request("GET", url, headers=headers, verify=False)
        print(f'[TPP_API][GET_TPP_TOKEN_INFO] {response}')
        return response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def save_tpp(tpp):
    try:
        environment = settings.environment
        domain = settings.domain[environment] + settings.endpoints.base_path
        url = f'{domain}{settings.endpoints.tpp.base_path}/save/test'
        print(f'[TPP_API][SAVE] {url}')
        token = bearer_token()
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }
        response = requests.request("POST", url, headers=headers, data=tpp, verify=False)
        print(f'[TPP_API][SAVE] {response}')
        return response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def delete_tpp(tpp):
    try:
        environment = settings.environment
        domain = settings.domain[environment] + settings.endpoints.base_path
        url = f'{domain}{settings.endpoints.tpp.base_path}/delete/test/{tpp}'
        print(f'[TPP_API][DELETE] {url}')
        token = bearer_token()
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }

        response = requests.request("DELETE", url, headers=headers, verify=False)
        print(f'[TPP_API][DELETE] {response}')
        return response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def update_state(tpp):
    try:
        environment = settings.environment
        domain = settings.domain[environment] + settings.endpoints.base_path
        url = f'{domain}{settings.endpoints.tpp.base_path}'
        print(f'[TPP_API][UPDATE_STATE] {url}')
        token = bearer_token()
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }

        response = requests.request("PUT", url, headers=headers, data=tpp, verify=False)
        print(f'[TPP_API][UPDATE_STATE] {response}')
        return response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def update_info(tpp):
    try:
        environment = settings.environment
        domain = settings.domain[environment] + settings.endpoints.base_path
        url = f'{domain}{settings.endpoints.tpp.base_path}/{tpp.tppId}'
        print(f'[TPP_API][UPDATE_INFO] {url}')
        token = bearer_token()
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }

        response = requests.request("PUT", url, headers=headers, data=tpp, verify=False)
        print(f'[TPP_API][UPDATE_INFO] {response}')
        return response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def update_token_info(tpp):
    try:
        environment = settings.environment
        domain = settings.domain[environment] + settings.endpoints.base_path
        url = f'{domain}{settings.endpoints.tpp.base_path}/{tpp.tppId}/token'
        print(f'[TPP_API][UPDATE_TOKEN_INFO] {url}')
        token = bearer_token()
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }

        response = requests.request("PUT", url, headers=headers, data=tpp, verify=False)
        print(f'[TPP_API][UPDATE_TOKEN_INFO] {response}')
        return response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None