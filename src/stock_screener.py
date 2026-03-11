import pandas as pd
from src.data_loader import load_stock
from src.indicators import moving_average, compute_rsi
from src.lstm_model import train_lstm, predict_next_price


def screen_stocks(symbols):

    results = []

    for symbol in symbols:

        try:

            data = load_stock(symbol)

            data.columns = data.columns.get_level_values(0)

            data = moving_average(data, 20)
            data = moving_average(data, 50)
            data = compute_rsi(data)

            current_price = data["Close"].iloc[-1]

            # LSTM prediction
            model, scaler = train_lstm(data)
            prediction = predict_next_price(model, scaler, data)

            rsi = data["RSI"].iloc[-1]
            ma20 = data["MA20"].iloc[-1]
            ma50 = data["MA50"].iloc[-1]

            # AI decision logic
            if prediction > current_price and rsi < 70 and ma20 > ma50:
                signal = "Strong Buy"

            elif prediction > current_price:
                signal = "Buy"

            else:
                signal = "Hold"

            results.append({
                "Symbol": symbol,
                "Current Price": round(current_price,2),
                "Predicted Price": round(prediction,2),
                "RSI": round(rsi,2),
                "Signal": signal
            })

        except:
            continue

    return pd.DataFrame(results)