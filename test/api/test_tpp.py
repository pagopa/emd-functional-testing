from unittest.mock import patch, MagicMock
from types import SimpleNamespace

from api.tpp import TppAPI


@patch('api.tpp.settings')
@patch('api.bearer_token.richiesta_con_token')
@patch('api.tpp.requests.request')
def test_save_consent(mock_requests, mock_richiesta_con_token, mock_settings):
    mock_settings.TARGET_ENV = 'dev'
    mock_settings.domain = {'dev': 'https://test.test'}
    mock_settings.domain_mil = {'dev': 'https://test.test'}
    mock_settings.endpoints = SimpleNamespace(
        base_path='/api/v1',
        base_path_citizen='/m',
        base_path_tpp='/m',
        tpp=SimpleNamespace(base_path='/tpp',base_path_tpp='/m',)
    )

    mock_richiesta_con_token.return_value = 'mocked-token'

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_requests.return_value = mock_response

    api = TppAPI()
    response = api.save_tpp({})

    mock_richiesta_con_token.assert_called_once_with("token_tpp")
    mock_requests.assert_called_once()
    assert response.status_code == 200


@patch('api.tpp.settings')
@patch('api.bearer_token.richiesta_con_token')
@patch('api.tpp.requests.request')
def test_get_tpp_by_entity_id(mock_requests, mock_richiesta_con_token, mock_settings):
    mock_settings.TARGET_ENV = 'dev'
    mock_settings.domain = {'dev': 'https://test.test'}
    mock_settings.domain_mil = {'dev': 'https://test.test'}
    mock_settings.endpoints = SimpleNamespace(
        base_path='/api/v1',
        base_path_citizen='/m',
        base_path_tpp='/m',
        tpp=SimpleNamespace(base_path='/tpp',base_path_tpp='/m',)
    )

    mock_richiesta_con_token.return_value = 'mocked-token'

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_requests.return_value = mock_response

    api = TppAPI()
    response = api.get_tpp_by_entity_id("entity")

    mock_richiesta_con_token.assert_called_once_with("token_tpp")
    mock_requests.assert_called_once()
    assert response.status_code == 200


@patch('api.tpp.settings')
@patch('api.bearer_token.richiesta_con_token')
@patch('api.tpp.requests.request')
def test_update_tpp(mock_requests, mock_richiesta_con_token, mock_settings):
    mock_settings.TARGET_ENV = 'dev'
    mock_settings.domain = {'dev': 'https://test.test'}
    mock_settings.domain_mil = {'dev': 'https://test.test'}
    mock_settings.endpoints = SimpleNamespace(
        base_path='/api/v1',
        base_path_citizen='/m',
        base_path_tpp='/m',
        tpp=SimpleNamespace(base_path='/tpp',base_path_tpp='/m',)
    )

    mock_richiesta_con_token.return_value = 'mocked-token'

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_requests.return_value = mock_response

    api = TppAPI()
    response = api.update_tpp({})

    mock_richiesta_con_token.assert_called_once_with("token_tpp")
    mock_requests.assert_called_once()
    assert response.status_code == 200


@patch('api.tpp.settings')
@patch('api.bearer_token.richiesta_con_token')
@patch('api.tpp.requests.request')
def test_update_status_tpp(mock_requests, mock_richiesta_con_token, mock_settings):
    mock_settings.TARGET_ENV = 'dev'
    mock_settings.domain = {'dev': 'https://test.test'}
    mock_settings.domain_mil = {'dev': 'https://test.test'}
    mock_settings.endpoints = SimpleNamespace(
        base_path='/api/v1',
        base_path_citizen='/m',
        base_path_tpp='/m',
        tpp=SimpleNamespace(base_path='/tpp',base_path_tpp='/m',)
    )

    mock_richiesta_con_token.return_value = 'mocked-token'

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_requests.return_value = mock_response

    api = TppAPI()
    response = api.update_status_tpp({})

    mock_richiesta_con_token.assert_called_once_with("token_tpp")
    mock_requests.assert_called_once()
    assert response.status_code == 200


@patch('api.tpp.settings')
@patch('api.bearer_token.richiesta_con_token')
@patch('api.tpp.requests.request')
def test_get_tpp_info(mock_requests, mock_richiesta_con_token, mock_settings):
    mock_settings.TARGET_ENV = 'dev'
    mock_settings.domain = {'dev': 'https://test.test'}
    mock_settings.domain_mil = {'dev': 'https://test.test'}
    mock_settings.endpoints = SimpleNamespace(
        base_path='/api/v1',
        base_path_citizen='/m',
        base_path_tpp='/m',
        tpp=SimpleNamespace(base_path='/tpp',base_path_tpp='/m',)
    )

    mock_richiesta_con_token.return_value = 'mocked-token'

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_requests.return_value = mock_response

    api = TppAPI()
    response = api.get_tpp_info("tpp")

    mock_richiesta_con_token.assert_called_once_with("token_tpp")
    mock_requests.assert_called_once()
    assert response.status_code == 200


@patch('api.tpp.settings')
@patch('api.bearer_token.richiesta_con_token')
@patch('api.tpp.requests.request')
def test_delete_tpp(mock_requests, mock_richiesta_con_token, mock_settings):
    mock_settings.TARGET_ENV = 'dev'
    mock_settings.domain = {'dev': 'https://test.test'}
    mock_settings.domain_mil = {'dev': 'https://test.test'}
    mock_settings.endpoints = SimpleNamespace(
        base_path='/api/v1',
        base_path_citizen='/m',
        base_path_tpp='/m',
        tpp=SimpleNamespace(base_path='/tpp',base_path_tpp='/m',)
    )

    mock_richiesta_con_token.return_value = 'mocked-token'

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_requests.return_value = mock_response

    api = TppAPI()
    response = api.delete_tpp({})

    mock_richiesta_con_token.assert_called_once_with("token_tpp")
    mock_requests.assert_called_once()
    assert response.status_code == 200
