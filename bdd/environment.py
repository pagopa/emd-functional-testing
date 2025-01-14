
import api.citizen as api_citizen
import api.tpp as api_tpp


def before_all(context):
    context.citizens = set()
    context.tpps = set()


def after_feature(context, feature):
    for citizen in context.citizens:
        api_citizen.delete_consents(citizen)
    context.citizens = set()
    for tpp in context.tpps:
        api_tpp.delete_tpp(tpp)
    context.tpps = set()

