from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

scores = SentimentIntensityAnalyzer()

print(scores.polarity_scores("high full toss outside off, surprises him as he misses, but it was below waist high, he is out!"))