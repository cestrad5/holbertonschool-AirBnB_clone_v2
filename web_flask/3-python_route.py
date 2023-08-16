#!/usr/bin/python3
"""3. Python is cool!"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home() -> str:
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb() -> str:
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def func_text(text: str) -> str:
    return "C {0}".format(text.replace("_", " "))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def func_python_text(text="is cool") -> str:
    return "Python {0}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
