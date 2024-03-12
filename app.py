from flask import Flask, render_template, session, request, redirect
    
app = Flask(__name__)

@app.route("/")
def get_menu():
    return render_template("home.html")

@app.route("/appel")
def get_appel():
    return render_template("appel.html")

database={'admin': 'admin'}

@app.route("/login/")
def login():
    return render_template("login.html")

@app.route('/form_login', methods=['POST', 'GET'])
def form_login():
    id= request.form['username']
    mdp= request.form['password']
    if id not in database:
        return render_template("login.html", message="Votre nom d'utilisateur est invalide.")
    else:
        if database[id]!=mdp:
            render_template("login.html", message="Votre mot de passe et votre nom d'utilisateur ne correspondent pas.")
        else:
            return redirect("/admin")

@app.route("/admin")
def admin():
    return render_template("admin.html")