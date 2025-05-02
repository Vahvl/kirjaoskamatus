# flask vist
from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/t1")
def t1():
    return render_template("tase1.html")

@app.route("/t2")
def t2():
    return render_template("tase2.html")

@app.route("/t3")
def t3():
    return render_template("tase3.html")

@app.route("/meist")
def meist():
    return render_template("storage.html")
  

if __name__ == '__main__':
    app.run(debug=True)

url_for("static", filename="style.css")
url_for("static",  filename="main.js")