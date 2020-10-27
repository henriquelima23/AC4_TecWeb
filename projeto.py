from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/equipes")
def equipes():
    return render_template("equipes.html")

@app.route("/bauru")
def bauru():
    return render_template("bauru.html")

@app.route("/brasilia")
def brasilia():
    return render_template("brasilia.html")

@app.route("/caxias")
def caxias():
    return render_template("caxias.html")

@app.route("/cerrado")
def cerrado(): 
    return render_template("cerrado.html")

@app.route("/corinthians")
def corinthians():
    return render_template("corinthians.html")

@app.route("/flamengo")
def flamengo():
    return render_template("flamengo.html")

@app.route("/fortaleza")
def fortaleza():
    return render_template("fortaleza.html")

@app.route("/sesi")
def sesi():
    return render_template("sesi.html")

@app.route("/minas")
def minas():
    return render_template("minas.html")

@app.route("/mogi")
def mogi():
    return render_template("mogi.html")

@app.route("/pato")
def pato():
    return render_template("pato.html")

@app.route("/paulistano")
def paulistano():
    return render_template("paulistano.html")

@app.route("/pinheiros")
def pinheiros():
    return render_template("pinheiros.html")

@app.route("/sao_paulo")
def sao_paulo():
    return render_template("sao_paulo.html")

@app.route("/unifacisa")
def unifacisa():
    return render_template("unifacisa.html")

@app.route("/mourao")
def mourao():
    return render_template("mourao.html")

app.run()