import feedparser
from textblob import TextBlob


def fetch_news(symbol):

    url = f"https://news.google.com/rss/search?q={symbol}+stock"

    feed = feedparser.parse(url)

    news_list = []

    for entry in feed.entries[:5]:
        news_list.append(entry.title)

    return news_list
def analyze_sentiment(news):

    if not news:   # FIX: handle empty news
        return "No news found"

    total_score = 0

    for article in news:

        analysis = TextBlob(article)

        total_score += analysis.sentiment.polarity

    score = total_score / len(news)

    if score > 0.1:
        return "Bullish 📈"

    elif score < -0.1:
        return "Bearish 📉"

    else:
        return "Neutral ⚖"