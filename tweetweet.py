import tweepy
import time

# Replace the following with your own access codes from Twitter:
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Gets your own data from Twitter
user = api.me()
print(user.name)
print(user.screen_name)
print(user.followers_count)

search = "japanese"
numberOfTweets = 2


def limit_handler(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(1000)


# Be nice to your followers. Follow everyone!
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.name == 'Usernamehere':
        print(follower.name)
        follower.follow()

# Be a narcisist and love your own tweets. or retweet anything with a keyword!
for tweet in limit_handler(tweepy.Cursor(api.search, search).items(numberOfTweets)):
    try:
        tweet.favorite()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
