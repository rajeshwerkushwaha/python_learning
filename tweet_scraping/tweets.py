import tweepy

consumer_key = '3SwBAiBII4vdIyHEoSv5gVeIW'
consumer_secret = 'nMAy5ClaLEF6jcmTZrRRL1CDi5NmZkW8whHMCVgwffUzQv1AIU'
access_token = '1553756329-jvla3TCgPGOplC6vkloFy1Khay93ldwu0ltqx66'
access_token_secret = 'uhnvmDI2X7EcqZe2lrbHLdWkd9UDvKxaYRWLZ9ryQwEEr'

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