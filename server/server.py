from flask import Flask, render_template
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/clicked")
def hello_server():
    conn = get_db_connection()
    todos = conn.execute('SELECT * FROM TodoList').fetchall()
    conn.close()
    todo = ""
    for row in todos:
        todo = list(row)
    return ', '.join(str(value) for value in todo) # TODO: need fix

def hello_server_html():
    return "<p>Hello Servers</p>"

 
