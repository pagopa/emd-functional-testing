import json
import random
import string

from conf import configuration

from api.message_core   import MessageCoreAPI
from api.tpp            import TppAPI
from api.citizen        import CitizenAPI


message_core_api = MessageCoreAPI()
tpp_api = TppAPI()
citizen_api = CitizenAPI()

settings = configuration.settings

