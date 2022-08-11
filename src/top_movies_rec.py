import config
import pandas as pd

def top_movies_rec():
    """
    Summary:
        provides user with top 10 most popular movies at this moment, since they did not provide any input. Not personalized towards the user at all.

    Returns:
        pd.DataFrame: movies df that is sorted in descending order by popularity
        
    Edge Cases:
        user just wants to see the most popular movies without a personalized recommendation algorithm added to it
        user accidentally bypassess the user preferences and scrolls to the movie recs section which will automatically populate the top movies at the moment (static for this project)
    """
    
    movies = pd.read_csv(config.TRAINING_FILE_MOVIES)
    ranked_movies = movies.copy(deep=True)
    ranked_movies = ranked_movies.sort_values("popularity", ascending=False)
        
    # Reset index to adjust for new movie order
    ranked_movies.reset_index(drop=True, inplace=True)
    ranked_movies = ranked_movies[:20]
    
    return ranked_movies