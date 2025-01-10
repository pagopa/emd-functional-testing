import json

from behave import given
from behave import then
from behave import when
from conf.configuration import settings
from api.tpp import get_tpp
from api.citizen import get_consent, save_consent


# Steps can fail if in consent_creation.feature the scenario ar not sorted
@given('{tpp} is a valid tpp')
def step_check_tpp(context, tpp):
    tpp = getattr(settings, tpp, None)
    status_code = get_tpp(tpp).status_code
    assert status_code == 200, (
        f"[CITIZEN_STEP][CHECK_TPP]Expected status code 200, got {status_code} instead."
    )


@given('{citizen} not onboarded on {tpp}')
def step_check_not_onboarded(context, citizen, tpp):
    citizen = getattr(settings, citizen, None)
    tpp = getattr(settings, tpp, None)
    status_code = get_consent(citizen, tpp).status_code
    assert status_code == 404, (
        f"[CITIZEN_STEP][CHECK_NOT_ONBOARDED] Expected status code 404, got {status_code} instead."
    )


@given('{citizen} already onboarded on {tpp}')
def step_check_onboarded(context, citizen, tpp):
    citizen = getattr(settings, citizen, None)
    tpp = getattr(settings, tpp, None)
    status_code = get_consent(citizen, tpp).status_code
    assert status_code == 200, (
        f"[CITIZEN_STEP][CHECK_ONBOARDED]Expected status code 200, got {status_code} instead."
    )

@given('{citizen} onboarded on {tpp_a} and not on {tpp_b}')
def step_check_onboarded_only_on_first(context, citizen, tpp_a, tpp_b):
    citizen = getattr(settings, citizen, None)
    tpp_a = getattr(settings, tpp_a, None)
    status_code = get_consent(citizen, tpp_a).status_code
    assert status_code == 200, (
        f"[CITIZEN_STEP][CHECK_ONBOARDED_ON_FIRST]Expected status code 200, got {status_code} instead."
    )
    tpp_b = getattr(settings, tpp_b, None)
    status_code = get_consent(citizen, tpp_b).status_code
    assert status_code != 200, (
        f"[CITIZEN_STEP][CHECK_ONBOARDED_ON_SECOND]Expected status code 200, got {status_code} instead."
    )


@when('an onboarding for {citizen} on {tpp} request arrives')
def step_create_consent(context, citizen, tpp):
    tpp = getattr(settings, tpp, None)
    citizen = getattr(settings, citizen, None)
    context.tpp_enabled = tpp
    context.response = save_consent(citizen, tpp)


@then('the request is successful')
def step_request_successful(context):
    status_code = context.response.status_code
    response_data = context.response.json()
    consents = response_data.get("consents")
    #The tc_date format on db is yyyy-MM-dd'T'HH:mm:ss.SSS so we use [:-6] to force that format
    tc_date = consents[context.tpp_enabled]['tcDate'][:-6]
    setattr(settings, 'tc_date', tc_date)
    assert status_code == 200, (
        f"[CITIZEN_STEP][REQUEST_SUCCESSFUL] Expected status code 200, got {status_code} instead."
    )


@then('the request is idempotent')
def step_request_idempotent(context):
    status_code = context.response.status_code
    response_data = context.response.json()
    consents = response_data.get("consents")
    tc_date = consents[context.tpp_enabled]['tcDate']
    print(f'response {response_data}')
    print(f'tc_saved att {getattr(settings, "tc_date", None)}')
    print(f'tc_saved response {tc_date}')
    assert status_code == 200, (
        f"[CITIZEN_STEP][REQUEST_IDEMPOTENT] Expected status code 200, got {status_code} instead."
    )
    assert tc_date == getattr(settings,'tc_date',None), (
        f"[CITIZEN_STEP][REQUEST_IDEMPOTENT] Expected tc_date {getattr(settings,'tc_date',None) }, got {tc_date} instead."
    )


@then('others onboarding are not visible')
def step_others_onboarding_are_not_visible(context):
    response_data = context.response.json()
    consents = response_data.get("consents")
    actual_key = list(consents.keys())[0]
    assert len(consents) == 1,(
        f"[CITIZEN_STEP][OTHER_ONBOARDING_NOT_VISIBLE] Expected 1 key in 'consents', but found {len(consents)}."
    )
    assert actual_key == context.tpp_enabled,(
        f"[CITIZEN_STEP][OTHER_ONBOARDING_NOT_VISIBLE] Expected key '{context.tpp_enabled}', but found '{actual_key}'."
    )
