from peewee import Model, CharField, DecimalField
from .db import db

class Product(Model):
    # アルバム名追加
    name = CharField()
    
    # 価格追加
    price = DecimalField()

    class Meta:
        # データベースに保存されていたデータを代入
        database = db