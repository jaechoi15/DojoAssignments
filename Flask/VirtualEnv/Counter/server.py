from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)

app.secret_key="15"

@app.route('/')
def index():
    if "count" in session:
        session["count"] += 1
    else:
        session["count"] = 0
    return render_template("index.html", count=session["count"])

app.run(debug=True)