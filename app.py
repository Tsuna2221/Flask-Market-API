from flask import Flask, jsonify, request, make_response
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS
from keys import db
import jwt

from products_router import ProductsRouter
from categories_router import CategoriesRouter
from customer_router import CustomerRouter

import datetime, random, string

app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = db
mongo = PyMongo(app)

customer = CustomerRouter
products = ProductsRouter
categories = CategoriesRouter

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
def get_customer():
    return customer.get()

@app.route('/customer/insert', methods=['POST'])
def post_customer():
    return customer.post()

@app.route('/customer/login', methods=['POST'])
def log_customer():
    return customer.log()



if __name__ == '__main__':
    app.run(debug=True)

