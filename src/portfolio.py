# import yfinance as yf
# import pandas as pd


# def load_portfolio(symbols):

#     data = yf.download(symbols, start="2020-01-01")['Close']

#     return data
# def calculate_returns(data):

#     returns = data.pct_change().dropna()

#     return returns
# def portfolio_risk(returns):

#     volatility = returns.std() * (252 ** 0.5)

#     return volatility