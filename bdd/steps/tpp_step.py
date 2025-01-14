import api.tpp as api

from behave import given
from behave import then
from behave import when
from conf.configuration import settings


@given('{tpp} not onboarded')
def step_check_not_onboarded(context, tpp):
    tpp = getattr(settings, tpp, None)
    status_code = api.get_tpp_info(tpp).status_code
    assert status_code == 404, (
        f"[CITIZEN_STEP][CHECK_NOT_ONBOARDED] Expected status code 404, got {status_code} instead."
    )


@given('{tpp} already onboarded')
def step_check_already_onboarded(context, tpp):
    tpp = getattr(settings, tpp, None)
    status_code = api.get_tpp_info(tpp).status_code
    assert status_code == 200, (
        f"[CITIZEN_STEP][CHECK_NEVER_ONBOARDED] Expected status code 404, got {status_code} instead."
    )


@when('an onboarding for {tpp} request arrives')
def step_onboarding_request(context, tpp):
    tpp = getattr(settings, tpp, None)
    payload = getattr(settings, "TppDTOCreationPayload", None)
    payload.tppId = tpp
    context.response = api.save_tpp(tpp)
    context.tpps.add(tpp)


@then('the onboarding request is successful')
def step_check_creation_ok(context):
    status_code = context.response.status_code
    assert status_code == 200, (
        f"[CITIZEN_STEP][GET_CONSENTS_LIST_SUCCESSFUL] Expected status code 200, got {status_code} instead."
    )


@then('the onboarding request fail')
def step_check_creation_fail(context):
    status_code = context.response.status_code
    assert status_code == 404, (
        f"[CITIZEN_STEP][GET_CONSENTS_LIST_SUCCESSFUL] Expected status code 200, got {status_code} instead."
    )
