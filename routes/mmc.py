from flask import Blueprint, render_template, request, redirect, url_for
from models import Order, User, Product


# Blueprintの作成
mmcgraph_bp = Blueprint('mmc_graph', __name__, url_prefix='http://127.0.0.1:8080/')

print("test")

# productID と userID のデータが必要

@mmcgraph_bp.route(methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        user_id = request.form['name']
        
        # modelsから価格を変数に代入
        money = request.form['price']
        
        print("--=====",money,"--=====")
        
        Order.create(user=user_id, money = money)
        
        return redirect(url_for('order.list'))
    users = User.select()
    moneys = Product.select()
    return render_template('order_add.html', users=users, products=moneys)

# @order_bp.route('/edit/<int:order_id>', methods=['GET', 'POST'])
# def edit(order_id):
#     order = Order.get_or_none(Order.id == order_id)
#     if not order:
#         return redirect(url_for('order.list'))

#     if request.method == 'POST':
#         order.user = request.form['user_id']
#         order.product = request.form['product_id']
#         order.save()
#         return redirect(url_for('order.list'))

#     users = User.select()
#     products = Product.select()
#     return render_template('order_edit.html', order=order, users=users, products=products)
