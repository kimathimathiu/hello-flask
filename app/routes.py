from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
   """Index URL"""
   return render_template ('index.html', title="Index")


@app.route('/about')
def about():
   """Index URL"""
   return render_template ('about.html', title="About")