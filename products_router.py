from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS
import datetime, random, string
import pprint

app = Flask(__name__)
CORS(app)
pp = pprint.PrettyPrinter(indent=4)
app.config["MONGO_URI"] = "mongodb://localhost:27017/flask_market"
mongo = PyMongo(app)

class ProductsRouter:
    @staticmethod
    def get():
        products = mongo.db.products
        q_company = request.args.get('company', None)
        q_pid = request.args.get('id', None)
        q_categories = request.args.get('category', None)

        if q_company:
            output = []

            if q_categories:
                for query in products.find({'company': q_company, 'category.category_name': q_categories}):
                    output.append({
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
            else:
                for query in products.find({'company': q_company}):
                    output.append({
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

        elif q_pid:
            output = []

            for query in products.find({'pid': q_pid}):
                output.append({
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

        elif q_categories:
            output = []

            for query in products.find({'category.category_name': q_categories}):
                output.append({
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

        else:
            output = []

            for query in products.find():
                output.append({
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

        return jsonify({
            "data": {
                "num_of_products": len(output),
                "products": output
            }
        })

    @staticmethod
    def post():
        products = mongo.db.products
        categories = mongo.db.categories

        request_category = categories.find_one({'category_name': request.json['category']['category_name']})

        request_category_name = request.json['category']['category_name']
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
        
        # Add category
        else:
            categories.insert_one({
                'category_name': request_category_name,
                'cid': ''.join(
                    random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _
                    in
                    range(8)),
                'sub_categories': [
                    {
                        'name': request_sub_category_name,
                        'types': [{
                            'type_label': request_sub_category_type,
                            'products': []
                        }]
                    }
                ]
            })

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

        return jsonify({"data": output})

    @staticmethod
    def delete(pid):
        products = mongo.db.products
        db_response = products.delete_one({'pid': pid})
        return jsonify({'data': db_response})

