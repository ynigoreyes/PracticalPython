# I filled this file in from some stuff I had, I am sure you do not care though

from flask import Flask, render_template, abort, request

app = Flask("app")   #name = name of file currently in

@app.route("/")

def index():
    pizza = request.args.get("pizza")
    drink = request.args.get("drink")
    drinks =["coke", "cream soda", "juice", "sprite", "water"]
    pizzas =["cheese", "pepperoni", "steak", "spinach", "alfredo"]
    if pizza in pizzas:
        return render_template("index.html", pizza = pizza, drink=drink)
    else:
        return abort(404)

#return "<b>Hello everyone</b>." #makes it bold

if __name__ == "__main__":      #if not doing python main.py this will not pass
    app.run(host = "0.0.0.0", port = 5000)
