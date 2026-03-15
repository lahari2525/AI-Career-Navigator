from flask import Flask, render_template, request
from reasoning_engine import recommend_career

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():

    result = None

    if request.method == "POST":
        skills = request.form["skills"].split(",")
        result = recommend_career(skills)

    return render_template("index.html", result=result)
app.run(host="127.0.0.1", port=5000, debug=True)
