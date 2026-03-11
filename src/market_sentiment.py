def market_sentiment(data, predicted_price):

    current_price = data["Close"].iloc[-1]

    ma20 = data["MA20"].iloc[-1]
    ma50 = data["MA50"].iloc[-1]

    rsi = data["RSI"].iloc[-1]

    if predicted_price > current_price and ma20 > ma50 and rsi < 70:
        sentiment = "Bullish 📈"

    elif predicted_price < current_price and ma20 < ma50 and rsi > 30:
        sentiment = "Bearish 📉"

    else:
        sentiment = "Neutral ⚖"

    return sentiment