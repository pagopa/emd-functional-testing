from unittest.mock import patch, MagicMock
from types import SimpleNamespace
from bdd import environment


@patch('bdd.environment.citizen_api.save_consent')
@patch('bdd.environment.tpp_api.save_tpp')
@patch('bdd.environment.settings')
def test_before_feature(mock_settings, mock_save_tpp, mock_save_consent):
    mock_settings.TppDtoFake = {"tppId": "mocked-tpp-id-fake"}
    mock_settings.TppFakeEntityIdA = {"tppId": "mocked-tpp-id-fake"}
    mock_settings.TppFakeEntityIdB = {"tppId": "mocked-tpp-id-fake"}
    mock_settings.TppFakeEntityIdC = {"tppId": "mocked-tpp-id-fake"}
    mock_settings.TppFakeEntityIdD = {"tppId": "mocked-tpp-id-fake"}

    mock_response_1 = MagicMock()
    mock_response_1.json.return_value = {"tppId":"mocked-tpp-id-fake"}
    mock_save_tpp.return_value = mock_response_1

    mock_settings.CitizenS = "mocked-citizen"

    mock_response_2 = MagicMock()
    mock_response_2.json.return_value = {"tppId":"mocked-tpp-id-fake"}
    mock_save_consent.return_value = mock_response_2

    context = MagicMock()
    feature = MagicMock()
    environment.before_feature(context, feature)