from flask import Flask

from main.apis import api1

app = Flask(__name__)

# 分割先のコントローラー(Blueprint)を登録する
app.register_blueprint(api1.app)

# 起動する
if __name__ == "__main__":
    app.run()