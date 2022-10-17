# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
from flask import Flask, render_template, request

app = Flask(__name__)


class Item:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount


@app.route("/")
def hello_world():
    items = [
        Item("Apfel", 5),
        Item("Computer", 1),
        Item("Birne", 4)
    ]

    out = render_template("start.html", name="Stefan Eder", items=items)
    return out


@app.route("/test")
def test():
    name = request.args.get("name")
    age = request.args.get("age")
    return render_template("test.html", name=name, age=age)


@app.route("/currency")
def currency():
    currency1 = request.args.get("currency1", "EUR")
    currency2 = request.args.get("currency2", "EUR")
    rate = float(request.args.get("rate", "1.0"))

    table1 = []
    for x in range(1, 50):
        table1.append((x, round(x * rate, 2)))

    table2 = []
    for x in range(1, 50):
        table2.append((x, round(x / rate, 2)))

    return render_template("currency.html",
                           currency1=currency1,
                           currency2=currency2,
                           rate=rate,
                           table1=table1,
                           table2=table2)
