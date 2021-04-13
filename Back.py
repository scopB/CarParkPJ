from flask import Flask, request
from flask_pymongo import PyMongo
import bcrypt

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://192.168.1.12:27017/carpark'
mongo = PyMongo(app)

myCollection1 = mongo.db.park
myCollection2 = mongo.db.user

@app.route('/create', methods=['POST'])
def insert_one():
    data = request.json

    myCollection1.insert_one(data)
    return {'result': 'Created successfully'}


@app.route('/find_all', methods=['GET'])
def find():
    query = myCollection1.find()

    output = []

    for ele in query:
        output.append({
            "light": ele["light"],
            "car": ele["car"],
            "idName": ele["idName"]
        })
    return { "result" : output }

@app.route('/reset', methods=['POST'])
def reset():
    """DELETE all data in database"""
    myCollection1.delete_many({})
    return {'result':' Delete Successfully'}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='2222', debug=True)
