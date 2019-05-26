from flask import Flask, jsonify, request
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from flask_cors import CORS
from setProductOutput import ProductOutput
import datetime, random, string
import pprint, re, math
try:
    from keys import db
except:
    from os import environ
    db = environ.get('DB')

app = Flask(__name__)
CORS(app)
pp = pprint.PrettyPrinter(indent=4)
app.config["MONGO_URI"] = db
mongo = PyMongo(app)

class ProductsRouter:
    @staticmethod
    def get():
        q_limit = int(request.args.get('limit', 20))
        q_offset = int(request.args.get('offset', 0))
        valid_parameters = {}

        def getInt(stat):
            if request.args.get(stat, 'None') == 'None':
                return 'None'
            return int(request.args.get(stat, 'None'))

        query_list = [
            {
                'key': 'company',
                'value': re.compile('^' + request.args.get('company', 'None') + '$', re.IGNORECASE)
            },
            {
                'key': 'pid',
                'value': request.args.get('id', 'None')
            },
            {
                'key': 'category.category_name',
                'value': re.compile('^' + request.args.get('category', 'None') + '$', re.IGNORECASE)
            },
            {
                'key': 'category.sub_category.name',
                'value': re.compile('^' + request.args.get('sub', 'None') + '$', re.IGNORECASE)
            },
            {
                'key': 'category.sub_category.type',
                'value': re.compile('^' + request.args.get('type', 'None') + '$', re.IGNORECASE)
            },
            {
                'key': 'price',
                'value': {'$gte': getInt('minprice')}
            },
            {
                'key': 'price',
                'value': {'$lte': getInt('maxprice')}
            },
            {
                'key': 'about.rating',
                'value': {'$gte': getInt('rating')}
            },
        ]

        for item in query_list:
            if 'None' not in str(item['value']):
                valid_parameters.update({item['key']: item['value']})

        if q_limit < 50:
            q_limit = q_limit
        else:
            q_limit = 50

        output = ProductOutput(valid_parameters).setOutput()

        def follow_query(c):
            if(c == "sub"):
                if(int(q_offset) - int(q_limit) < 0):
                    return "0"
                else:
                    return str(int(q_offset) - int(q_limit))

            if(c == "add"):
                if(int(q_offset) + int(q_limit) > output['count']):
                    return str(output['count'] - 1)
                else:
                    return str(int(q_offset) + int(q_limit))

        return jsonify({"data": {
            "query_next": "?limit=" + str(q_limit) + "&offset=" + follow_query('add'),
            "query_prev": "?limit=" + str(q_limit) + "&offset=" + follow_query('sub'), 
            "products": output['output'],
            "total_length": output['count'],
            "total_pages": math.ceil(output['count'] / q_limit),
            "total_query": len(output['output']),
            "list_companies": output['company_list'],
            "list_subs": output['sub_list'],
            "list_types": output['type_list']
        }})

    @staticmethod
    def post():
        products = mongo.db.products
        categories = mongo.db.categories

        request_category = categories.find_one({'category_name': request.json['category']['category_name']})

        request_sub_category_name = request.json['category']['sub_category']['name']
        request_sub_category_type = request.json['category']['sub_category']['type']

        # Check if category exists
        if request_category:
            name_array = []

            # Append sub-categories names into array
            for sub_categories in request_category['sub_categories']:
                name_array.append(sub_categories['name'])

            # Check if requested sub-category exists in array. If not add it
            if request_sub_category_name not in name_array:
                request_category['sub_categories'].append({
                    'name': request_sub_category_name,
                    'types': [{
                        'type_label': request_sub_category_type,
                        'products': []
                    }]
                })

                categories.update_one({'cid': request_category["cid"]}, {'$set': {'sub_categories': request_category['sub_categories']}})

            # Check if type exists in sub-category
            else:
                selected_category = [item for item in request_category['sub_categories'] if
                                     item['name'] == request_sub_category_name]
                selected_type_array = [item for item in selected_category[0]['types'] if
                                       item['type_label'] == request_sub_category_type]

                if selected_type_array == []:
                    modified = request_category['sub_categories']
                    filtered_categories = [item for item in modified if item['name'] != request_sub_category_name]
                    selected_category = [item for item in modified if item['name'] == request_sub_category_name]

                    selected_category[0]['types'].append({'type_label': request_sub_category_type, 'products': []})
                    filtered_categories.append(selected_category[0])

                    categories.update_one({'cid': request_category["cid"]}, {'$set': {'sub_categories': filtered_categories}})
        

        post_id = products.insert_one({
            'pid': ''.join(
                random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in
                range(8)),
            'title': request.json['title'],  #
            'company': request.json['company'],  #
            'price': request.json['price'],  #
            'price_percentage': request.json['price_percentage'],
            'created_at': datetime.datetime.now(),
            'quantity': request.json['quantity'],
            'num_of_shares': request.json['num_of_shares'],
            'about': request.json['about'],
            'category': request.json['category'],
            'images': request.json['images'],
        })

        created_product = products.find_one({'_id': ObjectId(str(post_id.inserted_id))})

        output = {
            'title': created_product['title'],
            'company': created_product['company'],
            'price': created_product['price'],
            'price_percentage': created_product['price_percentage'],
            'created_at': created_product['created_at'],
            'quantity': created_product['quantity'],
            'num_of_shares': created_product['num_of_shares'],
            'about': created_product['about'],
            'category': created_product['category'],
            'images': created_product['images'],
            'pid': created_product['pid']
        }

        return jsonify({output})

    @staticmethod
    def delete(pid):
        products = mongo.db.products
        db_response = products.delete_one({'pid': pid})
        return jsonify({'data': db_response})