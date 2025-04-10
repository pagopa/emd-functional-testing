import json

from api.tpp import TppAPI
from api.citizen import CitizenAPI
from conf import configuration

tpp_api = TppAPI()
citizen_api = CitizenAPI()

settings = configuration.settings

def before_feature(context, feature):
    context.citizens = {}
    context.tpps = {}
    payload = getattr(settings, "TppDtoFake", None)
    tpp_fake_a_id = getattr(settings, "TppFakeEntityIdA", None)
    tpp_fake_b_id = getattr(settings, "TppFakeEntityIdB", None)
    tpp_fake_c_id = getattr(settings, "TppFakeEntityIdC", None)
    tpp_fake_d_id = getattr(settings, "TppFakeEntityIdD", None)

    payload.entityId = tpp_fake_a_id
    response = tpp_api.save_tpp(json.dumps(payload))
    context.tpps["tpp_fake_a"] = response.json()

    payload.entityId = tpp_fake_b_id
    response = tpp_api.save_tpp(json.dumps(payload))
    context.tpps["tpp_fake_b"] = response.json()

    payload.entityId = tpp_fake_c_id
    response = tpp_api.save_tpp(json.dumps(payload))
    context.tpps["tpp_fake_c"] = response.json()

    payload.entityId = tpp_fake_d_id
    payload.state = False
    response = tpp_api.save_tpp(json.dumps(payload))
    context.tpps["tpp_fake_d"] = response.json()
    citizen_s = getattr(settings, "CitizenS", None)
    tpp_id = response.json()["tppId"]
    response = citizen_api.save_consent(citizen_s,tpp_id)
    context.citizens[citizen_s] = response.json()


def after_feature(context, feature):
    for value in context.citizens.values():
        citizen_api.delete_consents(str(value["fiscalCode"]))
    context.citizens = {}
    for value in context.tpps.values():
        tpp_api.delete_tpp(str(value["tppId"]))
    context.tpps = {}
