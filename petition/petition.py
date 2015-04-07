from flask import Flask
from flask import request, render_template

import sqlite3

DB_NAME = 'data.db'

app = Flask(__name__)
app.debug = True

def add_name(name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.executescript("INSERT INTO names VALUES ('%s');" % (name,))
        conn.commit()
    finally:
        conn.close()

def all_names():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        return cursor.execute("SELECT * FROM names;").fetchall()
    finally:
        conn.close()

def render_petition():
    names = all_names()
    return render_template(
        'home.html',
        names = [name[0] for name in names],
        amount = len(names))

@app.route('/', methods = ['POST', 'GET'])
def petition():
    if request.method == 'POST':
        add_name(request.form['name'])
        return render_petition()
    elif request.method == 'GET':
        return render_petition()

if __name__ == '__main__':
    app.run()
