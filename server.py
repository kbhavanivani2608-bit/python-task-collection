from flask import Flask, jsonify
from flask_cors import CORS
import csv

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "Python Task Server is running!"


@app.route("/products")
def products():

    products = []

    try:
        with open("products.csv", "r", encoding="utf-8-sig") as file:

            reader = csv.DictReader(file)

            for row in reader:
                products.append(row)

        return jsonify(products)

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)