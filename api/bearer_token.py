import requests

from config.configuration import settings
from config.configuration import secrets


def bearer_token():
    try:
        data = {
            'client_id': secrets.token_info.mil_client_id,
            'client_secret': secrets.token_info.mil_client_secret,
            'grant_type': secrets.token_info.mil_grant_type
        }

        response = requests.post(
            url=secrets.token_info.mil_token_url,
            data=data,  # Invia i dati nel corpo della richiesta
            timeout=settings.default_timeout,
            verify=False  # TODO: Riabilita verifica SSL prima di andare in ambiente
        )

        if response.status_code == 200:
            response_data = response.json()
            access_token = response_data.get("access_token")

            if access_token:
                print(f"Access Token: {access_token}")
                return access_token
            else:
                print("Access token not found in the response.")
                return None
        else:
            print(f"Error: Received status code {response.status_code}")
            print(f"Response: {response.text}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
