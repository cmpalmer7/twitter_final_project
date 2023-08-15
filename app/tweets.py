import tweepy
from transformers import pipeline
from statistics import mean
from app.alpha import BEARER_TOKEN
import plotly.express

#Help from https://www.youtube.com/watch?v=0EekpQBEP_8
#Help from https://favtutor.com/blogs/get-list-index-python#:~:text=The%20index()%20method%20returns,index('item_name').

def to_percent(numerator,denominator):
    """
    Takes a numerator and denominator and returns a formatted percentage
    """
    
    return f"{round((numerator/denominator)*100)}%"

if __name__ == "__main__":

    specific_model = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")


    client = tweepy.Client(BEARER_TOKEN)

    keyword = input("What would you like to search for, please be specific: ")

    query = (f"{keyword} -is:retweet")

    response = client.search_recent_tweets(query=query, max_results=100)

    tweets = []
    scores = []
    pos_score_type = []
    neg_score_type = []
    neu_score_type = []


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
            neu_score_type.append(x['label'])

    neg_tweet = scores.index(min(scores))

    pos_tweet = scores.index(max(scores))

    print(f"KEYWORD: {keyword}")

    print(f"NUMBER OF TWEETS: {len(scores)}")

    print(f"AVERAGE SCORE: {round(mean(scores),3)}")

    print(f"PERCENTAGE POSITIVE SENTIMENT: {to_percent(len(pos_score_type),len(scores))}")

    print(f"MOST NEGATIVE SCORE: {round(min(scores),3)} - {tweets[int(neg_tweet)]}")

    print(f"MOST POSITIVE SCORE: {round(max(scores),3)} - {tweets[int(pos_tweet)]}")

    score_types = ["Positive", "Neutral", "Negative"]

    score_counts = [len(pos_score_type)/len(scores),len(neu_score_type)/len(scores),len(neg_score_type)/len(scores)]

    fig = plotly.express.bar(x=score_types, y=score_counts, title=f"Sentiment Analysis for: {keyword}", labels={"x":"Sentiment Type", "y":"Percentage of Tweets"})

    fig.show()