# Cleaning text using Reg-Ex

import re


def clean_text(data):
    corpus = []
    for i in range(len(data)):
        # Removing non-word characters
        tweet = re.sub(r"\W", " ", str(data[i]))
        # Converting into lower case
        tweet = tweet.lower()
        # Removing single characters
        tweet = re.sub(r"\s+[a-z]\s+", " ", tweet)
        # Replacing multi-spaces by a single space
        tweet = re.sub(r"\s+", " ", tweet)
        corpus.append(tweet)
    return corpus



