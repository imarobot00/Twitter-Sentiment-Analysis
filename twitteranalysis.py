import numpy as np
import pandas as pd
from textblob import TextBlob

df = pd.read_csv('twitter_training.csv')

fourth_column = df.iloc[:, 3] 

# Assuming you have already loaded your DataFrame and extracted the 4th column into 'fourth_column'

# Filter the DataFrame to select only the rows where the tweet contains either "Borderlands" or "borderlands"
tweets_with_borderlands = fourth_column[fourth_column.str.contains('Borderlands|borderlands', na=False)]

# Create an empty list to store positive polarity tweets
positive_tweets = []

# Iterate over the filtered tweets and perform sentiment analysis
for tweet in tweets_with_borderlands:
    # Check if the tweet is not NaN (assuming NaN values are represented as floats)
    if not pd.isnull(tweet):
        # Convert the tweet to a string and then create a TextBlob object
        analysis = TextBlob(str(tweet))
        # Perform sentiment analysis
        polarity = analysis.sentiment.polarity
        # Check if polarity is positive
        if polarity < 0:
            # Print the tweet and its polarity
            print("Tweet:", tweet)
            print("Polarity:", polarity)
            positive_tweets.append(tweet)
    else:
        print("NaN value encountered, skipping...")

# Now, 'positive_tweets' contains all the tweets with positive polarity

# Convert the list of positive tweets into a DataFrame
positive_tweets_df = pd.DataFrame(positive_tweets, columns=['Positive Tweets'])

# Save the DataFrame to a CSV file
positive_tweets_df.to_csv('positive_tweets.csv', index=False)