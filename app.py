from webbrowser import get
from wsgiref.simple_server import ServerHandler
import numpy as np
import pandas as pd
from flask import Flask, jsonify, request, render_template
from flask_modals import Modal
import re

from src.top_movies_rec import top_movies_rec
from src.get_rec import get_rec

app = Flask(__name__)

movies_df = top_movies_rec()
movies = [
    {'title': title, 'overview': overview} for title, overview in zip(movies_df.title, movies_df.overview)
]

@app.route('/', methods=["GET", "POST"])
def home():
    global movies
    if request.method == 'POST':
        genre = request.form.getlist('genre')
        keyword = request.form.getlist('keyword')
        keywordTA = request.form.get('keywordTextArea')
        if keywordTA == '':
            keywordTA = None
        favMovie = request.form.get('favMovie')
        if genre or keyword or keywordTA:
            try:
                search_terms = genre + keyword + keywordTA.split(",")
            except:
                search_terms = genre + keyword
        else:
            search_terms = None
        movies_df = get_rec(search_terms=search_terms, fav_movie=favMovie)
        movies = [
            {'title': title, 'overview': overview} for title, overview in zip(movies_df.title, movies_df.overview)
        ]
        return render_template('index.html', movies=movies)
    return render_template("index.html", movies=movies)

if __name__=='__main__':
    app.run(debug=True)