from django.db import models
from MangoEngine import *
# ORM
# Create your models here.

class ArtiInfo(Document):
    des = StringField()
    title = StringField()
    scores = StringField()
    tags = ListField()

    meta = {
        'collection':'arti_info3'
    }



