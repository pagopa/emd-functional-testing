import requests

from conf.configuration import secrets

def bearer_token_mil():
    try:

        url = secrets.mil_token_info.mil_token_url

        payload = {
                'client_id': secrets.mil_token_info.mil_client_id,
                'client_secret': secrets.mil_token_info.mil_client_secret,
                'grant_type': secrets.mil_token_info.mil_grant_type
            }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        if response.status_code == 200:
            response_data = response.json()
            access_token = response_data.get("access_token")

            if access_token:
                #print(f"Access Token: {access_token}")
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


def bearer_token():
    try:

        url = secrets.token_info.token_url

        payload = {
                'client_id': secrets.token_info.client_id,
                'client_secret': secrets.token_info.client_secret,
                'grant_type': secrets.token_info.grant_type
            }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("POST", url, headers=headers, data=payload, verify=False)

        if response.status_code == 200:
            response_data = response.json()
            access_token = response_data.get("access_token")

            if access_token:
                #print(f"Access Token: {access_token}")
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
