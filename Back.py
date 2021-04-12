from flask import Flask, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://192.168.1.5:27017/carpark'
mongo = PyMongo(app)

myCollection1 = mongo.db.park
myCollection2 = mongo.db.user

post1 = {"light":0, "car":0,"idName" : 1}
post2 = {"name":"Bas", "Password": "1234"}

# myCollection.delete_one({})
myCollection1.insert_one(post1)
myCollection2.insert_one(post2)
