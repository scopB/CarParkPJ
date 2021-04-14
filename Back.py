from flask import Flask, request
from flask_pymongo import PyMongo
from bson.json_util import loads, dumps
import bcrypt
# import bcrypt


app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://192.168.1.10:27017/carpark'
mongo = PyMongo(app)

myCollection1 = mongo.db.park
myCollection2 = mongo.db.user

class user_c:
    def __init__(self,username,passwd):
        self.username = username
        self.passwd = passwd
    def get_json(self):
        return {'username':self.username,'passwd':self.passwd}

user = {}

def init():
    query = myCollection2.find()
    for i in query:
        if i['username'] not in user:
            user[i['username']]=user_c(i['username'],i['passwd'])

init()

# @app.route('/create', methods=['POST'])
# def insert_one():
#     data = request.json

#     myCollection1.insert_one(data)
#     return {'result': 'Created successfully'}

@app.route('/register', methods=['POST'])
def insert_one():
    data = request.json
    passs = data['passwd'].encode()
    hashed = bcrypt.hashpw(passs, bcrypt.gensalt())
    hashed = hashed.decode()
    myCollection2.insert_one({'username':data['username'],'passwd': hashed })
    return {'result': 'Created successfully'}

@app.route('/find_alluser',methods=['GET'])
def uuasdasd():
    recon = myCollection2.find()
    output = []
    for i in recon:
        output.append({
            "username": i["username"],
            "passwd": i["passwd"]
        })
    return { "result" : output }

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

@app.route('/find_user',methods=['POST' , 'GET'])
def fiuser():
    data = request.json
    if data['username'] in user:
        name = data['username']
        password = data['passwd']
        data2 = myCollection2.find({'username': name})
        output = []
        for i in data2:
            check = i['passwd']
            output.append({
            "username": i["username"],
            "passwd": i["passwd"],
        })
        # return {'result': check}
        check = check.encode()
        password = password.encode()
        if bcrypt.checkpw(password, check ):
            return {'result':1}
        else:
            return {'result':2}
    else:
        return {'result':0}


@app.route('/reset', methods=['POST'])
def reset():
    """DELETE all data in database"""
    myCollection2.delete_many({})
    return {'result':' Delete Successfully'}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='2222', debug=True)
