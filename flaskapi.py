from flask import Flask, json
from flask_cors import CORS

import data

api = Flask(__name__)
CORS(api)


@api.route("/sales/female", methods=["GET"])
def get_items_fe():
    return json.jsonify(data.CLOTHES_SALES_FEMALE)


@api.route("/sales/male", methods=["GET"])
def get_items_ma():
    return json.jsonify(data.CLOTHES_SALES_MALE)


@api.route("/collection/<int:item_id>", methods=["GET"])
def get_item(item_id):
    print(item_id)
    if item_id > data.CLOTHES_SALES_MALE[-1]["id"]:
        return json.jsonify({"err": "not_found", "status": 404})
    if item_id <= 100:
        item = [item for item in data.CLOTHES_SALES_FEMALE if item["id"] == item_id]
        return json.jsonify(item)
    else:
        item = [item for item in data.CLOTHES_SALES_MALE if item["id"] == item_id]
        return json.jsonify(item)


if __name__ == "__main__":
    api.run()
