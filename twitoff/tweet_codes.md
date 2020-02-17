twitter_user = TWITTER.get_user('elonmusk')
tweets = twitter_user.timeline(count=200, exclude_replies=True, include_rts=False,mode=extended)
tweets[0].text

ebedding = BASILICA.embed_sentence(tweet[0].text, model= 'twitter')
