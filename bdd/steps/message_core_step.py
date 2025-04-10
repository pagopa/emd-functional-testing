import json
import random
import string

from behave import given
from behave import then
from behave import when
from conf import configuration

from api.message_core import MessageCoreAPI

message_core_api = MessageCoreAPI()

settings = configuration.settings

@given('a message for the {citizen}')
def step_build_message(context, citizen):
    context.message = json.dumps({
        "messageId": generate_random_id(),
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
    context.response = message_core_api.send_message(context.message)


@then('the response status must be {status_code}')
def step_check_status_code(context, status_code):
    assert context.response.status_code == int(status_code), (
        f"Expected status code {status_code}, got {context.response.status_code} instead."
    )


@then('the answer must be {message_response}')
def step_check_message_response(context, message_response):
    assert context.response.json().get("outcome") == message_response, (
        f"Expected message response {message_response}, got {json.loads(context.response)['outcome']} instead."
    )

def generate_random_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
