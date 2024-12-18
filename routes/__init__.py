from .register_chart import register_bp
from .user import user_bp
from .product import product_bp
from .order import order_bp
from .mmc import mmc_bp
#from .album_units_sold import album_units_sold_bp
from .album_units_sold import ranking_bp  # すでに import 済み



# Blueprintをリストとしてまとめる
blueprints = [
  register_bp,
  user_bp,
  product_bp,
  order_bp,
  mmc_bp,
  #album_units_sold_bp
  ranking_bp  # 人気アルバムランキングの Blueprint を追加
]
