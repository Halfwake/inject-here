from flask import Flask
from flask import request, render_template, session, redirect, url_for

import hashlib

app = Flask(__name__)
app.secret_key = '4' # Number chosen by die roll. Guranteed to be random!
app.debug = True

DB_NAME = 'data.db'

@app.route('/')
def home():
    return render_template('home.html')

def user_exists(username):
    'Check if user exists.'
    conn = sqlite3.connect(DB_NAME)
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = '%s'" % (username,))
        return not not cursor.fetchone()
    finally:
        conn.close()

def user_hash(username):
    'Lookup the hash for this user in the database.'
    conn  = sqlite3.connect(DB_NAME)
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = '%s'" % (username,))
        cursor.fetchone()[1]
    finally:
        conn.close()

def valid_login(username, password):
    'Check if login information is valid.'
    return user_exists(username) and (user_hash(username) == hash_password(password))

def hash_password(password):
    'Hash the password attempt.'
    hasher = hashlib.md5()
    hasher.update(password)
    return hasher.hexdigest()

@app.route('/new_account', methods = ['GET', 'POST'])
def new_account():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not user_exists(username):
            add_account(username, password)
            return redirect(url_for('login'))
        else:
            return render_template('new_account.html', error = 'Username already in use.')
    elif request.method == 'GET':
        return render_template('new_account.html')
         

def take_money(username, amount):
    'Add money to this user\s' account'

def add_account(username, password):
    hashword = hash_password(password)
    conn = sqlite3.connect(DB_NAME)
    try:
        cursor = conn.cursor()
        cursor.execture("INSERT INTO users VALUES ('%s', '%s', %d)" % (username, hashword, 0))
        conn.commit()
    finally:
        conn.close()

@app.route('/logout')
def logout():
    return redirect('home') 

if __name__ == '__main__':
    app.run()
