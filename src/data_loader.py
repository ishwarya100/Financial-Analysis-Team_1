import yfinance as yf
import pandas as pd

def load_stock(symbol):

    try:
        data = yf.download(symbol, period="2y")

        if data is None or data.empty:
            raise ValueError("No data returned")

        data.reset_index(inplace=True)

        return data

    except Exception as e:
        print("Stock fetch error:", e)
        return pd.DataFrame()