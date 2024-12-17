from flask import Blueprint, render_template, jsonify
from models import User, Product, Order
from peewee import fn

mmc_bp = Blueprint('mmc', __name__, template_folder='templates')

def get_user_summary():
    user_total = (
        Order
        .select(
            Order.user_id.alias('user_id'),  # ユーザーIDの取得
            fn.SUM(Product.price).alias('total')
        )
        .join(Product)
        .group_by(Order.user_id)
        .order_by(fn.SUM(Product.price).desc())
    )  # ここでトータルの計算

    user_data = [
        {
            'user': User.get(User.id == purchase.user_id).name,  # ユーザー名の取得
            'total_amount': purchase.total
        } for purchase in user_total
    ]
    # print("--------------------------------")
    return user_data
