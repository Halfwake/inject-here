from flask import Flask
from flask import render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/broken')
def broken():
    return str(1 / 0)

if __name__ == '__main__':
    app.run()
