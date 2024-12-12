from models import Order, User, Product
orders = Order.select()
for order in orders:
    print(Product.get(order.product).name, order.order_date)