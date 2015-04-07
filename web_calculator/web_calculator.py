from flask import Flask
from flask import request, render_template

from calculator import calculate

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def math():
    if request.method == 'POST':
        math_str = str(request.form['math_str'])
        return render_template('result.html', result = calculate(math_str))
    elif request.method == 'GET':
        return render_template('calculate.html')
    
if __name__ == '__main__':
    app.run()
