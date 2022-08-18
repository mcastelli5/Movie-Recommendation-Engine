import src.config as config
import pandas as pd
from src.collab_filtering_rec import collab_based_rec
from src.content_based_rec import content_based_rec

movies = pd.read_csv(config.TRAINING_FILE_MOVIES)

def hybrid_rec(search_terms, fav_movie):    
    # Get content-based recommendations
    collab_recs_df = collab_based_rec(fav_movie=fav_movie)
    
    # Generate estimates on the content-based recs df
    hybrid_df = content_based_rec(movies_df=collab_recs_df, search_terms=search_terms)
    
    # Create rnk column for hybrid recommendations to be sorted on
    hybrid_df.reset_index(inplace=True)
    hybrid_df.rename({"index": "rnk"}, axis=1, inplace=True)
    
    # Filter df to top 10 content-based recommendations (regardless of est value)
    hybrid_df = hybrid_df[:10]
    
    # Sort movies dataframe by "est" column
    hybrid_df.sort_values(["est", "rnk"], ascending=[False, True], inplace=True)
    hybrid_df.reset_index(inplace=True, drop=True)
    
    # Get top ranked movies
    return hybrid_df