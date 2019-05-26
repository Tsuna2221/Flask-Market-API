from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS
from setCategoryOutput import CategoryOutput
import datetime, random, string
import pprint, re
try:
    from keys import db
except:
    from os import environ
    db = environ.get('DB')
    
app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = db
mongo = PyMongo(app)

class CategoriesRouter:
    @staticmethod
    def get():
        category_list = []
        total_products = []
        valid_parameters = {}

        query_list = [
            {
                'key': 'category_name',
                'value': re.compile('^' + request.args.get('category', 'None') + '$', re.IGNORECASE)
            },
            {
                'key': 'cid',
                'value': request.args.get('id', 'None')
            }
        ]

        for item in query_list:
            if 'None' not in str(item['value']):
                valid_parameters.update({item['key']: item['value']})

        output = CategoryOutput(valid_parameters).setOutput()

        return jsonify({'data': output, 'total_categories': len(output)})

    @staticmethod
    def post():
        categories = mongo.db.categories

        category_id = categories.insert_one({
            'category_name': request.json['category_name'],
            'cid': ''.join(
                random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in
                range(8)),
            'sub_categories': [],
            'created_at': datetime.datetime.now(),
        })

        created_product = categories.find_one({'_id': ObjectId(str(category_id.inserted_id))})

        output = {
            'category_name': created_product['category_name'],
            'cid': created_product['cid'],
            'sub_categories': created_product['sub_categories'],
            'created_at': created_product['created_at']
        }

        return jsonify({"data": output})