from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ninja")
def all_ninjas():
    return render_template("ninja.html")

@app.route("/ninja/<color>")
def ninja(color):
    return render_template("ninja.html", color=color)


app.run(debug=True)