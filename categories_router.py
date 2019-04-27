from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS
import datetime, random, string
import pprint, re

app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/flask_market"
mongo = PyMongo(app)


class CategoriesRouter:
    @staticmethod
    def get():
        categories = mongo.db.categories
        products = mongo.db.products
        q_categories = request.args.get('category', None)
        q_id = request.args.get('id', None)

        output = []
        category_list = []
        total_products = []

        if q_categories:
            for query in categories.find({"category_name": re.compile('^' + q_categories + '$', re.IGNORECASE)}):
                product_list = []

                for item in query['sub_categories']:
                    for type in item['types']:
                        for product in products.find({'category.sub_category.type': type['type_label'], 'category.sub_category.name': item['name']}):
                            total_products.append(product['pid'])
                            product_list.append(product['pid'])

                            type['products'].append({
                                "pid": product['pid'],
                                "title": product['title'],
                                "company": product['company'],
                                "price": product['price'],
                                "price_percentage": product['price_percentage'],
                                "created_at": product['created_at'],
                                "quantity": product['quantity'],
                                "num_of_shares": product['num_of_shares'],
                                "about": product['about'],
                                "category": product['category'],
                                "images": product['images']
                            })

                output = {
                    "category_name": query['category_name'],
                    "cid": query['cid'],
                    'num_of_products': len(product_list),
                    "sub_categories": query['sub_categories']
                }

        elif q_id:
            for query in categories.find({"cid": q_id}):
                product_list = []

                for item in query['sub_categories']:
                    for type in item['types']:
                        for product in products.find({'category.sub_category.type': type['type_label'], 'category.sub_category.name': item['name']}):
                            total_products.append(product['pid'])
                            product_list.append(product['pid'])

                            type['products'].append({
                                "pid": product['pid'],
                                "title": product['title'],
                                "company": product['company'],
                                "price": product['price'],
                                "price_percentage": product['price_percentage'],
                                "created_at": product['created_at'],
                                "quantity": product['quantity'],
                                "num_of_shares": product['num_of_shares'],
                                "about": product['about'],
                                "category": product['category'],
                                "images": product['images']
                            })

                output = {
                    "category_name": query['category_name'],
                    "cid": query['cid'],
                    'num_of_products': len(product_list),
                    "sub_categories": query['sub_categories']
                }
        else:
            for query in categories.find():
                product_list = []
                category_list.append(query['category_name'])

                for item in query['sub_categories']:
                    for type in item['types']:
                        for product in products.find({'category.sub_category.type': type['type_label'], 'category.sub_category.name': item['name']}):
                            total_products.append(product['pid'])
                            product_list.append(product['pid'])

                            type['products'].append({
                                "pid": product['pid'],
                                "title": product['title'],
                                "company": product['company'],
                                "price": product['price'],
                                "price_percentage": product['price_percentage'],
                                "created_at": product['created_at'],
                                "quantity": product['quantity'],
                                "num_of_shares": product['num_of_shares'],
                                "about": product['about'],
                                "category": product['category'],
                                "images": product['images']
                            })

                output.append({
                    "category_name": query['category_name'],
                    "sub_categories": query['sub_categories'],
                    "cid": query['cid'],
                    'num_of_products': len(product_list),
                })

        return jsonify({'data': output, 'total_categories': len(category_list), 'total_products': len(total_products)})

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