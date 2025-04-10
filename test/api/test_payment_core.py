from unittest.mock import patch, MagicMock
from types import SimpleNamespace

from api.payment_core import PaymentCoreAPI


@patch('api.payment_core.settings')
@patch('api.bearer_token.richiesta_con_token')
@patch('api.payment_core.requests.request')
def test_retrieval_tokens(mock_requests, mock_richiesta_con_token, mock_settings):
    mock_settings.TARGET_ENV = 'dev'
    mock_settings.domain = {'dev': 'https://test.test'}
    mock_settings.domain_mil = {'dev': 'https://test.test'}
    mock_settings.endpoints = SimpleNamespace(
        base_path='/api/v1',
        base_path_payment_core='/test',
        payment_core=SimpleNamespace(base_path='/message-core')
    )

    mock_richiesta_con_token.return_value = 'mocked-token'

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_requests.return_value = mock_response

    api = PaymentCoreAPI()
    response = api.retrieval_tokens({"id":"id"},"tpp_name")

    mock_richiesta_con_token.assert_called_once_with("tpp_name")
    mock_requests.assert_called_once()
    assert response.status_code == 200


@patch('api.payment_core.settings')
@patch('api.bearer_token.richiesta_con_token')
@patch('api.payment_core.requests.request')
def test_get_token(mock_requests, mock_richiesta_con_token, mock_settings):
    mock_settings.TARGET_ENV = 'dev'
    mock_settings.domain = {'dev': 'https://test.test'}
    mock_settings.domain_mil = {'dev': 'https://test.test'}
    mock_settings.endpoints = SimpleNamespace(
        base_path='/api/v1',
        base_path_payment_core='/test',
        payment_core=SimpleNamespace(base_path='/message-core')
    )

    mock_richiesta_con_token.return_value = 'mocked-token'

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_requests.return_value = mock_response

    api = PaymentCoreAPI()
    response = api.get_token("retrieval_id")

    mock_richiesta_con_token.assert_called_once_with("token_send")
    mock_requests.assert_called_once()
    assert response.status_code == 200

