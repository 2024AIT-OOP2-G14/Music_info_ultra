from .register_chart import register_bp
from .user import user_bp
from .product import product_bp
from .order import order_bp

# Blueprintをリストとしてまとめる
blueprints = [
  register_bp,
  user_bp,
  product_bp,
  order_bp
]
