# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    items = ["Apfel", "Birne", "Banane"]

    out = render_template("start.html", name="Stefan Eder", items=items)
    return out


@app.route("/test")
def test():
    name = request.args.get("name")
    return render_template("test.html", name=name)
