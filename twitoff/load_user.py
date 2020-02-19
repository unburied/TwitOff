"""load user and tweet data into db"""

import pickle
from .twitter import *

def load_user(user_name, cache=None): 
    # check if user data cached to improve tweet fetching and basilica performance
    user_pickle = pickle.dumps(user_name)

    if cache and cache.exists(user_pickle):       
        u = pickle.loads(cache.get(user_pickle))

        tweets = u['tweet_bucket']
        db_user = User(id=u['id'], name=u['name'], newest_tweet_id=u['nt_id'])
        
        for t in tweets:
            db_tweet = Tweet(id=t['t_id'], text=t['text'], embedding=t['embedding'])
            DB.session.add(db_tweet)
            db_user.tweets.append(db_tweet)
        
    else:
        # get user data
        u = user_data(user_name)
        tweets = u['tweets']
        db_user = User(id=u['id'], name=u['name'], newest_tweet_id=u['nt_id'])

        # embed tweets and load database
        for tweet in tweets:
            t = tweet_data(tweet)
            db_tweet = Tweet(id=t['t_id'], text=t['text'], embedding=t['embedding'])
            DB.session.add(db_tweet)
            db_user.tweets.append(db_tweet)

            #for caching
            u['tweet_bucket'].append(t)
            cache and cache.set(user_pickle, pickle.dumps(u))


    # load user and commit
    DB.session.add(db_user)
    DB.session.commit()

def user_data(user_name):
    """Use API to fetch user data and load into dict"""
    data = {}
    twitter_user = TWITTER.get_user(user_name)

    data['id'] = twitter_user.id
    data['name'] = twitter_user.screen_name
    data['tweets'] = twitter_user.timeline(count=200, exclude_replies=True,
                                    include_rts=False, tweet_mode='extended')
    data['nt_id'] = newest_tweet_id=data['tweets'][0].id
    data['tweet_bucket'] = [] # for caching
    
    return data

def tweet_data(tweet):
    """Use basilica to embed text from tweet"""
    data = {}
    data['t_id'] = tweet.id
    data['text'] = tweet.full_text[:500]
    data['embedding'] = BASILICA.embed_sentence(tweet.full_text, model='twitter')

    return data

"""I didnt time it before the changes, but I think it saves a few seconds"""
