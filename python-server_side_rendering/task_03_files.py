#!/usr/bin/python3
"""
Flask app that reads products from JSON or CSV files.
"""

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__, template_folder="templates")


# ---------------- JSON READER ----------------
def read_json():
    """Read products from JSON file."""
    with open('products.json', 'r') as f:
        return json.load(f)


# ---------------- CSV READER ----------------
def read_csv():
    """Read products from CSV file."""
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products


# ---------------- ROUTE ----------------
@app.route('/products')
def products():
    """Display products based on source and optional id."""

    source = request.args.get('source')
    product_id = request.args.get('id')

    data = []
    error = None

    # ---------- SOURCE CHECK ----------
    if source == "json":
        data = read_json()

    elif source == "csv":
        data = read_csv()

    else:
        return render_template('product_display.html', error="Wrong source", products=[])

    # ---------- FILTER BY ID ----------
    if product_id:
        product_id = int(product_id)
        data = [p for p in data if int(p['id']) == product_id]

        if not data:
            return render_template('product_display.html',
                                   error="Product not found",
                                   products=[])

    return render_template('product_display.html',
                           products=data,
                           error=None)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
