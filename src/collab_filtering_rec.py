from get_estimate import get_estimate
import config
import joblib
import pandas as pd

model = joblib.load(config.SVD_MODEL)
movies = pd.read_csv(config.TRAINING_FILE_MOVIES)

def collab_based_rec(movies_df = movies, fav_movie = None):
    """
    Summary:
        provide user with recommended movies based on collaborative filtering approach by using their favorite movie to find similar users and their respective preferences.

    Args:
        movies (pd.DataFrame): movies dataframe the contains the movie metadata
        ratings (pd.DataFrame): user ratings dataframe that contains 100k ratings for related movies
        fav_movie (str): string value to represent the users favorite movie
        
    Returns:
        list: collaborative filtered movie recommendations based on user's favorite movie
    
    Edge Cases:
        user only provided a favorite movie and no search terms for content-based filtering (only collab filtering)
        user provided all information for preferences and user will get hybrid recommendations with both content-based and collab filtering strategies
    """
    
    ratings = pd.read_csv(config.TRAINING_FILE_RATINGS)
    global model
    df = movies_df.copy(deep=True)
    
    # Get fav_movie id for the User's favorite movie to analyize
    fav_movie_id = df[df.title == fav_movie]['rating_id'].values[0]
    fave_movie_idx = df[df.title == fav_movie].index[0]
    
    # Drop favorite movie from local movies df
    df = df.drop(index=fave_movie_idx)
    
    # Get similiar users that have highly rated the users fav_movie in the past (top 15 users)
    similar_users = set(ratings[(ratings.movieId == fav_movie_id) & (ratings.rating >= 4)].sort_values("rating", ascending=False)["userId"])

    # Estimate the ratings the User would give each movie based on the similar users (predicted) ratings
    df['est'] = df.apply(lambda x: get_estimate(similar_users, x.id), axis=1)
    
    # Sort movies dataframe by "est" column
    df = df.sort_values("est", ascending=False)
    
    # Get top ranked movies
    return df