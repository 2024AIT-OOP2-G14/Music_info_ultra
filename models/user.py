from peewee import Model, CharField, IntegerField, DateField
from .db import db

class User(Model):
    name = CharField()
    number = IntegerField()
    date = DateField()

    class Meta:
        database = db