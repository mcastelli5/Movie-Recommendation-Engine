import numpy as np
import pandas as pd
from flask import Flask, jsonify, request, render_template
from flask_modals import Modal
import re

from src.top_movies_rec import top_movies_rec

app = Flask(__name__)

movies = [
    {
        'title': 'Movie 1',
        'overview': 'Movie 1 Overview'
    },
    {
        'title': 'Movie 2',
        'overview': 'Movie 2 Overview'
    },
    {
        'title': 'Movie 3',
        'overview': 'Movie 3 Overview'
    },
    {
        'title': 'Movie 4',
        'overview': 'Movie 4 Overview'
    },
    {
        'title': 'Movie 5',
        'overview': 'Movie 5 Overview',
        'genres': 'Move 5 Genres'
    },
    {
        'title': 'Movie 6',
        'overview': 'Movie 6 Overview'
    },
    {
        'title': 'Movie 7',
        'overview': 'Movie 7 Overview'
    },
    {
        'title': 'Movie 8',
        'overview': 'Movie 8 Overview'
    },
    {
        'title': 'Movie 9',
        'overview': 'Movie 9 Overview'
    },
    {
        'title': 'Movie 10',
        'overview': 'Movie 10 Overview'
    }
]

@app.route('/', methods=["GET", "POST"])
def home():
    movies_df = top_movies_rec()
    movies = [
        {'title': title, 'overview': overview} for title, overview in zip(movies_df.title, movies_df.overview)
        ]
    print(request.form.getlist('genre'))
    print(request.form.getlist('keyword'))
    print(request.form.get('keywordTextArea'))
    print(request.form.get('favMovie'))
    return render_template("index.html", movies=movies)

if __name__=='__main__':
    app.run(debug=True)