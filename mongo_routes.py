from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/add_user', methods=['POST'])
def add_user():
    client = MongoClient("mongodb://localhost:27017/")
    db = client['testdb']
    users = db['users']
    data = request.get_json()
    result = users.insert_one(data)
    client.close()
    return jsonify({'inserted_id': str(result.inserted_id)})

@app.route('/get_users', methods=['GET'])
def get_users():
    client = MongoClient("mongodb://localhost:27017/")
    db = client['testdb']
    users = db['users']
    user_list = list(users.find({}, {"_id": 0}))
    client.close()
    return jsonify(user_list)

if __name__ == '__main__':
    app.run(debug=True)
