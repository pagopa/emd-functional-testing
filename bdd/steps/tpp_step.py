import json

from behave import given
from behave import then
from behave import when
from conf import configuration

from api.tpp import TppAPI

tpp_api = TppAPI()

settings = configuration.settings

@given('{tpp} not onboarded')
def step_check_not_onboarded(context, tpp):
    entity_id = getattr(settings, tpp, None)
    status_code = tpp_api.get_tpp_by_entity_id(entity_id).status_code
    assert status_code == 404


@given('{tpp} already onboarded')
def step_check_already_onboarded(context, tpp):
    entity_id = getattr(settings, tpp, None)
    response = tpp_api.get_tpp_by_entity_id(entity_id)
    assert response.status_code == 200


@when('an onboarding for {tpp} request arrives')
def step_onboarding_request(context, tpp):
    entity_id = getattr(settings, tpp, None)
    payload = getattr(settings, "TppDtoFake", None)
    payload["entityId"] = entity_id
    context.response = tpp_api.save_tpp(json.dumps(payload))
    if "tppId" in context.response.json():
        context.tpps["tpp_fake"] = context.response.json()


@when('an updating for {tpp} request arrives')
def step_update_request(context, tpp):
    entity_id = getattr(settings, tpp, None)
    response = tpp_api.get_tpp_by_entity_id(entity_id)
    tpp_id = response.json().get('tppId')
    payload = getattr(settings, "TppDtoFake", None)
    payload["tppId"] = tpp_id
    context.response = tpp_api.update_tpp(json.dumps(payload))
    context.tpps["tpp_fake"] = context.response.json()

@when('an change state for {tpp} request arrives')
def step_change_request(context, tpp):
    tpp = getattr(settings, tpp, None)
    response = tpp_api.get_tpp_by_entity_id(tpp)
    tpp_id = response.json().get("tppId")
    payload = {
            'tppId': tpp_id,
            'state': True
        }
    context.response = tpp_api.update_status_tpp(json.dumps(payload))


@then('the onboarding request is successful')
def step_check_creation_ok(context):
    assert context.response.status_code == 200

@then('the changing request is successful')
def step_check_changing_ok(context):
    assert context.response.status_code == 200

@then('the onboarding request fail')
def step_check_creation_fail(context):
    assert context.response.status_code == 403
