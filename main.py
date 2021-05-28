import sys
import os
import time
import traceback
import pprint
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class home(Resource):
    def get(self):
        return {"data": "Hello-World"}, 200

api.add_resource(home, "/")

if __name__ == "__main__":
    app.run(debug=True)


