import json

from behave import given
from behave import then
from behave import when
from api.payment_core import PaymentCoreAPI
from api.tpp import TppAPI
from conf.configuration import settings

payment_core_api = PaymentCoreAPI()
tpp_api = TppAPI()

@given('the user decide to make a payment for TPP {tpp_name} and has chosen an agent {agent}')
def step_make_payment(context, tpp_name, agent):
    tpp_name = getattr(settings, tpp_name, None)
    agent = getattr(settings, agent, None)
    context.tpp_name = tpp_name
    context.agent = agent

@when('the user sends a payment request with the entity id {entity_id} and selected an agent {agent} and origin {origin_id}')
def step_check_not_onboarded(context, entity_id, agent, origin_id):
    entity_id = getattr(settings, entity_id, None)
    origin_id = getattr(settings, origin_id, None)

    response = tpp_api.get_tpp_by_entity_id(entity_id)

    context.entity_id = entity_id
    context.origin_id = origin_id
    context.response_get_tpp_by_entity_id = response

@then('if the tpp is valid, the system will returns a 200 OK')
def step_check_tpp_valid(context):
    assert context.response_get_tpp_by_entity_id.status_code == 200

@then('if the tpp is not valid, the system will returns a 404')
def step_check_tpp_not_valid(context):
    assert context.response_get_tpp_by_entity_id.status_code == 404

@then('if the agent is valid, the system will returns a 200 OK')
def step_check_agent_and_origin(context):
    payload = json.dumps({
        "agent": context.agent,
        "originId": context.origin_id
    })
    if context.tpp_name == "Fucino":
        token = "token_banca_del_fucino"
    response = payment_core_api.retrieval_tokens(payload, token)
    assert response.status_code == 200
    response_data = response.json()
    context.retrieval_token = response_data['retrievalId']
    context.retrieval_tokens = response

@then('if the agent is not valid, the system will returns a 404')
def step_check_agent_and_origin(context):
    payload = json.dumps({
        "agent": context.agent,
        "originId": context.origin_id
    })
    if context.tpp_name == "Fucino":
        token = "token_banca_del_fucino"
    response = payment_core_api.retrieval_tokens(payload, token)
    assert response.status_code == 404

@then('if both checks pass, the system creates a "Payment Attempt"')
def step_check_payment_attempt(context):
    assert context.retrieval_tokens.status_code == 200 and context.response_get_tpp_by_entity_id.status_code == 200


@then('the user with fiscal code {fiscal_code} and notice number {notice_number} is redirected to the destination link')
def step_check_redirect(context,fiscal_code,notice_number):
    fiscal_code = getattr(settings, fiscal_code, None)
    notice_number = getattr(settings, notice_number, None)

    response = payment_core_api.get_token(context.retrieval_token)
    response_data = response.json()
    params = {
        'retrievalId': response_data['retrievalId'],
        'fiscalCode': fiscal_code,
        'noticeNumber': notice_number
    }
    redirect = payment_core_api.generate_deep_link(params)

    assert redirect.status_code != 500