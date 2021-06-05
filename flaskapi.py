from flask import Flask, json

import data

api = Flask(__name__)


@api.route("/", methods=["GET"])
def get_items():
    return json.dumps(data.CLOTHES)


if __name__ == "__main__":
    api.run()
