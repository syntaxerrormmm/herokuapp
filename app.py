from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Ciao mondo!</h1>"

@app.route('/info')
def info():
    return "Informazioni"

if __name__ == '__main__':
    app.run()
