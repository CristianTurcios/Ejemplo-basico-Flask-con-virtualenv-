from flask import request, redirect, render_template,url_for
from app import app

@app.route('/')
#@app.route('/index')

def index():
    return render_template('index.html',#"Hello world"
    cosas=['RPG', 'Python', 'Juegos de mesa', 'Cthulhu', 'etc'])