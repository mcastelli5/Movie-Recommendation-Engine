from top_movies_rec import top_movies_rec
from content_based_rec import content_based_rec
from collab_filtering_rec import collab_based_rec
from hybrid_rec import hybrid_rec

def get_rec(search_terms: list = [], fave_movie: str = None):
    """
    Summary:
        decide what strategy is used to return recommnedations to the user based on the preferences that they provided.

    Args:
        search_terms (list, optional): keywords input by the user that can be used to match similar words in movies. Defaults to [].
        fave_movie (str, optional): user's favorite movie that can be used to find similar users that have rated other movies. Defaults to None.
    """
    
    # Top Movies Recommendation
    if not search_terms and not fave_movie:
        rec_df = top_movies_rec()
    
    # Content-based Recommendation
    elif search_terms and not fave_movie:
        rec_df = content_based_rec(search_terms=search_terms)
    
    # Collaborative Filtering Recommendation
    elif not search_terms and fave_movie:
        rec_df = collab_based_rec(fave_movie=fave_movie)
    
    # Hybrid Recommendation
    elif search_terms and fave_movie:
        rec_df = hybrid_rec(search_terms, fave_movie)
    
    # Get top 50 recommendations (in order)
    ranked_titles = []
    for idx, row in rec_df.iterrows():
        ranked_titles.append([idx, row.title])
    
    # Return the recommendations to be shown to the user
    return ranked_titles