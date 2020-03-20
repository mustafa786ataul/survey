from survey_project import app
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login_emp', methods=['GET', 'POST'])
def login_emp():
    return render_template('login_emp.html')

@app.route('/login_lm', methods=['GET', 'POST'])
def login_lm():
    return render_template('login_lm.html')