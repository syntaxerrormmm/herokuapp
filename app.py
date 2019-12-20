from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    titolo="Pagina iniziale"
    testo="Ciao mondo!"
    bottone="Più info"
    return render_template("index.html",
            titolo=titolo,
            testo=testo,
            bottone=bottone)

@app.route('/info')
def info():
    titolo="Pagina info"
    testo="Informazioni"
    bottone="Homepage"
    return render_template("info.html",
            titolo=titolo,
            testo=testo)

if __name__ == '__main__':
    app.run()
