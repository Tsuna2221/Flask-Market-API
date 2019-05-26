from flask import Flask, jsonify, request
from flask_pymongo import PyMongo, pymongo
from flask_cors import CORS
try:
    from keys import db
except:
    from os import environ
    db = environ.get('DB')

app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = db
mongo = PyMongo(app)

class CategoryOutput:
    def __init__(self, params):
        self.params = params
        self.output = []

    def setOutput(self):
        categories = mongo.db.categories
        data = categories.find(self.params)

        for item in data:
            self.output.append({
                "category_name": item['category_name'],
                "cid": item['cid'],
                "sub_categories": item['sub_categories']
            })

        return self.output