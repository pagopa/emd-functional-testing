from unittest.mock import patch, MagicMock
from types import SimpleNamespace

from api.message_core import MessageCoreAPI


@patch('api.citizen.settings')
@patch('api.bearer_token.richiesta_con_token')
@patch('api.citizen.requests.request')
def test_save_consent(mock_requests, mock_richiesta_con_token, mock_settings):
    mock_settings.TARGET_ENV = 'dev'
    mock_settings.domain = {'dev': 'https://test.test'}
    mock_settings.domain_mil = {'dev': 'https://test.test'}
    mock_settings.endpoints = SimpleNamespace(
        base_path='/api/v1',
        base_path_message_core='/test',
        message_core=SimpleNamespace(base_path='/message-core')
    )

    mock_richiesta_con_token.return_value = 'mocked-token'

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_requests.return_value = mock_response

    api = MessageCoreAPI()
    response = api.send_message({})

    mock_richiesta_con_token.assert_called_once_with("token_send")
    mock_requests.assert_called_once()
    assert response.status_code == 200