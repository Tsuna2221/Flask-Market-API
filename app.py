from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS
from products_router import ProductsRouter
from categories_router import CategoriesRouter
from keys import db
import datetime, random, string
import pprint

app = Flask(__name__)
CORS(app)
pp = pprint.PrettyPrinter(indent=4)
app.config["MONGO_URI"] = db
mongo = PyMongo(app)
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



if __name__ == '__main__':
    app.run(debug=True)

