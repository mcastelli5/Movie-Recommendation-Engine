from get_estimate import get_estimate
import config
import joblib

import pandas as pd

from surprise import Dataset
from surprise import Reader
from surprise.model_selection import cross_validate

def collab_based_rec(): #movies, ratings, fav_movie
    """
    Summary:
        provide user with recommended movies based on collaborative filtering approach by using their favorite movie to find similar users and their respective preferences.

    Args:
        movies (pd.DataFrame): movies dataframe the contains the movie metadata
        ratings (pd.DataFrame): user ratings dataframe that contains 100k ratings for related movies
        fav_movie (str): string value to represent the users favorite movie
        
    Returns:
        list: collaborative filtered movie recommendations based on user's favorite movie

    model = joblib.load(config.SVD_MODEL)
    df = movies.copy(deep=True)
    
    # Get fav_movie id for the User's favorite movie to analyize
    fav_movie_id = df[df.title == fav_movie]['rating_id'].values[0]
    
    # Get similiar users that have highly rated the users fav_movie in the past (top 15 users)
    similar_users = set(ratings[(ratings.movieId == fav_movie_id) & (ratings.rating >= 4)]["userId"])

    # Estimate the ratings the User would give each movie based on the similar users (predicted) ratings
    df['est'] = df.apply(lambda x: get_estimate(similar_users, x.id, model), axis=1)
    """
    model = joblib.load(config.SVD_MODEL)
    # Ingest all inputs
    ratings = pd.read_csv(config.TRAINING_FILE_RATINGS)
    
    # Instantiate reader object and svd object
    reader = Reader(rating_scale=(1, 5))

    # Load data into surprise dataset format with reader
    data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)
    cross_validate(model, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
    print(model)
    return model