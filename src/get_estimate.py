from train_svd import train_svd

def get_estimate(similar_users, movie, model):
    """
    Summary:
        provide user rating estimates on each movie that is in the movies dataframe based on similar user ratings (with trained model).

    Args:
        similar_users (list): users that rated the current users favorite movie similarly
        movie (str): string value to represent the movie being estimated
        model (model): trained model used to estimate the movie in question based on user in question past ratings
    """
    model = train_svd()
    total_est = 0
    num_similar = len(similar_users)
    if not num_similar:
        return total_est
    
    for user in similar_users:
        est = model.predict(uid=user, iid=movie).est
        total_est += est
    
    return total_est / num_similar