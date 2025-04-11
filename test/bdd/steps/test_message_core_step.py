from unittest.mock import patch, MagicMock
from bdd.steps import message_core_step


@patch('bdd.steps.message_core_step.settings')
def test_step_build_message(mock_settings):
    mock_settings.CitizenFake = "mocked-citizen"

    context = MagicMock()
    message_core_step.step_build_message(context, 'CitizenFake')


@patch('bdd.steps.message_core_step.message_core_api.send_message')
def test_step_notification_request(mock_send_message):

    mock_response_1 = MagicMock()
    mock_response_1.json.return_value = {"state": "mocked-true"}
    mock_send_message.return_value = mock_response_1

    context = MagicMock()
    message_core_step.step_notification_request(context)

def test_step_check_status_code():
    context = MagicMock()
    context.response.status_code = 200
    message_core_step.step_check_status_code(context, 200)

def test_step_check_message_response():
    context = MagicMock()

    mock_response = MagicMock()
    mock_response.json.return_value = {
        "outcome": "OK"
    }
    context.response = mock_response
    message_core_step.step_check_message_response(context, "OK")