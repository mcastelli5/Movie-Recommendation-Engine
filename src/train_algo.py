import src.config as config
import os
import pandas as pd
import joblib
from surprise import Dataset
from surprise import Reader
from surprise.model_selection import cross_validate
from surprise import SVD, NMF

def train_algo():
    """
    summary: train svd model on current movies and user ratings for collaborative filtering / hybrid option in recommnedation engine
    """
    
    # Ingest all inputs
    ratings = pd.read_csv(config.TRAINING_FILE_RATINGS)
    
    # Instantiate reader object and svd object
    reader = Reader(rating_scale=(0.5, 5.0))

    # Load data into surprise dataset format with reader
    data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)

    #algo = SVD(n_epochs=5)
    algo = NMF()
    cross_validate(algo, data, measures=['RMSE'], cv=5, verbose=True)

    # Train the model on the entire dataset by converting the CF dataset into a Surprice Trainset object
    trainset = data.build_full_trainset()
    algo.fit(trainset)
    
    # Save model to model directory for later usage
    joblib.dump(
        algo,
        os.path.join(config.MODEL_OUTPUT, "collab_rec.bin")
    )