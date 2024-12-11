from behave import given, when, then
from config.configuration import secrets




@given("un payload TPP valido")
def step_given_payload_tpp_valido(context):
    context.tpp = {
        "tppId": secrets.tpp.tppId,
        "authenticationType": secrets.tpp.authenticationType,
        "authenticationUrl": secrets.tpp.authenticationUrl,
        "businessName": secrets.tpp.businessName,
        "contact": {
            "email": secrets.tpp.contact.email,
            "name": secrets.tpp.contact.name,
            "number": secrets.tpp.contact.number
        },
        "entityId": secrets.tpp.entityId,
        "idPsp": secrets.tpp.idPsp,
        "legalAddress": secrets.tpp.legalAddress,
        "messageUrl": secrets.tpp.messageUrl,
        "state": secrets.tpp.state,
        "tokenSection": {
            "bodyAdditionalProperties": {
                "client_id": secrets.tpp.tokenSectionDecrypted.client_id,
                "client_secret": secrets.tpp.tokenSectionDecrypted.client_secret,
                "grant_type": secrets.tpp.tokenSectionDecrypted.grant_type,
                "contentType": secrets.tpp.tokenSectionDecrypted.contentType
            }
        }
    }