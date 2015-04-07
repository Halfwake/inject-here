from flask import Flask
from flask import render_template, request, url_for, redirect

app = Flask(__name__)
app.debug = True

def valid_login(username, password):
    valid_username = username == 'president@whitehouse.gov'
    valid_password = password == 'metalwolfchaos1'
    return valid_username and valid_password

@app.route('/', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if valid_login(username, password):
            return redirect(url_for('nuke_launch'))
        else:
            return render_template(
                'login.html',
                error = 'Unauthorized access. This incident will be reported to your parents.')

@app.route('/nuke', methods = ['GET', 'POST'])
def nuke_launch():
    if request.method == 'GET':
        return render_template('nuke.html')
    elif request.method == 'POST':
        return render_template('launch.html')

if __name__ == '__main__':
    app.run()
