from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS
from register_validation import v_email, v_pass_match, v_pass
try:
    from keys import db
except:
    from os import environ
    db = environ.get('DB')

import jwt
import re, random, datetime, string
import bcrypt

app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = db
mongo = PyMongo(app)

# mZOj2cy8Jt0AxRM
# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoidHN1bmEyMjIxQGxpdmUuY29tIiwiZXhwIjoxNTU4MjE2Mzg2fQ.MLD2sKrLA0UvLhcbDn-A8e4Ms33C3ETMqUQnmsi1oMQ

class CustomerRouter:
    @staticmethod
    def get():
        customer = mongo.db.customers
        q_id = request.args.get('id', None)
        token = request.args.get('token')
        secret = request.args.get('secret')

        if q_id != None:
            try:
                data = jwt.decode(token, secret)
                
                customer_data = customer.find_one({"customer_id": q_id})

                compiled_token = data['user'].lower()
                compiled_payload = customer_data['email'].lower()

                if customer_data:
                    if compiled_payload == compiled_token:
                        output = {
                            "name": str(customer_data['first_name']) + " " + str(customer_data['last_name']),
                            "email": customer_data['email'],
                            "created_at": customer_data['created_at'],
                            "id": customer_data['customer_id'],
                            'is_admin': customer_data['admin']
                        }
                    else:
                        output = 'unauthorized'
                else:
                    output = 'no customer found'

                return jsonify({"data": output})
            except:
                return jsonify({"data": 'something gone wrong'})
        return jsonify({'data': "no id provided"}) 


    @staticmethod
    def post():
        customers = mongo.db.customers
        pw = request.json['password']
        hashed_pass = bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt(10))

        if(v_email(request.json['email']) and v_pass_match(request.json['password'], request.json['confirm_password']) and v_pass(request.json['password'])):
            customer_id = customers.insert_one({
                'first_name': request.json['first_name'],
                'last_name': request.json['last_name'],
                'email': request.json['email'],
                'password': hashed_pass,
                'admin': False,
                'created_at': datetime.datetime.now(),
                'customer_id': ''.join(
                    random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in
                    range(10)),
            })

            created_customer = customers.find_one({'_id': ObjectId(str(customer_id.inserted_id))})

            output = {
                'first_name': created_customer['first_name'],
                'last_name': created_customer['last_name'],
                'email': created_customer['email'],
                'created_at': created_customer['created_at'],
                'customer_id': created_customer['customer_id']
            }

            return jsonify({'data': output})
        else:
            return jsonify({'data': 'Something gone wrong.'})

    @staticmethod
    def log():
        customers = mongo.db.customers

        email = request.json['email']
        time = request.json['timer']
        compiled_email = re.compile('^' + email + '$', re.IGNORECASE)
        pw = request.json['password'].encode('utf-8')

        customer_data = customers.find_one({"email": compiled_email})

        if customer_data:
            test = bcrypt.hashpw(pw, customer_data['password']) == customer_data['password']
            if test:
                key = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(15))
                
                token = jwt.encode({
                    'user': email,
                    'id': customer_data['customer_id'],
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=time)
                }, key)

                return jsonify({'data': {
                    "token": token.decode('UTF-8'),
                    "secret": key,
                    'user': email,
                    'id': customer_data['customer_id'],
                    "expire_in": time
                }})

            else:
                return jsonify({'data': 'Invalid Password'})
        else:
            return jsonify({'data': 'Email not found'})

    @staticmethod
    def get_all():
        customers = mongo.db.customers
        token = request.args.get('token')
        secret = request.args.get('secret')
        customers_data = customers.find()

        try:
            data = jwt.decode(token, secret)
            current_user = customers.find_one({'email': re.compile('^' + data['user'] + '$', re.IGNORECASE)})
            output = []

            if current_user['admin'] == True:
                for customer in customers_data:
                    output.append({
                        "name": str(customer['first_name']) + " " + str(customer['last_name']),
                        "email": customer['email'],
                        "created_at": customer['created_at'],
                        "id": customer['customer_id'],
                        'is_admin': customer['admin']
                    })

                return jsonify({"data": output})
            return jsonify({"data": 'unauthorized. not an admin'})
        except:
            return jsonify({"data": 'invalid token or secret'})