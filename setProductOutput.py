from flask import Flask, jsonify, request
from flask_pymongo import PyMongo, pymongo
from keys import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = db
mongo = PyMongo(app)

class ProductOutput:
    def __init__(self, params):
        self.params = params
        self.output = []

    def setOutput(self):
        def last_id(start):
            try: 
                return start[q_offset]['_id']
            except:
                return 0
        products = mongo.db.products
        count = 0
        company_list = []
        sub_list = []
        type_list = []

        q_limit = int(request.args.get('limit', 20))
        q_offset = int(request.args.get('offset', 0))
        starting_id = products.find(self.params).sort("_id", pymongo.ASCENDING)
        count = starting_id.count()
        great_id = {"_id": {'$gte': last_id(starting_id)}}
        for product in starting_id:
            if product['company'] not in company_list:
                company_list.append(product['company'])
                
            if product['category']['sub_category']['name'] not in sub_list:
                sub_list.append(product['category']['sub_category']['name'])

            if product['category']['sub_category']['type'] not in type_list:
                type_list.append(product['category']['sub_category']['type'])

        self.params.update(great_id)

        for query in products.find(self.params).sort("_id", pymongo.ASCENDING).limit(q_limit):
            self.output.append({
                "pid": query['pid'],
                "title": query['title'],
                "company": query['company'],
                "price": query['price'],
                "price_percentage": query['price_percentage'],
                "created_at": query['created_at'],
                "quantity": query['quantity'],
                "num_of_shares": query['num_of_shares'],
                "about": query['about'],
                "category": query['category'],
                "images": query['images']
            })

        return {
            "output": self.output,
            'count': count,
            "company_list": company_list,
            "sub_list": sub_list,
            "type_list": type_list
        }