import tweepy
from textblob import TextBlob



consumer_key = 'i8g7flRE838Hgn5Qq5nnXU6qW'
consumer_secret = 'cYZGXIkcrJdPY0ekJ3SoWfG1amKM97jLKIcJq1nPQ0N8r40Ldd'

access_token = '2583536299-2Gn3OZUjI26e75XzyjDrF9PHm04Dq2XGYNOkywi'
access_token_secret = 'N9c0fFHAY6I5GSNdF7mKQY6ecZg9JZLHbyuWdphcspJQU'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


# Step 2 - Retrieve Tweets
# public_tweets = api.search('Yorushika')

# for tweet in public_tweets:
#     print(tweet.text)

#     # Step 3 Perform Sentiment Analysis on Tweets
#     analysis = TextBlob(tweet.text)
#     print(analysis.sentiment)
#     print("")

# Additional Question Solutions:
#Date Input Validation
import datetime
def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")

since_date = validate(input('Enter starting date wihtin last 6-8 days (YYYY-MM-DD): '))
until_date = validate(input('Enter ending date wihtin last 6-8 days (YYYY-MM-DD): '))

# Step 3 - Retrieve Tweets
user_input = input('Which topic would you like to search for on Twitter: ')
public_tweets = api.search(user_input, count = 100, since = since_date , until=until_date)


# Additional Step - Function of labelisation of analysis
def get_label(analysis, threshold=0):
    if analysis.sentiment[0] > threshold:
        return 'Positive'
    else:
        return 'Negative'

total_score = 0
for tweet in public_tweets:
    print(tweet.text)

    # Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment, get_label(analysis))
    total_score = total_score + analysis.sentiment[1]
    print("")

print("average score is", str((total_score/len(public_tweets))))

# # public_tweets = api.search('red sox')
# what = input("what topic")
# public_tweets = api.search(what)

# def detector(sentence):
#     analysis = TextBlob(tweet.text)
#     print(analysis.sentiment)


# # sentence = "ass"
# # analyser = SentimentIntensityAnalyzer()
# # snt = analyser.polarity_scores(sentence)
# # print(sentence, str(snt))

# for tweet in public_tweets:
#     print(tweet.text)
#     # Step 3 Perform Sentiment Analysis on Tweets
#     analysis = detector(tweet.text)


