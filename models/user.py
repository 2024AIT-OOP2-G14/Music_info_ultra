from peewee import Model, CharField, IntegerField, DateField
from .db import db

class User(Model):
    # 名前追加
    name = CharField()
    
    # 会員番号追加 (多分)
    number = IntegerField()
    
    # 日付追加
    date = DateField()

    class Meta:
        # データベースに保存されていたデータを代入
        database = db