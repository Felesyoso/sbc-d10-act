# app.py

from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_age', methods=['POST'])
def calculate_age():
    fullname = request.form['fullname']
    birthdate_str = request.form['birthdate']
    
    birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    
    return render_template('result.html', fullname=fullname, age=age)

if __name__ == '__main__':
    app.run(debug=True)
