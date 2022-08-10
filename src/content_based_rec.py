from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import config

movies = pd.read_csv(config.TRAINING_FILE_MOVIES)

def content_based_rec(movies_df=movies, search_terms=[]):
    """
    Summary:
        provides a content-based movie recommnedation based on the users search terms that they provided as input
    
    Args:
        movies (pd.DataFrame): movies dataframe the contains the movie metadata
        search_terms (list): values provided by the user that will allow movies to be rated on content specific values

    Returns:
        pd.DataFrame: df containing content-based movie recommendations based on user search terms
    
    Edge Cases:
        user cannot think of favorite movie and only provides movie keywords and genres that they are interested in
        user provides all user preference information and content-based information is used in tandem with collaborative filtering technique for a better personalized recommendation
    """
    
    df = movies_df.copy(deep=True)
    
    # Calculate the average "vote_average" to limit the recs to movies that are above average
    rating_avg = round(df.vote_average.mean(), 0)
    df = df[df.vote_average >= rating_avg]
    
    # Creating a copy of the last row of the dataset, which we will use to input the user's input
    new_row = df.iloc[-1,:].copy()
    
    # Adding the input to the new row
    new_row.iloc[-2] = " ".join(search_terms)
  
    # Adding the new row to the dataset
    df = df.append(new_row)
  
    # Vectorizing the entire matrix
    count = CountVectorizer(analyzer = 'word', stop_words='english', ngram_range=(1, 2))
    count_matrix = count.fit_transform(df['soup'])

    # Pairwise cosine similarity and creating the cosine matrix
    cosine_sim2 = cosine_similarity(count_matrix, count_matrix)
  
    # Sorting cosine similarities by highest to lowest
    sim_scores = list(enumerate(cosine_sim2[-1,:]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Append top ranked df based on search terms to ranked_titles
    ranked_titles = movies_df[movies_df.index == sim_scores[1][0]]
    for i in range(len(df)):
        idx = sim_scores[i][0]
        ranked_titles = pd.concat([ranked_titles, movies_df[movies_df.index == idx]])
        
    # Reset index to adjust for new movie order
    ranked_titles.reset_index(drop=True, inplace=True)
        
    return ranked_titles