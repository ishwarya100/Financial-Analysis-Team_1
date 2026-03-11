import pandas as pd


def moving_average(data, window):

    data[f"MA{window}"] = data["Close"].rolling(window).mean()

    return data

def compute_rsi(data, period=14):

    # ensure Close is a Series (not DataFrame)
    close = data["Close"]

    if isinstance(close, pd.DataFrame):
        close = close.iloc[:, 0]

    delta = close.diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    rs = avg_gain / avg_loss

    rsi = 100 - (100 / (1 + rs))

    data["RSI"] = rsi

    return data
def bollinger_bands(data):

    data['MA20'] = data['Close'].rolling(20).mean()

    data['STD'] = data['Close'].rolling(20).std()

    data['UpperBand'] = data['MA20'] + (2 * data['STD'])
    data['LowerBand'] = data['MA20'] - (2 * data['STD'])

    return data