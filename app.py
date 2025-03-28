# flask vist
from flask import Flask
Flask.url_for('static', filename='style.css')
Flask.url_for('static', filename='main.html')

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)

