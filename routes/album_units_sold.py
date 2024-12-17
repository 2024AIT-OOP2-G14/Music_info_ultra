from flask import Flask, Blueprint, send_file
from peewee import fn
import matplotlib
import matplotlib.pyplot as plt
import io
from models import Order, Product


matplotlib.use('Agg')
def get_ranking_data():
    # アルバムごとの販売数を格納するリスト
    album_counts = []

    # 注文テーブルとアルバムテーブルを結合し、アルバムごとの販売数を取得するクエリ
    order_albums = (Order.select(Order.product, fn.COUNT(Order.id).alias('count'))
            .join(Product).group_by(Order.product))

    # アルバムごとの販売数を取得
    for order in order_albums:
        # アルバム名を取得
        product_name = Product.get(Product.id == order.product).name
        # アルバム名と販売数をタプルでリストに追加
        album_counts.append((product_name, order.count))

    # 販売数の降順にソート
    album_counts.sort(key=lambda x: x[1], reverse=True)
    # リストを辞書に変換
    album_counts = dict(album_counts)
    # 人気アルバムランキングを返す
    return album_counts

# Blueprint の作成
ranking_bp = Blueprint('ranking', __name__, url_prefix='/ranking')

# 円グラフ画像生成ルート
@ranking_bp.route('/ranking-chart.png')
def ranking_chart():
    ranking_data = get_ranking_data()  # ランキングデータを取得
    labels = list(ranking_data.keys())  # アルバム名
    sizes = list(ranking_data.values())  # 注文数
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


# Flask アプリの作成
app = Flask(__name__)
app.register_blueprint(ranking_bp)

if __name__ == '__main__':
    app.run(debug=True)