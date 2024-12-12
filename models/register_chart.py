from peewee import Model, IntegerField
from .db import db

class register_chart(Model):
    member = IntegerField()

    class Meta:
        database = db