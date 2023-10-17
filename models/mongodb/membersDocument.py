
from mongoengine import *

import json

class MembersDocument(Document):


    meta = {
        'abstract' : False,
        'allow_inheritance': True,
        'collection': "adhesion"
    }
    first_name = StringField(required=True)
    last_name=StringField(required=True)
    birth_date=DateTimeField(required=True)
    email=EmailField(required=True)
    address=StringField(required=True)
    zip_code=StringField(required=True)
    press_media_authorized=BooleanField(required=True)
    social_network_authorized=BooleanField(required=True)
    ecreadys_site_web_authorized=BooleanField(required=True)
    phone=StringField(required=True)
    payment=FloatField(required=True)
    receipt_url=URLField(required=True)
    adhesion_name=StringField(required=True)


    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)