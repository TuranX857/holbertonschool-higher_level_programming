#!/usr/bin/python3
"""
Flask app that renders items from JSON using Jinja.
"""

from flask import Flask, render_template
import json

app = Flask(__name__, template_folder="templates")


@app.route('/items')
def items():
    """Display items from JSON file."""

    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get("items", [])
    except Exception:
        items_list = []

    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
