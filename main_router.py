from flask import Flask, jsonify, request
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from flask_cors import CORS
import datetime, random, string
import pprint, re, math
try:
    from key import db
    print('success')
except:
    from os import environ
    db = environ.get('DB')

app = Flask(__name__)
CORS(app)
pp = pprint.PrettyPrinter(indent=4)
app.config["MONGO_URI"] = db
mongo = PyMongo(app)

class MainRouter:
    @staticmethod
    def get():
        categories = mongo.db.categories
        products = mongo.db.products


        featured_array = ['5PdIfemU', 'wcDhQthy', 'RzHCG1OU', 'xjtFVYnD']
        featured_output = []

        category_array = ['5PdIfemU', 'wcDhQthy', 'RzHCG1OU']
        category_output = []

        products_array = ['X8Ih01jg', 'xgAQftCx', 'O7zS1yEa', 'No4DCewt', 'Z84nnUdC']
        products_output =  []

        for cat in category_array:
            data = categories.find_one({'cid': cat})
            category_output.append({
                'id': data['cid'],
                'label': data['category_name'],
                'href': "/c/" + data['category_name'].replace(" ", "-"),
                'image': 'https://res.cloudinary.com/db5msl9ld/image/upload/v1558215818/category_image/' + data['cid'] + '.png'
            })

        for fet in featured_array:
            data = categories.find_one({'cid': fet})
            featured_output.append({
                'id': data['cid'],
                'name': data['category_name'],
                'href': "/c/" + data['category_name'].replace(" ", "-")
            })

        for pro in products_array:
            data = products.find_one({'pid': pro})
            products_output.append({
                'id': data['pid'],
                'title': data['title'],
                'price': data['price'],
                'price_percentage': data['price_percentage'],
                'rating': data['about']['rating'],
                'image': data['images'][0]
            })

        output = {
            "trend": {
                "product": products_output,
                "category": category_output,
            },
            "featured_categories": featured_output,
            "banners": [
                "https://picsum.photos/id/1005/1920/444",
                "https://picsum.photos/id/1/1920/444",
                "https://picsum.photos/id/2/1920/444",
                "https://picsum.photos/id/3/1920/444",
                "https://picsum.photos/id/4/1920/444"
            ],
        }

        return jsonify({"data": output}) 