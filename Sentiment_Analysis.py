import tweepy
from textblob import TextBlob
consumer_key ='WuwoFCPwLzw2VFzhzLrnDbIye'
consumer_secret='Yt32xjre4ws9kq0SN6LOIMT3nc5fHFjZ3qcJ510SYin9XmR0bO'
access_token='1011001660066451456-6hrbsrzm6GktJG2ChjWnPgHQQRFNzB'
access_token_secret='AXO0xBMrLeIkx64DEXetfpptYMUbvXrBXGR5grzTdVHVh'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

tweets = api.search('worldcup')

for tweet in tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)