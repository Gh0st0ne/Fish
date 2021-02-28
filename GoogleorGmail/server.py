from flask import Flask
from flask.templating import render_template


app = Flask(__name__)
@app.route("/")
def he():
    return render_template("Gmail.html")

app.run()