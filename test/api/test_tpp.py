import json

from conf import configuration

from api.tpp   import TppAPI


tpp_api = TppAPI()

settings = configuration.settings

payload = getattr(settings, "TppDtoFake", None)
tpp_fake_a_id = getattr(settings, "TppFakeEntityIdA", None)
payload.entityId = tpp_fake_a_id
