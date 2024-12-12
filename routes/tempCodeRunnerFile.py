from flask import Blueprint, send_file
from models import Order, Product
import matplotlib.pyplot as plt
import io


orders = Order.select()
for order in orders:
    print(Product.get(order.product).name, order.order_date)
    
# Blueprintの作成
album_units_sold_bp = Blueprint('product', __name__, url_prefix='/products')


# 円グラフ画像生成ルート
@orders.route('/ranking-chart.png')
def ranking_chart():
    ranking_data = get_ranking_data()  # ランキングデータを取得
    labels = list(ranking_data.keys())[:5]  # 上位5つを取得
    sizes = list(ranking_data.values())[:5]
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
    explode = [0.1 if i == 0 else 0 for i in range(len(labels))]  # 一位を目立たせる

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title('人気アルバムランキング')
    
    # 画像をバイナリデータに保存
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return send_file(img, mimetype='image/png')