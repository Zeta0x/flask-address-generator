import requests
from flask import Flask, jsonify, redirect, url_for
import json


app = Flask(__name__)


def fake_data():
    url = 'https://fakerapi.it/api/v1/addresses?_quantity=1'
    request = requests.get(url).text
    json_response = json.loads(request)
    return json_response


@app.route("/", methods=['GET'])
def index():
    return redirect(url_for("fake_address_generator"))


@app.route("/fake-address", methods=['GET'])
def fake_address_generator():
    response = jsonify(fake_data())
    return response


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)