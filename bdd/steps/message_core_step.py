import json
from behave import given
from behave import then
from behave import when
from conf.configuration import settings
from api.message_core import send_messge


@given('{citizen not onboarded on {TppA}')
def step_build_message(context, citizen):
    context.message = json.dumps({
        "messageId": "1234567890",
        "recipientId": getattr(settings, citizen, None),
        "triggerDateTime": "2024-06-21T12:34:56Z",
        "senderDescription": "Comune di Pontecagnano",
        "messageUrl": "https://www.google.com",
        "message": "Nuova notifica",
        "originId": "origindId",
        "associatedPayment": True
    })


@when('a notification request arrives')
def step_notification_request(context):
    context.response = send_messge(context.message)


@then('the response status must be {status_code}')
def step_check_status_code(context, status_code):
    assert context.response.status_code == int(status_code), (
        f"Expected status code {status_code}, got {context.response.status_code} instead."
    )


@then('the answer must be {message_response}')
def step_check_message_response(context, message_response):
    assert context.response.text == message_response, (
        f"Expected message response {message_response}, got {json.loads(context.response.text)['message']} instead."
    )
