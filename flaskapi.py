from flask import Flask, json
from flask_cors import CORS

import data

api = Flask(__name__)
CORS(api)


@api.route("/sales/female", methods=["GET"])
def get_items_fe():
    return json.dumps(data.CLOTHES_SALES_FEMALE)


@api.route("/sales/male", methods=["GET"])
def get_items_ma():
    return json.dumps(data.CLOTHES_SALES_MALE)


if __name__ == "__main__":
    api.run()
