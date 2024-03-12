from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def get_menu():
    return render_template("home.html")
