from unittest.mock import patch, MagicMock
from bdd.steps import tpp_step


@patch('bdd.steps.tpp_step.settings')
@patch('bdd.steps.tpp_step.tpp_api.get_tpp_by_entity_id')
def test_step_check_not_onboarded(mock_get_tpp_by_entity_id, mock_settings):
    mock_settings.EntityIdFake = "mocked-entity-id-fake"

    mock_response_1 = MagicMock()
    mock_response_1.status_code = 404
    mock_get_tpp_by_entity_id.return_value = mock_response_1

    context = MagicMock()
    tpp_step.step_check_not_onboarded(context,"EntityIdFake")

    mock_get_tpp_by_entity_id.assert_called_once_with('mocked-entity-id-fake')

@patch('bdd.steps.tpp_step.settings')
@patch('bdd.steps.tpp_step.tpp_api.get_tpp_by_entity_id')
def test_step_check_already_onboarded(mock_get_tpp_by_entity_id, mock_settings):
    mock_settings.EntityIdFake = "mocked-entity-id-fake"

    mock_response_1 = MagicMock()
    mock_response_1.status_code = 200
    mock_get_tpp_by_entity_id.return_value = mock_response_1

    context = MagicMock()
    tpp_step.step_check_already_onboarded(context,"EntityIdFake")

    mock_get_tpp_by_entity_id.assert_called_once_with('mocked-entity-id-fake')

@patch('bdd.steps.tpp_step.settings')
@patch('bdd.steps.tpp_step.tpp_api.save_tpp')
def test_step_onboarding_request(mock_save_tpp, mock_settings):
    mock_settings.EntityIdFake = "mocked-entity-id-fake"
    mock_settings.TppDtoFake = {"tppId":"mocked-tpp-id-fake"}

    mock_response_1 = MagicMock()
    mock_response_1.json.return_value = {"tppId":"mocked-tpp-id-fake"}
    mock_save_tpp.return_value = mock_response_1

    context = MagicMock()
    tpp_step.step_onboarding_request(context,"EntityIdFake")


@patch('bdd.steps.tpp_step.settings')
@patch('bdd.steps.tpp_step.tpp_api.get_tpp_by_entity_id')
@patch('bdd.steps.tpp_step.tpp_api.update_tpp')
def test_step_update_request(mock_update_tpp, mock_get_tpp_by_entity_id, mock_settings):
    mock_settings.EntityIdFake = "mocked-entity-id-fake"
    mock_settings.TppDtoFake = {"tppId": "mocked-tpp-id-fake"}

    mock_response_1 = MagicMock()
    mock_response_1.json.return_value = {"tppId": "mocked-tpp-id-fake"}
    mock_get_tpp_by_entity_id.return_value = mock_response_1

    mock_response_2 = MagicMock()
    mock_response_2.json.return_value = {"tppId": "mocked-tpp-id-fake"}
    mock_update_tpp.return_value = mock_response_2

    context = MagicMock()
    tpp_step.step_update_request(context,"EntityIdFake")

@patch('bdd.steps.tpp_step.settings')
@patch('bdd.steps.tpp_step.tpp_api.get_tpp_by_entity_id')
@patch('bdd.steps.tpp_step.tpp_api.update_status_tpp')
def test_step_change_request(mock_update_status_tpp, mock_get_tpp_by_entity_id, mock_settings):
    mock_settings.EntityIdFake = "mocked-entity-id-fake"
    mock_settings.TppDtoFake = {"tppId": "mocked-tpp-id-fake"}

    mock_response_1 = MagicMock()
    mock_response_1.json.return_value = {"tppId": "mocked-tpp-id-fake"}
    mock_get_tpp_by_entity_id.return_value = mock_response_1

    mock_response_2 = MagicMock()
    mock_response_2.json.return_value = {"tppId": "mocked-tpp-id-fake"}
    mock_update_status_tpp.return_value = mock_response_2

    context = MagicMock()
    tpp_step.step_change_request(context,"EntityIdFake")


def test_step_check_creation_ok():
    context = MagicMock()
    context.response.status_code = 200
    tpp_step.step_check_creation_ok(context)

def test_step_check_changing_ok():
    context = MagicMock()
    context.response.status_code = 200
    tpp_step.step_check_changing_ok(context)

def test_step_check_creation_fail():
    context = MagicMock()
    context.response.status_code = 403
    tpp_step.step_check_creation_fail(context)
