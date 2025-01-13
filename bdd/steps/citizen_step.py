import api.citizen as api

from behave import given
from behave import then
from behave import when
from conf.configuration import settings
from api.tpp import get_tpp


@given('{tpp} is a valid tpp')
def step_check_tpp(context, tpp):
    tpp = getattr(settings, tpp, None)
    status_code = get_tpp(tpp).status_code
    assert status_code == 200, (
        f"[CITIZEN_STEP][CHECK_TPP]Expected status code 200, got {status_code} instead."
    )


@given('{tpp} is not valid')
def step_check_tpp_not_valid(context, tpp):
    tpp = getattr(settings, tpp, None)
    status_code = get_tpp(tpp).status_code
    assert status_code == 404, (
        f"[CITIZEN_STEP][CHECK_TPP_NOT_VALID]Expected status code 404, got {status_code} instead."
    )


@given('{citizen} not onboarded on {tpp}')
def step_check_not_onboarded(context, citizen, tpp):
    citizen = getattr(settings, citizen, None)
    tpp = getattr(settings, tpp, None)
    status_code = api.get_consent(citizen, tpp).status_code
    assert status_code == 404, (
        f"[CITIZEN_STEP][CHECK_NOT_ONBOARDED] Expected status code 404, got {status_code} instead."
    )


@given('{citizen} never onboarded')
def step_check_never_onboarded(context, citizen):
    citizen = getattr(settings, citizen, None)
    status_code = api.get_consent_list(citizen).status_code
    assert status_code == 404, (
        f"[CITIZEN_STEP][CHECK_NEVER_ONBOARDED] Expected status code 404, got {status_code} instead."
    )


@given('{citizen} already onboarded on {tpp}')
def step_check_onboarded(context, citizen, tpp):
    citizen = getattr(settings, citizen, None)
    tpp = getattr(settings, tpp, None)
    status_code = api.save_consent(citizen, tpp).status_code
    assert status_code == 200, (
        f"[CITIZEN_STEP][CHECK_ONBOARDED] Expected status code 200, got {status_code} instead."
    )


@given('{citizen} onboarded on {tpp} but disabled')
def step_check_onboarded_disabled(context, citizen, tpp):
    citizen = getattr(settings, citizen, None)
    tpp = getattr(settings, tpp, None)
    status_code = api.save_consent(citizen, tpp).status_code
    assert status_code == 200, (
        f"[CITIZEN_STEP][CHECK_ONBOARDED] Expected status code 200, got {status_code} instead."
    )
    status_code = api.switch_state(citizen, tpp).status_code
    assert status_code == 200, (
        f"[CITIZEN_STEP][CHECK_ONBOARDED_DISABLED] Expected status code 200, got {status_code} instead."
    )


@given('{citizen} onboarded on {tpp_a} and not on {tpp_b}')
def step_check_onboarded_only_on_first(context, citizen, tpp_a, tpp_b):
    citizen = getattr(settings, citizen, None)
    tpp_a = getattr(settings, tpp_a, None)
    status_code = api.save_consent(citizen, tpp_a).status_code
    assert status_code == 200, (
        f"[CITIZEN_STEP][CHECK_ONBOARDED_ON_FIRST]Expected status code 200, got {status_code} instead."
    )
    tpp_b = getattr(settings, tpp_b, None)
    status_code = api.get_consent(citizen, tpp_b).status_code
    assert status_code != 200, (
        f"[CITIZEN_STEP][CHECK_NOT_ONBOARDED_ON_SECOND]Expected status code 200, got {status_code} instead."
    )


@when('an onboarding for {citizen} on {tpp} request arrives')
def step_create_consent(context, citizen, tpp):
    tpp = getattr(settings, tpp, None)
    citizen = getattr(settings, citizen, None)
    context.tpp_enabled = tpp
    context.response = api.save_consent(citizen, tpp)


@when('a state change for {citizen} on {tpp} request arrives')
def step_state_change(context, citizen, tpp):
    tpp = getattr(settings, tpp, None)
    citizen = getattr(settings, citizen, None)
    context.tpp_enabled = tpp
    context.response = api.switch_state(citizen, tpp)


@when('a get consent state for {citizen} and {tpp} request arrives')
def step_get_consent(context, citizen, tpp):
    tpp = getattr(settings, tpp, None)
    citizen = getattr(settings, citizen, None)
    context.tpp_enabled = tpp
    context.response = api.get_consent(citizen, tpp)


@when('a get consents list for {citizen} request arrives')
def step_get_consent(context, citizen):
    citizen = getattr(settings, citizen, None)
    context.response = api.get_consent_list(citizen)


@when('a get consents list enabled for {citizen} request arrives')
def step_get_consent(context, citizen):
    citizen = getattr(settings, citizen, None)
    context.response = api.get_consent_list_enabled(citizen)


@when('a get citizens onboarded list for {tpp} request arrives')
def step_get_consent(context, tpp):
    tpp = getattr(settings, tpp, None)
    context.tpp_enabled = tpp
    context.response = api.get_citizens_on_tpp(tpp)


@then('the creation request is successful')
def step_creation_request_successful(context):
    status_code = context.response.status_code
    response_data = context.response.json()
    consents = response_data.get("consents")
    # The tc_date format on db is yyyy-MM-dd'T'HH:mm:ss.SSS, so we use [:22] to force that format
    tc_date = consents[context.tpp_enabled]['tcDate'][:22]
    setattr(settings, 'tc_date', tc_date)
    assert status_code == 200, (
        f"[CITIZEN_STEP][CREATION_REQUEST_SUCCESSFUL] Expected status code 200, got {status_code} instead."
    )


@then('the creation request is idempotent')
def step_creation_request_idempotent(context):
    status_code = context.response.status_code
    response_data = context.response.json()
    consents = response_data.get("consents")
    tc_date = consents[context.tpp_enabled]['tcDate'][:22]
    print(f'response {response_data}')
    print(f'tc_saved att {getattr(settings, "tc_date", None)}')
    print(f'tc_saved response {tc_date}')
    assert status_code == 200, (
        f"[CITIZEN_STEP][CREATION_REQUEST_IDEMPOTENT] Expected status code 200, got {status_code} instead."
    )
    assert tc_date == getattr(settings, 'tc_date', None), (
        f"[CITIZEN_STEP][CREATION_REQUEST_IDEMPOTENT] "
        f"Expected tc_date {getattr(settings, 'tc_date', None)}, got {tc_date} instead."
    )


@then('others onboarding are not visible')
def step_others_onboarding_are_not_visible(context):
    response_data = context.response.json()
    consents = response_data.get("consents")
    actual_key = list(consents.keys())[0]
    assert len(consents) == 1, (
        f"[CITIZEN_STEP][OTHER_ONBOARDING_NOT_VISIBLE] Expected 1 key in 'consents', but found {len(consents)}."
    )
    assert actual_key == context.tpp_enabled, (
        f"[CITIZEN_STEP][OTHER_ONBOARDING_NOT_VISIBLE] Expected key '{context.tpp_enabled}', but found '{actual_key}'."
    )


@then('the state change request is successful')
def step_state_change_request_successful(context):
    status_code = context.response.status_code
    assert status_code == 200, (
        f"[CITIZEN_STEP][CHANGE_REQUEST_SUCCESSFUL] Expected status code 200, got {status_code} instead."
    )


@then('the state change request fail')
def step_state_change_request_fail(context):
    status_code = context.response.status_code
    assert status_code == 404, (
        f"[CITIZEN_STEP][CHANGE_REQUEST_FAIL] Expected status code 404, got {status_code} instead."
    )


@then('the get consent state request fail')
def step_get_consents_list_request_fail(context):
    status_code = context.response.status_code
    assert status_code == 404, (
        f"[CITIZEN_STEP][GET_CONSENT_SUCCESSFUL] Expected status code 404, got {status_code} instead."
    )


@then('the get consent state request is successful')
def step_get_consent_request_successful(context):
    status_code = context.response.status_code
    assert status_code == 200, (
        f"[CITIZEN_STEP][GET_CONSENT_SUCCESSFUL] Expected status code 200, got {status_code} instead."
    )


@then('the get consents list request fail')
def step_get_consents_list_request_fail(context):
    status_code = context.response.status_code
    assert status_code == 404, (
        f"[CITIZEN_STEP][GET_CONSENTS_LIST_SUCCESSFUL] Expected status code 404, got {status_code} instead."
    )


@then('the get consents list request is successful')
def step_get_consents_list_request_successful(context):
    status_code = context.response.status_code
    assert status_code == 200, (
        f"[CITIZEN_STEP][GET_CONSENTS_LIST_SUCCESSFUL] Expected status code 200, got {status_code} instead."
    )


@then('the consents list is not empty')
def step_consent_list_not_empty(context):
    response_data = context.response.json()
    consents = response_data.get("consents")
    assert len(consents) != 0, (
        f"[CITIZEN_STEP][CONSENT_LIST_NOT_EMPTY] Expected at least 1 key in 'consents', but found {len(consents)}."
    )


@then('the consents list is empty')
def step_consent_list_is_empty(context):
    response_data = context.response.json()
    consents = response_data.get("consents")
    assert len(consents) == 0, (
        f"[CITIZEN_STEP][CONSENT_LIST_IS_EMPTY] Expected at least no key in 'consents', but found {len(consents)}."
    )


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
    assert status_code == 404, (
        f"[CITIZEN_STEP][GET_CONSENTS_LIST_SUCCESSFUL] Expected status code 404, got {status_code} instead."
    )


@then('the get citizens onboarded list request is successful')
def step_get_citizens_onboarded_list_request_successful(context):
    status_code = context.response.status_code
    assert status_code == 200, (
        f"[CITIZEN_STEP][GET_CONSENTS_LIST_SUCCESSFUL] Expected status code 200, got {status_code} instead."
    )


@then('the tpp consents list is empty')
def step_tpp_consents_list_is(context):
    response_data = context.response.json()
    assert len(response_data) == 0, (
        f"[CITIZEN_STEP][GET_CONSENTS_LIST_SUCCESSFUL] Expected no consents, got {response_data} instead."
    )


@then('the tpp consents list is not empty')
def step_get_citizens_onboarded_list_request_successful(context):
    response_data = context.response.json()
    assert len(response_data) != 0, (
        f"[CITIZEN_STEP][GET_CONSENTS_LIST_SUCCESSFUL] Expected at least 1 consent, got {response_data} instead."
    )


@then('the get consents list enabled request fail')
def step_get_consents_list_enabled_request_fail(context):
    status_code = context.response.status_code
    assert status_code == 404, (
        f"[CITIZEN_STEP][GET_CONSENTS_LIST_ENABLED__SUCCESSFUL] Expected status code 404, got {status_code} instead."
    )


@then('the get consents list enabled request is successful')
def step_get_consents_list_enabled_request_successful(context):
    status_code = context.response.status_code
    assert status_code == 200, (
        f"[CITIZEN_STEP][GET_CONSENTS_LIST_ENABLED_SUCCESSFUL] Expected status code 200, got {status_code} instead."
    )


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
