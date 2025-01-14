
import api.citizen as api_citizen


def before_all(context):
    context.citizens = set()


def after_feature(context, feature):
    for citizen in context.citizens:
        api_citizen.delete_consents(citizen)
    context.citizens = set()

