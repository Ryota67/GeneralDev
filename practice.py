from flask import Flask, request, jsonify
app = Flask(__name__)

messages = []

# C : Create
@app.route('/v1/create', methods=['GET'])
def create():
    messages = [{"name": "me", "message": "My name is Hamada"}]
    return jsonify(messages)

# R : Read
@app.route('/v1/read', methods=['GET'])
def read():
    return jsonify(messages)

# U : Update
@app.route('/v1/update', methods=['GET'])
def update():
    message = {"name": "me", "message": "update"}
    messages.append(message)
    return jsonify(messages)

# D : Delete
@app.route('/v1/delete', methods=['GET'])
def delete():
    del messages[-1]   # 末尾のメッセージ
    return jsonify(messages)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 8080)   # ポート番号を開けておく