import json

from behave import given
from behave import then
from behave import when
from conf.configuration import settings
from api.tpp import get_tpp
from api.citizen import get_consent, save_consent

#Steps can fail if in consent_creation.feature the scenario ar not sorted
@given('{tpp} is a valid tpp')
def step_check_tpp(tpp):
    status_code = get_tpp(tpp).status_code
    assert status_code == 200, (
        f"Expected status code 200, got {status_code} instead."
    )


@given('{citizen} not onboarded on {tpp}')
def step_check_not_onboarded(citizen, tpp):
    status_code = get_consent(citizen, tpp).status_code
    assert status_code != 200, (
        f"Expected status code 200, got {status_code} instead."
    )


@given('{citizen} onboarded on {tpp}')
def step_check_onboarded(citizen, tpp):
    status_code = get_consent(citizen, tpp).status_code
    assert status_code == 200, (
        f"Expected status code 200, got {status_code} instead."
    )


@given('a {citizen} onborded on {tppA} and not on {tppB}')
def step_check_onboarded_only_on_first(citizen, tpp_a, tpp_b):
    status_code = get_consent(citizen, tpp_a).status_code
    assert status_code == 200, (
        f"Expected status code 200, got {status_code} instead."
    )
    status_code = get_consent(citizen, tpp_b).status_code
    assert status_code != 200, (
        f"Expected status code 200, got {status_code} instead."
    )


@when('an onboarding for {citizen} on {tpp} request arrives')
def step_create_consent(context, citizen, tpp):
    context.tpp_enabled = tpp
    context.response = save_consent(citizen, tpp)


@then('the request is successful')
def step_request_successful(context):
    status_code = context.response.status_code
    consents = context.response_json["consents"]
    tc_date = consents[context.tpp_enabled]["tcDate"]["$date"]
    context.tc_date = tc_date
    assert status_code == 200, (
        f"Expected status code 200, got {status_code} instead."
    )



@then('the request is idempotent')
def step_request_idempotent(context):
    status_code = context.response.status_code
    consents = context.response_json["consents"]
    tc_date = consents[context.tpp_enabled]["tcDate"]["$date"]
    assert status_code == 200, (
        f"Expected status code 200, got {status_code} instead."
    )
    assert tc_date == context.tc_date, (
        f"Expected tc_date {context.tc_date}, got {tc_date} instead."
    )


@then('others onboarding are not visible')
def step_others_onboarding_are_not_visible(context):
    status_code = context.response.status_code
    consents = context.response_json["consents"]
    actual_key = list(consents.keys())[0]
    assert status_code == 200, (
        f"Expected status code 200, got {status_code} instead."
    )
    assert len(consents) == 1, f"Expected 1 key in 'consents', but found {len(consents)}."
    assert actual_key == context.tpp_enabled, f"Expected key '{context.tpp_enabled}', but found '{actual_key}'."
