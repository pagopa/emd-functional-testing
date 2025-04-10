from behave import given
from behave import then
from behave import when
from conf import configuration

from api.tpp import TppAPI
from api.citizen import CitizenAPI

tpp_api = TppAPI()
citizen_api = CitizenAPI()

settings = configuration.settings

@given('{tpp} is a valid tpp')
def step_check_tpp(context, tpp):
    tpp = getattr(settings, tpp, None)
    response = tpp_api.get_tpp_by_entity_id(tpp)
    tpp_id = response.json().get('tppId')
    status_code = tpp_api.get_tpp_info(tpp_id).status_code
    assert status_code == 200


@given('{tpp} is not valid')
def step_check_tpp_not_valid(context, tpp):
    tpp = getattr(settings, tpp, None)
    response = tpp_api.get_tpp_by_entity_id(tpp)
    tpp_id = response.json().get('tppId')
    status_code = tpp_api.get_tpp_info(tpp_id).status_code
    assert status_code == 404


@given('{citizen} not onboarded on {tpp}')
def step_check_not_onboarded(context, citizen, tpp):
    citizen = getattr(settings, citizen, None)
    tpp = getattr(settings, tpp, None)
    response = tpp_api.get_tpp_by_entity_id(tpp)
    tpp_id = response.json().get('tppId')
    status_code = citizen_api.get_consent(citizen, tpp_id).status_code
    assert status_code == 404


@given('{citizen} never onboarded')
def step_check_never_onboarded(context, citizen):
    citizen = getattr(settings, citizen, None)
    response = citizen_api.get_consent_list(citizen)
    assert response.status_code == 404

@given('{citizen} already onboarded on {tpp}')
def step_check_onboarded(context, citizen, tpp):
    citizen = getattr(settings, citizen, None)
    tpp = getattr(settings, tpp, None)
    tpp_id = tpp_api.get_tpp_by_entity_id(tpp)
    response = citizen_api.save_consent(citizen, tpp_id.json()["tppId"])
    context.citizens[citizen] = response.json()
    assert response.status_code == 200, (
        f"[CITIZEN_STEP][CHECK_ONBOARDED] Expected status code 200, got {response.status_code} instead."
    )


@given('{citizen} onboarded on {tpp} but disabled')
def step_check_onboarded_disabled(context, citizen, tpp):
    citizen = getattr(settings, citizen, None)
    entity_id = getattr(settings, tpp, None)
    tpp = tpp_api.get_tpp_by_entity_id(entity_id)
    response = citizen_api.save_consent(citizen, tpp.json().get('tppId'))
    context.citizens[citizen] = response.json()
    assert response.status_code == 200
    status_code = citizen_api.switch_state(citizen, tpp.json()["tppId"]).status_code
    assert status_code == 200


@given('{citizen} onboarded on {tpp_a} and not on {tpp_b}')
def step_check_onboarded_only_on_first(context, citizen, tpp_a, tpp_b):
    citizen = getattr(settings, citizen, None)
    tpp_a = getattr(settings, tpp_a, None)
    tpp = tpp_api.get_tpp_by_entity_id(tpp_a)
    status_code = citizen_api.save_consent(citizen, tpp.json()["tppId"]).status_code
    assert status_code == 200
    tpp_b = getattr(settings, tpp_b, None)
    tpp = tpp_api.get_tpp_by_entity_id(tpp_b)
    status_code = citizen_api.get_consent(citizen, tpp.json()["tppId"]).status_code
    assert status_code != 200


@when('an onboarding for {citizen} on {tpp} request arrives')
def step_create_consent(context, citizen, tpp):
    tpp = getattr(settings, tpp, None)
    citizen = getattr(settings, citizen, None)
    response = tpp_api.get_tpp_by_entity_id(tpp)
    tpp_id = response.json().get('tppId')
    context.response = citizen_api.save_consent(citizen, tpp_id)
    if "fiscalCode" in context.response.json():
        context.citizens[citizen] = context.response.json()



@when('a state change for {citizen} on {tpp} request arrives')
def step_state_change(context, citizen, tpp):
    tpp = getattr(settings, tpp, None)
    citizen = getattr(settings, citizen, None)
    response = tpp_api.get_tpp_by_entity_id(tpp)
    tpp_id = response.json().get('tppId')
    context.response = citizen_api.switch_state(citizen, tpp_id)


@when('a get consent state for {citizen} and {tpp} request arrives')
def step_get_consent(context, citizen, tpp):
    tpp = getattr(settings, tpp, None)
    citizen = getattr(settings, citizen, None)
    response = tpp_api.get_tpp_by_entity_id(tpp)
    tpp_id = response.json().get('tppId')
    context.tpp_enabled = tpp_id
    context.response = citizen_api.get_consent(citizen, tpp_id)


@when('a get consents list for {citizen} request arrives')
def step_get_consent_list(context, citizen):
    citizen = getattr(settings, citizen, None)
    context.response = citizen_api.get_consent_list(citizen)


@when('a get consents list enabled for {citizen} request arrives')
def step_get_consent_list_enabled(context, citizen):
    citizen = getattr(settings, citizen, None)
    context.response = citizen_api.get_consent_list_enabled(citizen)


@when('a get citizens onboarded list for {tpp} request arrives')
def step_get_consent_on_tpp(context, tpp):
    tpp = getattr(settings, tpp, None)
    response = tpp_api.get_tpp_by_entity_id(tpp)
    tpp_id = response.json().get('tppId')
    context.tpp_enabled = tpp_id
    context.response = citizen_api.get_citizens_on_tpp(tpp_id)


@then('the creation request is successful')
def step_creation_request_successful(context):
    status_code = context.response.status_code
    assert status_code == 200


@then('the creation request is idempotent')
def step_creation_request_idempotent(context):
    status_code = context.response.status_code
    assert status_code == 200


@then('others onboarding are not visible')
def step_others_onboarding_are_not_visible(context):
    response_data = context.response.json()
    consents = response_data.get("consents")
    assert len(consents) == 1


@then('the state change request is successful')
def step_state_change_request_successful(context):
    status_code = context.response.status_code
    assert status_code == 200


@then('the state change request fail')
def step_state_change_request_fail(context):
    status_code = context.response.status_code
    assert status_code == 404


@then('the get consent state request fail')
def step_get_consents_state_request_fail(context):
    status_code = context.response.status_code
    assert status_code == 404


@then('the get consent state request is successful')
def step_get_consent_request_successful(context):
    status_code = context.response.status_code
    assert status_code == 200


@then('the get consents list request fail')
def step_get_consents_list_request_fail(context):
    status_code = context.response.status_code
    assert status_code == 404


@then('the get consents list request is successful')
def step_get_consents_list_request_successful(context):
    status_code = context.response.status_code
    assert status_code == 200


@then('the consents list is not empty')
def step_consent_list_not_empty(context):
    response_data = context.response.json()
    consents = response_data.get("consents")
    assert len(consents) != 0


@then('the consents list is empty')
def step_consent_list_is_empty(context):
    response_data = context.response.json()
    consents = response_data.get("consents")
    assert len(consents) == 0


@then('all the consents are enabled')
def step_consent_list_are_enabled(context):
    response_data = context.response.json()
    consents = response_data.get("consents", {})

    for consent_id, consent_info in consents.items():
        tpp_state = consent_info.get("tppState")
        if not tpp_state:
            raise AssertionError(
                f"[CITIZEN_STEP][CONSENT_LIST_ARE_ENABLED] Expected all consents to be enabled"
            )


@then('the get citizens onboarded list request fail')
def step_get_citizens_onboarded_list_request_fail(context):
    status_code = context.response.status_code
    assert status_code == 404


@then('the get citizens onboarded list request is successful')
def step_get_citizens_onboarded_list_request_successful(context):
    status_code = context.response.status_code
    assert status_code == 200

@then('the tpp consents list is empty')
def step_tpp_consents_list_is(context):
    response_data = context.response.json()
    assert len(response_data) == 0


@then('the tpp consents list is not empty')
def step_get_citizens_list_request_successful(context):
    response_data = context.response.json()
    assert len(response_data) != 0


@then('the get consents list enabled request fail')
def step_get_consents_list_enabled_request_fail(context):
    status_code = context.response.status_code
    assert status_code == 404


@then('the get consents list enabled request is successful')
def step_get_consents_list_enabled_request_successful(context):
    status_code = context.response.status_code
    assert status_code == 200

@then('only the tpp enabled consent are visible')
def step_only_the_tpp_enabled_consent_are_visible(context):
    response_data = context.response.json()
    tpp = context.tpp_enabled

    for element in response_data:
        fiscal_code = element.get("fiscalCode", "UNKNOWN")
        consents = element.get("consents", {})

        if len(consents) != 1:
            raise AssertionError(
                f"[CITIZEN_STEP][GET_CONSENTS_LIST_ENABLED_SUCCESSFUL]  "
                f"{fiscal_code} - Consents does not contain exactly one pair."
            )

        if tpp not in consents:
            raise AssertionError(
                f"[CITIZEN_STEP][GET_CONSENTS_LIST_ENABLED_SUCCESSFUL]  "
                f"{fiscal_code} - Required key not found in consents."
            )

        if not consents[tpp].get("tppState", False):
            raise AssertionError(
                f"[CITIZEN_STEP][GET_CONSENTS_LIST_ENABLED_SUCCESSFUL] "
                f" {fiscal_code} - tppState is not True."
            )
