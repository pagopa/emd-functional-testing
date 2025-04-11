from unittest.mock import patch, MagicMock

from api import bearer_token

@patch('api.bearer_token.secrets')
@patch('api.bearer_token.requests.request')
def test_request_new_token(mock_requests, mock_secrets):
    mock_secrets.tpp_token_info.url = 'url'
    mock_secrets.tpp_token_info.client_id = 'client_id'
    mock_secrets.tpp_token_info.client_secret = 'client_secret'
    mock_secrets.tpp_token_info.grant_type = 'grant_type'

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"access_token":"access_token","expires_in":0}
    mock_requests.return_value = mock_response
    bearer_token.richiesta_con_token('token_tpp')
    mock_requests.assert_called_once()


