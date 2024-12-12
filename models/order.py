from peewee import Model, ForeignKeyField, DateTimeField
from .db import db
from .user import User
from .product import Product

class Order(Model):
    
    # 貸し出し一覧の名前に代入
    user = ForeignKeyField(User, backref='orders')
    
    # 貸し出し一覧のアルバム名に代入
    product = ForeignKeyField(Product, backref='orders')
    
    # 貸し出した日付を表示
    order_date = DateTimeField()

    class Meta:
        database = db
