from flask import Flask, render_template
from models import initialize_database
from routes import blueprints
from routes.mmc import get_user_summary

app = Flask(__name__)

# データベースの初期化
initialize_database()

# 各Blueprintをアプリケーションに登録
for blueprint in blueprints:
    app.register_blueprint(blueprint)

# ホームページのルート
@app.route('/')
def index():
    user_data = get_user_summary()
    #デバック用print
    print("--------------------------------")
    print(user_data)

    return render_template('index.html', chart_data=user_data)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
