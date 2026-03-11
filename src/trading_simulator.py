import pandas as pd
from src.data_loader import load_stock
from src.indicators import moving_average, compute_rsi


def simulate_trading(symbol, strategy="MA Crossover", initial_cash=10000):

    data = load_stock(symbol)

    data.columns = data.columns.get_level_values(0)

    data = moving_average(data, 20)
    data = moving_average(data, 50)
    data = compute_rsi(data)

    cash = initial_cash
    shares = 0
    trade_log = []

    for i in range(1, len(data)):

        price = data["Close"].iloc[i]

        ma20 = data["MA20"].iloc[i]
        ma50 = data["MA50"].iloc[i]

        rsi = data["RSI"].iloc[i]

        # Strategy 1 — Moving Average Crossover
        if strategy == "MA Crossover":

            if ma20 > ma50 and cash > price:

                shares = cash // price
                cash -= shares * price

                trade_log.append({
                    "Action": "BUY",
                    "Price": price,
                    "Date": data["Date"].iloc[i]
                })

            elif ma20 < ma50 and shares > 0:

                cash += shares * price

                trade_log.append({
                    "Action": "SELL",
                    "Price": price,
                    "Date": data["Date"].iloc[i]
                })

                shares = 0

        # Strategy 2 — RSI Strategy
        elif strategy == "RSI":

            if rsi < 30 and cash > price:

                shares = cash // price
                cash -= shares * price

                trade_log.append({
                    "Action": "BUY",
                    "Price": price,
                    "Date": data["Date"].iloc[i]
                })

            elif rsi > 70 and shares > 0:

                cash += shares * price

                trade_log.append({
                    "Action": "SELL",
                    "Price": price,
                    "Date": data["Date"].iloc[i]
                })

                shares = 0

    final_value = cash + shares * data["Close"].iloc[-1]

    profit = final_value - initial_cash

    trades = pd.DataFrame(trade_log)

    return final_value, profit, trades

def compare_strategies(symbol, initial_cash=10000):

    strategies = ["MA Crossover", "RSI"]

    results = []

    for strategy in strategies:

        final_value, profit, trades = simulate_trading(
            symbol,
            strategy,
            initial_cash
        )

        results.append({
            "Strategy": strategy,
            "Final Value": final_value,
            "Profit": profit
        })

    return pd.DataFrame(results)