# flask vist
from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)

url_for("static", filename="style.css")
url_for("static",  filename="main.js")