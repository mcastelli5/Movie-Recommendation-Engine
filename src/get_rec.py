from src.top_movies_rec import top_movies_rec
from src.content_based_rec import content_based_rec
from src.collab_filtering_rec import collab_based_rec
from src.hybrid_rec import hybrid_rec

def get_rec(search_terms: list = [], fav_movie: str = None):
    """
    Summary:
        decide what strategy is used to return recommnedations to the user based on the preferences that they provided.

    Args:
        search_terms (list, optional): keywords input by the user that can be used to match similar words in movies. Defaults to [].
        fave_movie (str, optional): user's favorite movie that can be used to find similar users that have rated other movies. Defaults to None.
    """
    
    # Top Movies Recommendation
    if not search_terms and not fav_movie:
        rec_df = top_movies_rec()
    
    # Content-based Recommendation
    elif search_terms and not fav_movie:
        rec_df = content_based_rec(search_terms=search_terms)
    
    # Collaborative Filtering Recommendation
    elif not search_terms and fav_movie:
        rec_df = collab_based_rec(fav_movie=fav_movie)
    
    # Hybrid Recommendation
    elif search_terms and fav_movie:
        rec_df = hybrid_rec(search_terms, fav_movie)
    
    # Return the recommendations to be shown to the user
    return rec_df