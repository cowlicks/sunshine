from flask import render_template

from app import app

departments = ['water', 'trash', 'cops']

@app.route('/')
def index():
    return render_template('index.html', departments=departments)

@app.route('/department/<dept>')
def department(dept):
    return "Welcome to the %s department" % dept
