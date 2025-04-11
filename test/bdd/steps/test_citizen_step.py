from unittest.mock import patch, MagicMock
from bdd.steps import citizen_step


@patch('bdd.steps.citizen_step.settings')
@patch('bdd.steps.citizen_step.tpp_api.get_tpp_info')
@patch('bdd.steps.citizen_step.tpp_api.get_tpp_by_entity_id')
def test_step_check_tpp(mock_get_tpp_by_entity_id, mock_get_tpp_info, mock_settings):
    mock_settings.TppFake = "mocked-tpp-entity-id"

    mock_response_1 = MagicMock()
    mock_response_1.json.return_value = {"tppId": "mocked-tpp-id"}
    mock_get_tpp_by_entity_id.return_value = mock_response_1

    mock_response_2 = MagicMock()
    mock_response_2.status_code = 200
    mock_get_tpp_info.return_value = mock_response_2

    context = MagicMock()
    citizen_step.step_check_tpp(context, 'TppFake')

    mock_get_tpp_by_entity_id.assert_called_once_with("mocked-tpp-entity-id")
    mock_get_tpp_info.assert_called_once_with('mocked-tpp-id')


@patch('bdd.steps.citizen_step.settings')
@patch('bdd.steps.citizen_step.tpp_api.get_tpp_info')
@patch('bdd.steps.citizen_step.tpp_api.get_tpp_by_entity_id')
def test_step_check_tpp_not_valid(mock_get_tpp_by_entity_id, mock_get_tpp_info, mock_settings):
    mock_settings.TppFake = "mocked-tpp-entity-id"

    mock_response_1 = MagicMock()
    mock_response_1.json.return_value = {"tppId": "mocked-tpp-id"}
    mock_get_tpp_by_entity_id.return_value = mock_response_1

    mock_response_2 = MagicMock()
    mock_response_2.status_code = 404
    mock_get_tpp_info.return_value = mock_response_2

    context = MagicMock()
    citizen_step.step_check_tpp_not_valid(context, 'TppFake')

    mock_get_tpp_by_entity_id.assert_called_once_with("mocked-tpp-entity-id")
    mock_get_tpp_info.assert_called_once_with('mocked-tpp-id')


@patch('bdd.steps.citizen_step.settings')
@patch('bdd.steps.citizen_step.tpp_api.get_tpp_by_entity_id')
@patch('bdd.steps.citizen_step.citizen_api.get_consent')
def test_step_check_not_onboarded(mock_get_consent, mock_get_tpp_by_entity_id, mock_settings):
    mock_settings.TppFake = "mocked-tpp-entity-id"
    mock_settings.CitizenFake = "mocked-citizen"

    mock_response_1 = MagicMock()
    mock_response_1.json.return_value = {"tppId": "mocked-tpp-id"}
    mock_get_tpp_by_entity_id.return_value = mock_response_1

    mock_response_2 = MagicMock()
    mock_response_2.status_code = 404
    mock_get_consent.return_value = mock_response_2

    context = MagicMock()
    citizen_step.step_check_not_onboarded(context, 'CitizenFake', 'TppFake')

    mock_get_tpp_by_entity_id.assert_called_once_with('mocked-tpp-entity-id')
    mock_get_consent.assert_called_once_with("mocked-citizen", "mocked-tpp-id")


@patch('bdd.steps.citizen_step.settings')
@patch('bdd.steps.citizen_step.citizen_api.get_consent_list')
def test_step_check_never_onboarded(mock_get_consent_list, mock_settings):
    mock_settings.CitizenFake = "mocked-citizen"

    mock_response_1 = MagicMock()
    mock_response_1.status_code = 404
    mock_get_consent_list.return_value = mock_response_1

    context = MagicMock()
    citizen_step.step_check_never_onboarded(context, 'CitizenFake')

    mock_get_consent_list.assert_called_once_with("mocked-citizen")


@patch('bdd.steps.citizen_step.settings')
@patch('bdd.steps.citizen_step.citizen_api.save_consent')
@patch('bdd.steps.citizen_step.tpp_api.get_tpp_by_entity_id')
def test_step_check_onboarded(mock_get_tpp_by_entity_id, mock_save_consent, mock_settings):
    mock_settings.TppFake = "mocked-tpp-entity-id"
    mock_settings.CitizenFake = "mocked-citizen"

    mock_response_1 = MagicMock()
    mock_response_1.json.return_value = {"tppId": "mocked-tpp-id"}
    mock_get_tpp_by_entity_id.return_value = mock_response_1

    mock_response_2 = MagicMock()
    mock_response_2.status_code = 200
    mock_save_consent.return_value = mock_response_2

    context = MagicMock()
    citizen_step.step_check_onboarded(context, 'CitizenFake', 'TppFake')

    mock_get_tpp_by_entity_id.assert_called_once_with('mocked-tpp-entity-id')
    mock_save_consent.assert_called_once_with("mocked-citizen", "mocked-tpp-id")


@patch('bdd.steps.citizen_step.settings')
@patch('bdd.steps.citizen_step.citizen_api.switch_state')
@patch('bdd.steps.citizen_step.citizen_api.save_consent')
@patch('bdd.steps.citizen_step.tpp_api.get_tpp_by_entity_id')
def test_step_check_onboarded_disabled(mock_get_tpp_by_entity_id, mock_save_consent, mock_switch_state, mock_settings):
    mock_settings.CitizenFake = "mocked-citizen"
    mock_settings.TppFake = "mocked-tpp-entity-id"

    mock_response_1 = MagicMock()
    mock_response_1.json.return_value = {"tppId": "mocked-tpp-id"}
    mock_get_tpp_by_entity_id.return_value = mock_response_1

    mock_response_2 = MagicMock()
    mock_response_2.status_code = 200
    mock_save_consent.return_value = mock_response_2

    mock_response_3 = MagicMock()
    mock_response_3.status_code = 200
    mock_switch_state.return_value = mock_response_3

    context = MagicMock()
    citizen_step.step_check_onboarded_disabled(context, 'CitizenFake', 'TppFake')

    mock_get_tpp_by_entity_id.assert_called_once_with('mocked-tpp-entity-id')
    mock_save_consent.assert_called_once_with('mocked-citizen','mocked-tpp-id')
    mock_switch_state.assert_called_once_with('mocked-citizen','mocked-tpp-id')


@patch('bdd.steps.citizen_step.settings')
@patch('bdd.steps.citizen_step.citizen_api.get_consent')
@patch('bdd.steps.citizen_step.citizen_api.save_consent')
@patch('bdd.steps.citizen_step.tpp_api.get_tpp_by_entity_id')
def test_step_check_onboarded_only_on_first(mock_get_tpp_by_entity_id, mock_save_consent, mock_get_consent, mock_settings):
    mock_settings.CitizenFake = "mocked-citizen"
    mock_settings.TppFakeA = "mocked-tpp-entity-id"

    mock_response_1 = MagicMock()
    mock_response_1.json.return_value = {"tppId": "mocked-tpp-id"}
    mock_get_tpp_by_entity_id.return_value = mock_response_1

    mock_response_2 = MagicMock()
    mock_response_2.status_code = 200
    mock_save_consent.return_value = mock_response_2

    mock_settings.TppFakeB = "mocked-tpp-entity-id"

    mock_response_3 = MagicMock()
    mock_response_3.status_code = 202
    mock_get_consent.return_value = mock_response_3

    context = MagicMock()
    citizen_step.step_check_onboarded_only_on_first(context, 'CitizenFake', 'TppFakeA', 'TppFakeB')

    mock_save_consent.assert_called_once_with('mocked-citizen','mocked-tpp-id')
    mock_get_consent.assert_called_once_with('mocked-citizen','mocked-tpp-id')



@patch('bdd.steps.citizen_step.settings')
@patch('bdd.steps.citizen_step.citizen_api.save_consent')
@patch('bdd.steps.citizen_step.tpp_api.get_tpp_by_entity_id')
def test_step_create_consent(mock_get_tpp_by_entity_id, mock_save_consent, mock_settings):
    mock_settings.CitizenFake = "mocked-citizen"
    mock_settings.TppFake = "mocked-tpp-entity-id"

    mock_response_1 = MagicMock()
    mock_response_1.json.return_value = {"tppId": "mocked-tpp-id"}
    mock_get_tpp_by_entity_id.return_value = mock_response_1

    mock_response_2 = MagicMock()
    mock_response_2.status_code = {"fiscalCode": "mocked-fiscal-code"}
    mock_save_consent.return_value = mock_response_2

    context = MagicMock()
    citizen_step.step_create_consent(context, 'CitizenFake', 'TppFake')

    mock_get_tpp_by_entity_id.assert_called_once_with('mocked-tpp-entity-id')
    mock_save_consent.assert_called_once_with('mocked-citizen','mocked-tpp-id')


@patch('bdd.steps.citizen_step.settings')
@patch('bdd.steps.citizen_step.citizen_api.switch_state')
@patch('bdd.steps.citizen_step.tpp_api.get_tpp_by_entity_id')
def test_step_state_change(mock_get_tpp_by_entity_id, mock_switch_state, mock_settings):
    mock_settings.CitizenFake = "mocked-citizen"
    mock_settings.TppFake = "mocked-tpp-entity-id"

    mock_response_1 = MagicMock()
    mock_response_1.json.return_value = {"tppId": "mocked-tpp-id"}
    mock_get_tpp_by_entity_id.return_value = mock_response_1

    mock_response_2 = MagicMock()
    mock_response_2.status_code = {"state": "mocked-true"}
    mock_switch_state.return_value = mock_response_2

    context = MagicMock()
    citizen_step.step_state_change(context, 'CitizenFake', 'TppFake')

    mock_get_tpp_by_entity_id.assert_called_once_with('mocked-tpp-entity-id')
    mock_switch_state.assert_called_once_with('mocked-citizen','mocked-tpp-id')


@patch('bdd.steps.citizen_step.settings')
@patch('bdd.steps.citizen_step.citizen_api.get_consent')
@patch('bdd.steps.citizen_step.tpp_api.get_tpp_by_entity_id')
def test_step_get_consent(mock_get_tpp_by_entity_id, mock_get_consent, mock_settings):
    mock_settings.CitizenFake = "mocked-citizen"
    mock_settings.TppFake = "mocked-tpp-entity-id"

    mock_response_1 = MagicMock()
    mock_response_1.json.return_value = {"tppId": "mocked-tpp-id"}
    mock_get_tpp_by_entity_id.return_value = mock_response_1

    mock_response_2 = MagicMock()
    mock_response_2.json.return_value = {"state": "mocked-true"}
    mock_get_consent.return_value = mock_response_2

    context = MagicMock()
    citizen_step.step_get_consent(context, 'CitizenFake', 'TppFake')

    mock_get_tpp_by_entity_id.assert_called_once_with('mocked-tpp-entity-id')
    mock_get_consent.assert_called_once_with('mocked-citizen','mocked-tpp-id')


@patch('bdd.steps.citizen_step.settings')
@patch('bdd.steps.citizen_step.citizen_api.get_consent_list')
def test_step_get_consent_list(mock_get_consent_list, mock_settings):
    mock_settings.CitizenFake = "mocked-citizen"

    mock_response_2 = MagicMock()
    mock_response_2.json.return_value = {"state": "mocked-true"}
    mock_get_consent_list.return_value = mock_response_2

    context = MagicMock()
    citizen_step.step_get_consent_list(context, 'CitizenFake')

    mock_get_consent_list.assert_called_once_with('mocked-citizen')


@patch('bdd.steps.citizen_step.settings')
@patch('bdd.steps.citizen_step.citizen_api.get_consent_list_enabled')
def test_step_get_consent_list_enabled(mock_get_consent_list_enabled, mock_settings):
    mock_settings.CitizenFake = "mocked-citizen"

    mock_response_2 = MagicMock()
    mock_response_2.status_code = {"state": "mocked-true"}
    mock_get_consent_list_enabled.return_value = mock_response_2

    context = MagicMock()
    citizen_step.step_get_consent_list_enabled(context, 'CitizenFake')

    mock_get_consent_list_enabled.assert_called_once_with('mocked-citizen')

@patch('bdd.steps.citizen_step.settings')
@patch('bdd.steps.citizen_step.citizen_api.get_citizens_on_tpp')
@patch('bdd.steps.citizen_step.tpp_api.get_tpp_by_entity_id')
def test_step_get_consent_on_tpp(mock_get_tpp_by_entity_id, mock_get_citizens_on_tpp, mock_settings):
    mock_settings.TppFake = "mocked-tpp-entity-id"

    mock_response_1 = MagicMock()
    mock_response_1.json.return_value = {"tppId": "mocked-tpp-id"}
    mock_get_tpp_by_entity_id.return_value = mock_response_1

    mock_response_2 = MagicMock()
    mock_response_2.json.return_value = {"state": "mocked-true"}
    mock_get_citizens_on_tpp.return_value = mock_response_2

    context = MagicMock()
    citizen_step.step_get_consent_on_tpp(context, 'TppFake')

    mock_get_tpp_by_entity_id.assert_called_once_with('mocked-tpp-entity-id')
    mock_get_citizens_on_tpp.assert_called_once_with('mocked-tpp-id')


def test_step_creation_request_successful():
    context = MagicMock()
    context.response.status_code = 200
    citizen_step.step_creation_request_successful(context)

def test_step_creation_request_idempotent():
    context = MagicMock()
    context.response.status_code = 200
    citizen_step.step_creation_request_idempotent(context)

def test_step_others_onboarding_are_not_visible():
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "consents": ["consent1"]
    }
    context = MagicMock()
    context.response = mock_response
    citizen_step.step_others_onboarding_are_not_visible(context)

def test_step_state_change_request_successful():
    context = MagicMock()
    context.response.status_code = 200
    citizen_step.step_state_change_request_successful(context)

def test_step_state_change_request_fail():
    context = MagicMock()
    context.response.status_code = 404
    citizen_step.step_state_change_request_fail(context)

def test_step_get_consents_state_request_fail():
    context = MagicMock()
    context.response.status_code = 404
    citizen_step.step_get_consents_state_request_fail(context)

def test_step_get_consent_request_successful():
    context = MagicMock()
    context.response.status_code = 200
    citizen_step.step_get_consent_request_successful(context)

def test_step_get_consents_list_request_fail():
    context = MagicMock()
    context.response.status_code = 404
    citizen_step.step_get_consents_list_request_fail(context)

def test_step_get_consents_list_request_successful():
    context = MagicMock()
    context.response.status_code = 200
    citizen_step.step_get_consents_list_request_successful(context)

def test_step_consent_list_not_empty():
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "consents": ["consent1"]
    }
    context = MagicMock()
    context.response = mock_response
    citizen_step.step_consent_list_not_empty(context)

def test_step_consent_list_is_empty():
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "consents": []
    }
    context = MagicMock()
    context.response = mock_response
    citizen_step.step_consent_list_is_empty(context)

def test_step_consent_list_are_enabled():
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "consents": {
            "consent1": {"tppState": "approved"},
            "consent2": {"tppState": "pending"}
        }
    }
    context = MagicMock()
    context.response = mock_response
    citizen_step.step_consent_list_are_enabled(context)

def test_step_get_citizens_onboarded_list_request_fail():
    context = MagicMock()
    context.response.status_code = 404
    citizen_step.step_get_citizens_onboarded_list_request_fail(context)

def test_step_get_citizens_onboarded_list_request_successful():
    context = MagicMock()
    context.response.status_code = 200
    citizen_step.step_get_citizens_onboarded_list_request_successful(context)

def test_step_tpp_consents_list_is():
    mock_response = MagicMock()
    mock_response.json.return_value = {
    }
    context = MagicMock()
    context.response = mock_response
    citizen_step.step_tpp_consents_list_is(context)

def test_step_get_citizens_list_request_successful():
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "element": "element"
    }
    context = MagicMock()
    context.response = mock_response
    citizen_step.step_get_citizens_list_request_successful(context)

def test_step_get_consents_list_enabled_request_fail():
    context = MagicMock()
    context.response.status_code = 404
    citizen_step.step_get_consents_list_enabled_request_fail(context)

def test_step_get_consents_list_enabled_request_successful():
    context = MagicMock()
    context.response.status_code = 200
    citizen_step.step_get_consents_list_enabled_request_successful(context)

def test_step_only_the_tpp_enabled_consent_are_visible():
    mock_response = MagicMock()
    mock_response.json.return_value = [{
        "fiscalCode": "1234567890",
        "consents": {
            "1234567890": {"tppState": True}
        }
    }]
    context = MagicMock()
    context.response = mock_response
    context.tpp_enabled = "1234567890"
    citizen_step.step_only_the_tpp_enabled_consent_are_visible(context)