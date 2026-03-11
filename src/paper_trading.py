import pandas as pd
import yfinance as yf

portfolio = {
    "cash": 10000,
    "positions": {}
}


def buy_stock(symbol, amount):

    price = yf.Ticker(symbol).history(period="1d")["Close"].iloc[-1]

    shares = amount // price

    cost = shares * price

    if portfolio["cash"] >= cost:

        portfolio["cash"] -= cost

        portfolio["positions"][symbol] = portfolio["positions"].get(symbol, 0) + shares

        return f"Bought {shares} shares of {symbol}"

    return "Not enough balance"


def sell_stock(symbol):

    if symbol in portfolio["positions"]:

        price = yf.Ticker(symbol).history(period="1d")["Close"].iloc[-1]

        shares = portfolio["positions"][symbol]

        portfolio["cash"] += shares * price

        del portfolio["positions"][symbol]

        return f"Sold {shares} shares of {symbol}"

    return "Stock not owned"


def portfolio_value():

    total = portfolio["cash"]

    for symbol, shares in portfolio["positions"].items():

        price = yf.Ticker(symbol).history(period="1d")["Close"].iloc[-1]

        total += shares * price

    return total