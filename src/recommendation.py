def generate_signal(data, predicted_price):

    current_price = data['Close'].iloc[-1]

    rsi = data['RSI'].iloc[-1]

    ma20 = data['MA20'].iloc[-1]

    ma50 = data['MA50'].iloc[-1]


    # Basic logic

    if predicted_price > current_price and rsi < 70 and ma20 > ma50:
        signal = "BUY"

    elif predicted_price < current_price and rsi > 30 and ma20 < ma50:
        signal = "SELL"

    else:
        signal = "HOLD"

    return signal, current_price