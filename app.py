from flask import Flask, render_template

app = Flask(__name__)

articles = {
    1: {
        "lien_image": "https://placehold.co/200x150",
        "titre": "Premier article",
        "accroche": ["L'accroche du 1er article ne fait qu'une ligne."],
        "date": "21/02/2024",
        "auteur": "Auteur 1"
    },
    2: {
        "lien_image": "https://placehold.co/200x150",
        "titre": "Deuxième article",
        "accroche": [
            "L'accroche du 2nd article fait deux lignes.",
            "Voici la preuve."
        ],
        "date": "22/02/2024",
        "auteur": "Auteur 2"
    }
}

@app.route("/")
def get_menu():
    return render_template("index.html", articles=articles)

@app.route("/article/<int:id>")
def get_article(id):
    article = articles[id]
    return render_template("article.html", **article)

@app.route("/auteur/login")
@app.route("/auteur/rediger")
@app.route("/auteursupprimer")
def get_auteur():
    pass
