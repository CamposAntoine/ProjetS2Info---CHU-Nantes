from flask import Flask,request, render_template

app= Flask("Appli de ouf")

@app.route("/")
def index():
  context = {
      "name": "Bob l'éponge",
      "data": [1,2,3,4,5,6,7,8,9,10]
  }
  return render_template("index.html", **context) ## pouvant être du html, du json, ....
#on ajoute le dictionnaire contexte avec des données


@app.route("/named/<string:name>/<int:nb_item>")
def named(name,nb_item):
  context = {
      "name": name,
      "data": [i for i in range (nb_item)]
  }
  return render_template("index.html", **context)


@app.route("/hello")
def hello():
    name = request.args.get("name", "No name")
    return f"<h1>Hello {name}</h1>"
#on demande à l'ulisateur la variable name. Si elle n'est pas donnée on affiche No Name
#Pour ce faire on tape : http://127.0.0.1:3001/hello?name=Matti

@app.route("/user/<string:name>/<int:repeat>")
def user_profile(name,repeat):
    return f"<h1> User : {name}</h1>" * repeat
#url paramétrique on met directement dans l'url des variables
#pour faire un espace on écrit %20


@app.route("/about")
def about():
    return "<h1>Page About</h1> <a href='/'> Home </a> <br> <p> This is a simple web app created using Flask</p>"
app.run(debug=True, port=3001)