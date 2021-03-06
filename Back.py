from flask import Flask, request
from flask_pymongo import PyMongo
import bcrypt
from flask_cors import CORS, cross_origin
# import bcrypt


app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://192.168.1.4:27017/carpark'
mongo = PyMongo(app)

myCollection1 = mongo.db.park
myCollection2 = mongo.db.user

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={
    r"/": {
        "origins": "*",
        "allow_headers": '*'
    }
})


########################################### GET IN DB USER SYS ############################################

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



################################################## USER ##################################################

@app.route('/register', methods=['POST'])
@cross_origin()
def insert_one():
    data = request.json
    passs = data['passwd'].encode()
    hashed = bcrypt.hashpw(passs, bcrypt.gensalt())
    hashed = hashed.decode()
    myCollection2.insert_one({'username':data['username'],'passwd': hashed })
    init()
    return {'result': 'Created User successfully'}


@app.route('/find_alluser',methods=['GET'])
@cross_origin()
def uuasdasd():
    recon = myCollection2.find()
    output = []
    for i in recon:
        output.append({
            "username": i["username"],
            "passwd": i["passwd"]
        })
    return { "result" : output }


@app.route('/find_user',methods=['POST'])
@cross_origin()
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


################################################# PARK ############################################

@app.route('/create', methods=['POST'])
@cross_origin()
def insert_oneone():
    data = request.json
    myCollection1.insert_one(data)
    return {'result': 'Created successfully'}


@app.route('/find_all', methods=['GET'])
@cross_origin()
def find():
    query = myCollection1.find()

    output = []

    for ele in query:
        output.append({
            "light": ele["light"],
            "idName": ele["idName"]
        })

    return { "result" : output }

@app.route('/update_light', methods=['POST'])
@cross_origin()
def update_one():
    data = request.json
    name = data['idName']
    data2 = myCollection1.find({'idName': name})
    for i in data2:
        if i['light'] == 0:
            newvalues = { "$set": { 'light': 1 } }
            myCollection1.update_one({'idName': name},newvalues)
            return {'result':1}
        else :
            return {'result':0}
        
    
########################################### HARDWARE #########################################

@app.route('/light_status',methods=['GET'])
@cross_origin()
def lightha():
    data = request.args.get('idName')
    query = myCollection1.find({'idName':data})
    for i in query:
        if i['light'] == 1:
            return {'light': 1}
        else:
            return {'light' : 0}
    return {'light':'error'}


@app.route('/light_hard',methods=['POST'])
@cross_origin()
def lightupup():
    data = request.json
    name = data['idName']
    data2 = myCollection1.find({'idName': name})
    for i in data2:
        if i['light'] == 0:
            newvalues = { "$set": { 'light': 1 } }
            myCollection1.update_one({'idName': name},newvalues)
            return {'result':'update to 1'}
        else :
            newvalues = { "$set": { 'light': 0 } }
            myCollection1.update_one({'idName': name},newvalues)
            return {'result':'update to 0'}


########################################### RESET ############################################

@app.route('/reset_user', methods=['POST'])
@cross_origin()
def reset():
    """DELETE all data in database"""
    myCollection2.delete_many({})
    return {'result':' Delete User Successfully'}



@app.route('/reset_park', methods=['POST'])
@cross_origin()
def resetasd():
    """DELETE all data in database"""
    myCollection1.delete_many({})
    return {'result':' Delete Park Successfully'}




if __name__ == "__main__":
    app.run(host='0.0.0.0', port='2222', debug=True)




