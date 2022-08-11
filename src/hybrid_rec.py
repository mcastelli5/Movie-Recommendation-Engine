import config
import pandas as pd
from collab_filtering_rec import collab_based_rec
from content_based_rec import content_based_rec

movies = pd.read_csv(config.TRAINING_FILE_MOVIES)

def hybrid_rec(search_terms, fav_movie):
    global movies
    ratings = pd.read_csv(config.TRAINING_FILE_RATINGS)
    df = movies.copy(deep=True)
    
    # Get content-based recommendations
    collab_recs_df = collab_based_rec(fav_movie=fav_movie)
    
    # Generate estimates on the content-based recs df
    hybrid_df = content_based_rec(movies_df=collab_recs_df, search_terms=search_terms)
    
    # Create rnk column for hybrid recommendations to be sorted on
    hybrid_df.reset_index(inplace=True)
    hybrid_df.rename({"index": "rnk"}, axis=1, inplace=True)
    
    # Filter df to top 50 content-based recommendations (regardless of est value)
    hybrid_df = hybrid_df[:20]
    
    # Sort movies dataframe by "est" column
    hybrid_df.sort_values(["est", "rnk"], ascending=[False, True], inplace=True)
    hybrid_df.reset_index(inplace=True, drop=True)
    
    # Get top ranked movies
    return hybrid_df