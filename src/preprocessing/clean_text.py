# Cleaning text using Reg-Ex

import re


def clean_text(data):
    corpus = []
    for i in range(len(data)):
        # Removing non-word characters
        tweet = re.sub(r"\W", " ", str(data[i]))
        corpus.append(tweet)
    return corpus



