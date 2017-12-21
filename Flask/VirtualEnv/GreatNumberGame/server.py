from flask import Flask, redirect, render_template, session, request

import random

app = Flask(__name__)
app.secret_key = "asjiojasd"



@app.route("/")
def index():
    return render_template("index.html")

def number():
    num = random.randrange(0,101)
    return 

@app.route("/guess", methods=["POST"])
def guess():
    random_num = number()
    session["input"] = int(request.form["input"])

    if session["input"] == random_num:
        session["status"] = "win"
    elif session["input"] > random_num:
        session["status"] = "high"
    elif session["input"] < random_num:
        session["status"] = "low"
    return redirect("/")

app.run(debug=True)