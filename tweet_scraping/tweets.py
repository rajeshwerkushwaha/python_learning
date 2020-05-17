import tweepy

consumer_key = 'CONSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET'
access_token = 'ACCESS_TOKEN'
access_token_secret = 'ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# get public tweets
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)


# # get tweets based on given query
# for tweet in tweepy.Cursor(api.search, q='#corona').items(5):
# 	# print(tweet)
#     print(tweet.text)


# Iterate through all of the authenticated user's friends
for friend in tweepy.Cursor(api.friends).items():
    # Process the friend here
    print(friend.name)



# # Iterate through the first 200 statuses in the home timeline
# for status in tweepy.Cursor(api.home_timeline).items(200):
#     # Process the status here
#     process_status(status)
