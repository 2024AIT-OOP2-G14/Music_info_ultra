from .user import user_bp
from .product import product_bp
from .order import order_bp
#from .album_units_sold import album_units_sold_bp

# Blueprintをリストとしてまとめる
blueprints = [
  user_bp,
  product_bp,
  order_bp,
  #album_units_sold_bp
]
