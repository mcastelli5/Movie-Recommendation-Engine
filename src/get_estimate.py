import joblib
import src.config as config

model = joblib.load(config.SVD_MODEL)

def get_estimate(similar_users, movie):
    """
    Summary:
        provide user rating estimates on each movie that is in the movies dataframe based on similar user ratings (with trained model).

    Args:
        similar_users (list): users that rated the current users favorite movie similarly
        movie (str): string value to represent the movie being estimated
    """
    
    global model
    total_est = 0
    num_similar = len(similar_users)
    if not num_similar:
        return total_est
    
    for user in similar_users:
        est = model.predict(uid=user, iid=movie).est
        total_est += est
    
    return total_est / num_similar