import numpy as np
import pandas as pd
import yfinance as yf


def optimize_portfolio(symbols):

    data = yf.download(symbols, period="1y")["Close"]

    returns = data.pct_change().dropna()

    mean_returns = returns.mean()
    cov_matrix = returns.cov()

    num_assets = len(symbols)

    weights = np.random.random(num_assets)
    weights /= np.sum(weights)

    portfolio_return = np.sum(mean_returns * weights) * 252
    portfolio_volatility = np.sqrt(
        np.dot(weights.T, np.dot(cov_matrix * 252, weights))
    )

    allocation = pd.DataFrame({
        "Stock": symbols,
        "Weight": weights
    })

    allocation["Weight"] = allocation["Weight"] * 100

    return allocation, portfolio_return, portfolio_volatility