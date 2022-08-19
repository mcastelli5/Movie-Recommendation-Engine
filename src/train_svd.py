import src.config as config
import os
import pandas as pd
import joblib
from surprise import Dataset
from surprise import Reader
from surprise.model_selection import cross_validate
from surprise import SVD

def train_svd():
    """
    summary: train svd model on current movies and user ratings for collaborative filtering / hybrid option in recommnedation engine
    """
    
    # Ingest all inputs
    ratings = pd.read_csv(config.TRAINING_FILE_RATINGS)
    
    # Instantiate reader object and svd object
    reader = Reader(rating_scale=(1, 5))

    # Load data into surprise dataset format with reader
    data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)

    svd = SVD(n_epochs=5)
    cross_validate(svd, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)

    # Train the model on the entire dataset by converting the CF dataset into a Surprice Trainset object
    trainset = data.build_full_trainset()
    svd.fit(trainset)
    
    # Save model to model directory for later usage
    joblib.dump(
        svd,
        os.path.join(config.MODEL_OUTPUT, "svd.bin")
    )