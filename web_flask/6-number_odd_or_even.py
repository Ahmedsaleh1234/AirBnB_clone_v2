#!/usr/bin/python3
"""starts a Flask web application:"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """return text"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def home():
    """return text"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """retrun replace text"""
    text = text.repalce("_", " ")
    return "C {text}".format(text)


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py_text(text):
    """return replace text"""
    text = text.replace("_", " ")
    return "python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """return number"""
    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def html_number(n):
    """display a HTML page only if n is an integer"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def html_odd_or_even(n):
    """display a HTML page only if n is an intege"""
    if (n % 2 == 0):
        x = 'even'
    else:
        x = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           x=x)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
