from flask import render_template,request,redirect,url_for
from . import main

@main.route('/')
def index():

    title = 'Home Page - Get The latest Pitch stories'
    return render_template('index.html',title = title, article=news_article)
