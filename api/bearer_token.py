import requests
import time
from conf import configuration

secrets = configuration.secrets


def request_new_token(token_name):
    try:
        urls = {
            "token_tpp": secrets.tpp_token_info.url,
            "token_send": secrets.token_info.url,
            "token_emd_tpp_test": secrets.emd_tpp_test_token_info.url
        }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        payloads = {
            "token_tpp":  {
                            'client_id': secrets.tpp_token_info.client_id,
                            'client_secret': secrets.tpp_token_info.client_secret,
                            'grant_type': secrets.tpp_token_info.grant_type
            },
            "token_send": {
                            'client_id': secrets.token_info.client_id,
                            'client_secret': secrets.token_info.client_secret,
                            'grant_type': secrets.token_info.grant_type
                            },
            "token_emd_tpp_test": {
                            'client_id': secrets.emd_tpp_test_token_info.client_id,
                            'client_secret': secrets.emd_tpp_test_token_info.client_secret,
                            'grant_type': secrets.emd_tpp_test_token_info.grant_type
                            }
        }

        url = urls.get(token_name)
        payload = payloads.get(token_name)
        response = requests.request("POST", url, headers=headers, data=payload, verify=False)
        if response.status_code == 200:
            response_data = response.json()
            return response_data.get("access_token"), response_data.get("expires_in",1600)
        return None, 0
    except requests.RequestException:
        return None, 0


class TokenManager:
    def __init__(self):
        self.tokens = {
            "token_tpp": {"value": None, "expires_at": 0},
            "token_send": {"value": None, "expires_at": 0},
            "token_emd_tpp_test": {"value": None, "expires_at": 0}
        }

    def get_token(self, token_name):
        if token_name not in self.tokens:
            return None

        token_info = self.tokens[token_name]

        if token_info["value"]and time.time() < token_info["expires_at"]:
            return token_info["value"]

        new_token, expires_in = request_new_token(token_name)

        if new_token:
            token_info["value"] = new_token
            token_info["expires_at"] = time.time() + expires_in
            return new_token
        else:
            return None


token_manager = TokenManager()

def richiesta_con_token(token_name):
    token = token_manager.get_token(token_name)
    return token

def bearer_token():
    return None