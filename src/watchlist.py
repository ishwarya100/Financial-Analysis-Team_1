import pandas as pd
import yfinance as yf
import os

WATCHLIST_FILE = "data/watchlist.csv"


def load_watchlist():

    if os.path.exists(WATCHLIST_FILE):
        return pd.read_csv(WATCHLIST_FILE)

    else:
        return pd.DataFrame(columns=["Symbol", "AlertPrice"])


def save_watchlist(df):

    df.to_csv(WATCHLIST_FILE, index=False)


def add_stock(symbol, alert_price):

    df = load_watchlist()

    if symbol not in df["Symbol"].values:
        new_row = pd.DataFrame(
            [[symbol, alert_price]],
            columns=["Symbol", "AlertPrice"]
        )

        df = pd.concat([df, new_row], ignore_index=True)

    save_watchlist(df)


def remove_stock(symbol):

    df = load_watchlist()

    df = df[df["Symbol"] != symbol]

    save_watchlist(df)


def get_live_prices(symbols):

    prices = {}

    for s in symbols:

        try:

            ticker = yf.Ticker(s)

            data = ticker.history(period="1d")

            if data.empty:
                prices[s] = None
            else:
                prices[s] = float(data["Close"].iloc[-1])

        except Exception:

            prices[s] = None

    return prices