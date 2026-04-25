#!/usr/bin/python3
"""
Basic Flask application using Jinja templates.
"""

from flask import Flask, render_template
import os

app = Flask(__name__, template_folder="templates")


@app.route('/')
def home():
    """Home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """About page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Contact page."""
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
