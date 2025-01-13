import requests
from api.bearer_token import bearer_token
from conf.configuration import settings


def build_url(*paths):
    """Constructs a complete URL based on environment and given path components."""
    environment = settings.environment
    domain = settings.domain[environment] + settings.endpoints.base_path
    return f"{domain}{'/'.join(paths)}"


def make_request(method, url, token, headers=None):
    """Makes an HTTP request with the specified method, URL, and headers."""
    if headers is None:
        headers = {}
    headers.update({
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    })
    try:
        response = requests.request(method, url, headers=headers, verify=False)
        print(f"[CITIZEN_API][{method}] {response}")
        return response
    except requests.exceptions.RequestException as e:
        print(f"[CITIZEN_API][{method}] An error occurred: {e}")
        return None


def save_consent(citizen, tpp):
    url = build_url(settings.endpoints.citizen.base_path, citizen, tpp)
    print(f"[CITIZEN_API][SAVE_CONSENT] {url}")
    token = bearer_token()
    return make_request("POST", url, token)


def get_consent(citizen, tpp):
    url = build_url(settings.endpoints.citizen.base_path, citizen, tpp)
    print(f"[CITIZEN_API][GET_CONSENT] {url}")
    token = bearer_token()
    return make_request("GET", url, token)


def switch_state(citizen, tpp):
    url = build_url(settings.endpoints.citizen.base_path, citizen, tpp)
    print(f"[CITIZEN_API][SWITCH_STATE] {url}")
    token = bearer_token()
    return make_request("PUT", url, token)


def get_consent_list(citizen):
    url = build_url(settings.endpoints.citizen.base_path, "list", citizen)
    print(f"[CITIZEN_API][GET_CONSENT_LIST] {url}")
    token = bearer_token()
    return make_request("GET", url, token)


def get_consent_list_enabled(citizen):
    url = build_url(settings.endpoints.citizen.base_path, "list", citizen, "enabled")
    print(f"[CITIZEN_API][GET_CONSENT_LIST_ENABLED] {url}")
    token = bearer_token()
    return make_request("GET", url, token)


def get_citizens_on_tpp(tpp):
    url = build_url(settings.endpoints.citizen.base_path, tpp)
    print(f"[CITIZEN_API][GET_CITIZENS_ON_TPP] {url}")
    token = bearer_token()
    return make_request("GET", url, token)


def delete_consents(citizen):
    url = build_url(settings.endpoints.citizen.base_path, "test", citizen)
    print(f"[CITIZEN_API][GET_CITIZENS_ON_TPP] {url}")
    token = bearer_token()
    return make_request("DELETE", url, token)
