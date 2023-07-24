from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/clicked")
def hello_server():
    return hello_server_html() 


def hello_server_html():
    return "<p>Hello Servers</p>"

 
