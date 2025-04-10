import json
from unittest.mock import patch, MagicMock
from bdd.steps import payment_core_step



@patch('bdd.steps.payment_core_step.settings')
def test_step_make_payment(mock_settings):
    mock_settings.TppFake = "mocked-tpp-fake"
    mock_settings.AgentFake = "mocked-agent-fake"

    context = MagicMock()
    payment_core_step.step_make_payment(context,"TppFake", "AgentFake")

@patch('bdd.steps.payment_core_step.settings')
@patch('bdd.steps.payment_core_step.tpp_api.get_tpp_by_entity_id')
def test_step_check_not_onboarded(mock_get_tpp_by_entity_id, mock_settings):
    mock_settings.EntityIdFake = "mocked-entity-id-fake"
    mock_settings.OriginIdFake = "mocked-origin-id-fake"

    mock_response_1 = MagicMock()
    mock_response_1.json.return_value = {"tppId": "mocked-tpp-id"}
    mock_get_tpp_by_entity_id.return_value = mock_response_1

    context = MagicMock()
    payment_core_step.step_check_not_onboarded(context,"EntityIdFake", "AgentIdFake", "OriginIdFake")

    mock_get_tpp_by_entity_id.assert_called_once_with('mocked-entity-id-fake')

def test_step_check_tpp_valid():
    context = MagicMock()
    context.response_get_tpp_by_entity_id.status_code = 200
    payment_core_step.step_check_tpp_valid(context)

def test_step_check_tpp_not_valid():
    context = MagicMock()
    context.response_get_tpp_by_entity_id.status_code = 404
    payment_core_step.step_check_tpp_not_valid(context)

@patch('bdd.steps.payment_core_step.payment_core_api.retrieval_tokens')
def test_step_check_agent_and_origin_ok(mock_retrieval_tokens):
    context = MagicMock()
    context.agent = "mocked-agent-id-fake"
    context.origin_id = "mocked-origin-id-fake"
    context.tpp_name = "TppNameA"


    mock_response_1 = MagicMock()
    mock_response_1.json.return_value = {"retrievalId": "mocked-retrieval-id"}
    mock_response_1.status_code = 200
    mock_retrieval_tokens.return_value = mock_response_1

    payment_core_step.step_check_agent_and_origin_ok(context)

    payload = json.dumps({
        "agent":  "mocked-agent-id-fake",
        "originId": "mocked-origin-id-fake"
    })
    mock_retrieval_tokens.assert_called_once_with(payload, "token_emd_tpp_test")


@patch('bdd.steps.payment_core_step.payment_core_api.retrieval_tokens')
def test_step_check_agent_and_origin_not_ok(mock_retrieval_tokens):
    context = MagicMock()
    context.agent = "mocked-agent-id-fake"
    context.origin_id = "mocked-origin-id-fake"
    context.tpp_name = "TppNameA"


    mock_response_1 = MagicMock()
    mock_response_1.json.return_value = {"retrievalId": "mocked-retrieval-id"}
    mock_response_1.status_code = 404
    mock_retrieval_tokens.return_value = mock_response_1

    payment_core_step.step_check_agent_and_origin_not_ok(context)

    payload = json.dumps({
        "agent":  "mocked-agent-id-fake",
        "originId": "mocked-origin-id-fake"
    })
    mock_retrieval_tokens.assert_called_once_with(payload, "token_emd_tpp_test")


def test_step_check_payment_attempt():
    context = MagicMock()
    context.retrieval_tokens.status_code = 200
    context.response_get_tpp_by_entity_id.status_code = 200
    payment_core_step.step_check_payment_attempt(context)


@patch('bdd.steps.payment_core_step.settings')
@patch('bdd.steps.payment_core_step.payment_core_api.get_token')
@patch('bdd.steps.payment_core_step.payment_core_api.generate_deep_link')
def test_step_check_redirect(mock_generate_deep_link, mock_get_token, mock_settings):
    mock_settings.fiscal_code = "mocked-fiscal-code-fake"
    mock_settings.notice_number = "mocked-notice-number-fake"

    context = MagicMock()

    mock_response_1 = MagicMock()
    mock_response_1.json.return_value = {"retrievalId": "mocked-retrieval-id"}
    mock_get_token.return_value = mock_response_1

    payment_core_step.step_check_redirect(context,"fiscal_code","notice_number")

    params = {
        'retrievalId': "mocked-retrieval-id",
        'fiscalCode': "mocked-fiscal-code-fake",
        'noticeNumber': "mocked-notice-number-fake"
    }
    mock_generate_deep_link.assert_called_once_with(params)

