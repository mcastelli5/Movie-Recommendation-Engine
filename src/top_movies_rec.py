import config

def top_movies_rec():
    """
    Summary:
        provides user with top 10 most popular movies at this moment, since they did not provide any input. Not personalized towards the user at all.

    Args:
        movies (pd.DataFrame): movies dataframe the contains the movie metadata

    Returns:
        list: list of top 10 movies based on popularity scores
        
    Edge Cases:
        user just wants to see the most popular movies without a personalized recommendation algorithm added to it
        user accidentally bypassess the user preferences and scrolls to the movie recs section which will automatically populate the top movies at the moment (static for this project)
    """
    movies = config.TRAINING_FILE_MOVIES
    ranked_titles = []
    ranked_movies = movies.copy(deep=True)
    ranked_movies = ranked_movies.sort_values("popularity", ascending=False)
    for idx in range(10):
        ranked_titles.append([movies.title.iloc[idx], movies.rating_id.iloc[idx]])
    return ranked_titles