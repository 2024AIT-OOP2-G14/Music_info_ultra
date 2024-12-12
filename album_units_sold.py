from models import Order, User, Product
orders = Order.select()
for order in orders:
    print(order.user, order.product, order.order_date)