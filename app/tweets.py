import tweepy
from transformers import pipeline
from statistics import mean
from app.alpha import BEARER_TOKEN

specific_model = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")


client = tweepy.Client(BEARER_TOKEN)

keyword = input("What would you like to search for, please be specific: ")

query = (f"{keyword} -is:retweet")

response = client.search_recent_tweets(query=query, max_results=50)

tweets = []
scores = []
pos_score_type = []
neg_score_type = []


for t in response.data:
  tweets.append(t["text"])

data_analysis = specific_model(tweets)

for x in data_analysis:
  if x['label'] == 'POS':
    scores.append(x['score'])
    pos_score_type.append(x['label'])
  elif x['label'] == 'NEG':
    scores.append(x['score']*-1)
    neg_score_type.append(x['label'])
  else:
    scores.append(0)

neg_tweet = scores.index(min(scores))

pos_tweet = scores.index(max(scores))

print(f"KEYWORD: {keyword}")

print(f"NUMBER OF TWEETS: {len(scores)}")

print(f"AVERAGE SCORE: {round(mean(scores),3)}")

print(f"PERCENTAGE POSITIVE SENTIMENT: {round(len(pos_score_type)/(len(scores))*100)}%")

print(f"MOST NEGATIVE SCORE: {round(min(scores),3)} - {tweets[int(neg_tweet)]}")

print(f"MOST POSITIVE SCORE: {round(max(scores),3)} - {tweets[int(pos_tweet)]}")