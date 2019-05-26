from flask import Flask, jsonify, request, make_response
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS
from functools import wraps
import datetime, random, string
import jwt
try:
    from keys import db
except:
    from os import environ
    db = environ.get('DB')

from products_router import ProductsRouter
from categories_router import CategoriesRouter
from customer_router import CustomerRouter
from main_router import MainRouter

app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = db
mongo = PyMongo(app)

customer = CustomerRouter
products = ProductsRouter
categories = CategoriesRouter
main = MainRouter

#secret = rZP0y2lg5A61NtC
#token = eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoidHN1bmEyMjIxQGxpdmUuY29tIiwiZXhwIjoxNTU3OTMyMDEyfQ.jEK3vz4YnMgTpkxvCUpN0YPr1wVnGaMr5P1YBQWouw8

#2 = qKMMY7ccxrWX515
#2 = eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiZG9lSm9obkBnbWFpbC5jb20iLCJleHAiOjE1NTc5MzgxNTF9.jvKZ43dj9oSt7WWHbENiHc3PL_qBH3R09vOci9sKbXQ

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        secret = request.args.get('secret')

        if token:
            if secret:
                try:
                    jwt.decode(token, secret)
                    
                    return f(*args, **kwargs)
                except:
                    return jsonify({"data": 'invalid token or secret'})
            return jsonify({"data": 'no secret provided'})
        return jsonify({"data": 'no token provided'})
    return decorated


@app.route('/', methods=['GET'])
def get_main_data():
    return main.get()

@app.route('/products', methods=['GET'])
def get_products():
    return products.get()

@app.route('/products/insert', methods=['POST'])
def post_product():
    return products.post()

@app.route('/products/delete/<pid>', methods=['DELETE'])
def delete_test(pid):
    return products.delete(pid)

@app.route('/categories', methods=['GET'])
def get_categories():
    return categories.get()

@app.route('/categories/insert', methods=['POST'])
def post_category():
    return categories.post()
    
@app.route('/customer', methods=['GET'])
@token_required
def get_customer():
    return customer.get()

@app.route('/customer/all', methods=['GET'])
@token_required
def get_all_customers():
    return customer.get_all()

@app.route('/customer/insert', methods=['POST'])
def post_customer():
    return customer.post()

@app.route('/customer/login', methods=['POST'])
def log_customer():
    return customer.log()


# @app.route('/update', methods=['GET'])
# def update_admin():
#     c = mongo.db.customers

#     d = c.find()

#     for a in d:
#         c.update_one({'customer_id': a['customer_id']}, {'$set': {"admin": False}})

#     return ':D'


if __name__ == '__main__':
    app.run(debug=True)

