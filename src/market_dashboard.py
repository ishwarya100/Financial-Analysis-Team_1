import yfinance as yf
import pandas as pd

def market_overview():

    # Popular stocks to track
    symbols = [
        "AAPL","MSFT","NVDA","TSLA","GOOGL",
        "AMZN","META","AMD","NFLX","INTC"
    ]

    data = yf.download(symbols, period="1d", interval="1m")["Close"]

    latest = data.iloc[-1]
    prev = data.iloc[0]

    change = ((latest - prev) / prev) * 100

    df = pd.DataFrame({
        "Stock": symbols,
        "Price": latest.values,
        "Change %": change.values
    })

    df = df.sort_values("Change %", ascending=False)

    gainers = df.head(5)
    losers = df.tail(5)

    return df, gainers, losers