"""Module to train model and make predictions on tweet embeddings"""

from .models import User
import numpy as np
import pickle
from sklearn.sklearn.linear_model import LogisticRegression
from .twtter import BASILICA

def predict_user(u1_name, u2_name, tweet_text, cache=None):
    """Predict which use is more likely to post tweet in tweet_text"""
    user_set = pickle.dumps((u1_name, u2_name))
    if cache and cache.exists(user_set):
        log_reg = pickle.loads(cache.get(user_set))
    else:
        u1 = User.query.filter(User.name = u1_name).one()
        u2 = User.query.filter(User.name = u2_name).one()
        u1.embeddings = np.array([tweet.embeddings for tweet in u1.tweets])
        u2.embeddings = np.array([tweet.embeddings for tweet in u2.tweets])
        embeddings = np.vstack([u1.embeddings, u2.embeddings])
        labels = np.concatenate([np.ones(len(u1.tweets)),
                                 np.zeroes(len(u2.tweets))])
        log_reg = LogisticRegression().fit(embeddings,labels)
        cache and cache.set(user_set, pickle.dumps(log_reg))
        tweet_embeddings = BASILICA.get_sentence(tweet_text, model='twitter')

        return log_reg.predict(np.array(tweet_text).reshape(1,-1))
        


    

