import json
from flask import Flask, render_template, request, redirect
    
app = Flask(__name__)

@app.route("/")
def get_menu():
    return render_template("home.html")

@app.route("/appel")
def get_appel():
    with open("test.json", 'r') as f:
        tree = json.load(f)
        return render_template("appel.html", **tree)

database={'admin': 'admin'}

@app.route("/login/", methods=['POST', 'GET'])
def login():
    if "username" not in request.form:
        return render_template("login.html")
    
    id= request.form['username']
    mdp= request.form['password']
    if id not in database:
        return render_template("login.html", message="Votre nom d'utilisateur est invalide.")
    else:
        if database[id]!=mdp:
           return render_template("login.html", message="Votre mot de passe et votre nom d'utilisateur ne correspondent pas.")
        else:
            return redirect("/admin")

@app.route("/admin")
def admin():
    return render_template("admin.html")
