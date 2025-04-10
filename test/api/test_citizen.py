from unittest.mock import patch, MagicMock
from types import SimpleNamespace

from api.citizen import CitizenAPI


@patch('api.citizen.settings')
@patch('api.bearer_token.richiesta_con_token')
@patch('api.citizen.requests.request')
def test_save_consent(mock_requests, mock_richiesta_con_token, mock_settings):
    mock_settings.TARGET_ENV = 'dev'
    mock_settings.domain = {'dev': 'https://test.test'}
    mock_settings.domain_mil = {'dev': 'https://test.test'}
    mock_settings.endpoints = SimpleNamespace(
        base_path='/api/v1',
        base_path_citizen='/m',
        citizen=SimpleNamespace(base_path='/citizen')
    )

    mock_richiesta_con_token.return_value = 'mocked-token'

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_requests.return_value = mock_response

    api = CitizenAPI()
    response = api.save_consent('fiscalcode123', 'tpp456')

    mock_richiesta_con_token.assert_called_once_with("token_send")
    mock_requests.assert_called_once()
    assert response.status_code == 200

@patch('api.citizen.settings')
@patch('api.bearer_token.richiesta_con_token')
@patch('api.citizen.requests.request')
def test_get_consent(mock_requests, mock_richiesta_con_token, mock_settings):
    mock_settings.TARGET_ENV = 'dev'
    mock_settings.domain = {'dev': 'https://test.test'}
    mock_settings.domain_mil = {'dev': 'https://test.test'}
    mock_settings.endpoints = SimpleNamespace(
        base_path='/api/v1',
        base_path_citizen='/m',
        citizen=SimpleNamespace(base_path='/citizen')
    )

    mock_richiesta_con_token.return_value = 'mocked-token'

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_requests.return_value = mock_response

    api = CitizenAPI()
    response = api.get_consent('fiscalcode123', 'tpp456')

    mock_richiesta_con_token.assert_called_once_with("token_send")
    mock_requests.assert_called_once()
    assert response.status_code == 200

@patch('api.citizen.settings')
@patch('api.bearer_token.richiesta_con_token')
@patch('api.citizen.requests.request')
def test_switch_state(mock_requests, mock_richiesta_con_token, mock_settings):
    mock_settings.TARGET_ENV = 'dev'
    mock_settings.domain = {'dev': 'https://test.test'}
    mock_settings.domain_mil = {'dev': 'https://test.test'}
    mock_settings.endpoints = SimpleNamespace(
        base_path='/api/v1',
        base_path_citizen='/m',
        citizen=SimpleNamespace(base_path='/citizen')
    )

    mock_richiesta_con_token.return_value = 'mocked-token'

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_requests.return_value = mock_response

    api = CitizenAPI()
    response = api.switch_state('fiscalcode123', 'tpp456')

    mock_richiesta_con_token.assert_called_once_with("token_send")
    mock_requests.assert_called_once()
    assert response.status_code == 200


@patch('api.citizen.settings')
@patch('api.bearer_token.richiesta_con_token')
@patch('api.citizen.requests.request')
def test_get_consent_list(mock_requests, mock_richiesta_con_token, mock_settings):
    mock_settings.TARGET_ENV = 'dev'
    mock_settings.domain = {'dev': 'https://test.test'}
    mock_settings.domain_mil = {'dev': 'https://test.test'}
    mock_settings.endpoints = SimpleNamespace(
        base_path='/api/v1',
        base_path_citizen='/m',
        citizen=SimpleNamespace(base_path='/citizen')
    )

    mock_richiesta_con_token.return_value = 'mocked-token'

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_requests.return_value = mock_response

    api = CitizenAPI()
    response = api.get_consent_list('fiscalcode123')

    mock_richiesta_con_token.assert_called_once_with("token_send")
    mock_requests.assert_called_once()
    assert response.status_code == 200



@patch('api.citizen.settings')
@patch('api.bearer_token.richiesta_con_token')
@patch('api.citizen.requests.request')
def test_get_consent_list_enabled(mock_requests, mock_richiesta_con_token, mock_settings):
    mock_settings.TARGET_ENV = 'dev'
    mock_settings.domain = {'dev': 'https://test.test'}
    mock_settings.domain_mil = {'dev': 'https://test.test'}
    mock_settings.endpoints = SimpleNamespace(
        base_path='/api/v1',
        base_path_citizen='/m',
        citizen=SimpleNamespace(base_path='/citizen')
    )

    mock_richiesta_con_token.return_value = 'mocked-token'

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_requests.return_value = mock_response

    api = CitizenAPI()
    response = api.get_consent_list_enabled('fiscalcode123')

    mock_richiesta_con_token.assert_called_once_with("token_send")
    mock_requests.assert_called_once()
    assert response.status_code == 200


@patch('api.citizen.settings')
@patch('api.bearer_token.richiesta_con_token')
@patch('api.citizen.requests.request')
def test_get_citizens_on_tpp(mock_requests, mock_richiesta_con_token, mock_settings):
    mock_settings.TARGET_ENV = 'dev'
    mock_settings.domain = {'dev': 'https://test.test'}
    mock_settings.domain_mil = {'dev': 'https://test.test'}
    mock_settings.endpoints = SimpleNamespace(
        base_path='/api/v1',
        base_path_citizen='/m',
        citizen=SimpleNamespace(base_path='/citizen')
    )

    mock_richiesta_con_token.return_value = 'mocked-token'

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_requests.return_value = mock_response

    api = CitizenAPI()
    response = api.get_citizens_on_tpp('tpp')

    mock_richiesta_con_token.assert_called_once_with("token_send")
    mock_requests.assert_called_once()
    assert response.status_code == 200


@patch('api.citizen.settings')
@patch('api.bearer_token.richiesta_con_token')
@patch('api.citizen.requests.request')
def test_delete_consents(mock_requests, mock_richiesta_con_token, mock_settings):
    mock_settings.TARGET_ENV = 'dev'
    mock_settings.domain = {'dev': 'https://test.test'}
    mock_settings.domain_mil = {'dev': 'https://test.test'}
    mock_settings.endpoints = SimpleNamespace(
        base_path='/api/v1',
        base_path_citizen='/m',
        citizen=SimpleNamespace(base_path='/citizen')
    )

    mock_richiesta_con_token.return_value = 'mocked-token'

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_requests.return_value = mock_response

    api = CitizenAPI()
    response = api.delete_consents('citizen')

    mock_richiesta_con_token.assert_called_once_with("token_send")
    mock_requests.assert_called_once()
    assert response.status_code == 200