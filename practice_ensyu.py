from flask import Flask, request, jsonify
app = Flask(__name__)

messages = []

# C : Create
@app.route('/v1/create', methods=['①'])  # URLとHTTPメソッドを指定
def create():
    messages = [{"name": "me", "message": "My name is Hamada"}]
    return ②  # json形式でレスポンス

# R : Read
@app.route('/v1/read', methods=['①'])
def read():
    return ②

# U : Update
@app.route('/v1/update', methods=['①'])
def update():
    message = {"name": "me", "message": "update"}
    ③  # メッセージを追加
    return ②

# D : Delete
@app.route('/v1/delete', methods=['①'])
def delete():
    ④   # 末尾のメッセージを削除
    return ②

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 8080)   # ポート番号を開けておく