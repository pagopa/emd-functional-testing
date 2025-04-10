import json

from conf import configuration

from api.payment_core   import PaymentCoreAPI

settings = configuration.settings

payment_core_api = PaymentCoreAPI()
citizen_fake = getattr(settings, "CitizenFake", None)


