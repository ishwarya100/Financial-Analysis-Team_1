import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import yfinance as yf

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="AI Stock Market Analyzer",
    page_icon="📈",
    layout="wide"
)

# -----------------------------
# TITLE
# -----------------------------

st.markdown("""
<h1 style='text-align:center;color:#00A8E8;'>
📈 AI Stock Market Analyzer
</h1>
""", unsafe_allow_html=True)

st.markdown(
"<h4 style='text-align:center;'>Intelligent Financial Analytics Platform</h4>",
unsafe_allow_html=True
)

# -----------------------------
# DASHBOARD CARDS
# -----------------------------

st.markdown("""
<style>

.card {
background: linear-gradient(135deg,#1f2c4c,#2a5298);
padding:20px;
border-radius:15px;
text-align:center;
color:white;
box-shadow:0px 6px 18px rgba(0,0,0,0.3);
}

.card h3{
font-size:30px;
margin-bottom:5px;
}

.card p{
font-size:16px;
opacity:0.9;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# IMPORT MODULES
# -----------------------------

from streamlit_autorefresh import st_autorefresh
from src.data_loader import load_stock
from src.indicators import moving_average, compute_rsi, bollinger_bands
from src.predictor import train_model, predict_price
from src.lstm_model import train_lstm, predict_next_price,build_lstm_model,prepare_lstm_data
from src.recommendation import generate_signal
from src.news_sentiment import fetch_news, analyze_sentiment
# from src.portfolio import load_portfolio, calculate_returns, portfolio_risk
from src.watchlist import load_watchlist, add_stock, remove_stock, get_live_prices
from src.stock_screener import screen_stocks
from src.tickers import search_ticker
from src.trading_simulator import simulate_trading, compare_strategies
from src.paper_trading import buy_stock, sell_stock, portfolio_value, portfolio
from src.portfolio_optimizer import optimize_portfolio
from src.market_dashboard import market_overview
from src.market_sentiment import market_sentiment

# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.title("📊 AI Trading Dashboard")
st.sidebar.markdown("Select a feature below")
tickers = ["AAPL", "TSLA", "MSFT", "NVDA", "GOOGL"]

ticker_text = ""

for t in tickers:
    try:
        ticker = yf.Ticker(t)
        data = ticker.history(period="2d")

        if data is None or data.empty:
            continue

    except Exception as e:
        print("Ticker fetch error:", t)
        continue

    if len(data) >= 2:

        price = data["Close"].iloc[-1]
        prev = data["Close"].iloc[-2]

        change = ((price - prev) / prev) * 100
        arrow = "▲" if change > 0 else "▼"

        ticker_text += f"{t} {arrow} {change:.2f}%   |   "

    else:

        ticker_text += f"{t} data unavailable | "
st.markdown(
f"""
<div style="background:#111;padding:10px;border-radius:10px;font-size:18px">
{ticker_text}
</div>
""",
unsafe_allow_html=True
)
menu = st.sidebar.radio(
    "Navigation",
    [
        "📊 Market Dashboard",
        "📈 Stock Analyzer",
        "🤖 AI Prediction",
        "📰 News Sentiment",
        # "💼 Portfolio Analyzer",
        "⭐ Watchlist",
        "🤖 AI Stock Screener",
        "💹 Trading Simulator",
        "💰 Paper Trading",
        "📊 Portfolio Optimizer"
    ]
)

# ---------------------------------------------------
# MARKET DASHBOARD
# ---------------------------------------------------

if menu == "📊 Market Dashboard":

    # DASHBOARD CARDS
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="card">
            <h3>11</h3>
            <p>📊 Features</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3>2</h3>
            <p>🤖 AI Models</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <h3>2</h3>
            <p>📈 Strategies</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="card">
            <h3>2</h3>
            <p>💰 Trading Modes</p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # PLATFORM OVERVIEW
    st.subheader("📊 Platform Overview")

    st.markdown("""
    This platform provides **AI-powered stock market analysis** with:

    • 📈 Stock trend analysis  
    • 🤖 Machine learning price prediction  
    • 📰 News sentiment analysis  
    • ⭐ Watchlist monitoring  
    # • 💼 Portfolio analysis  
    • 💹 Trading strategy simulation  
    • 💰 Paper trading  

    Use the **sidebar navigation** to explore each feature.
    """)

    # MARKET PREVIEW
    st.subheader("📈 Market Trend Preview")

    preview_data = yf.download("AAPL", period="6mo")

    preview_data.columns = preview_data.columns.get_level_values(0)

    fig = px.line(
        preview_data,
        y="Close",
        title="Apple Stock Trend (Last 6 Months)"
    )

    st.plotly_chart(fig, use_container_width=True)

    # YOUR EXISTING MARKET DATA
    df, gainers, losers = market_overview()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🚀 Top Gainers")
        st.dataframe(gainers)

    with col2:
        st.subheader("📉 Top Losers")
        st.dataframe(losers)
# ---------------------------------------------------
# STOCK ANALYZER
# ---------------------------------------------------

# elif menu == "📈 Stock Analyzer":

#     st.header("📈 Stock Market Analyzer")

#     symbol = st.text_input("Enter Stock Symbol", "AAPL").upper()

#     if st.button("Analyze Stock"):

#         data = load_stock(symbol)
#         data.columns = data.columns.get_level_values(0)
#         data["Date"] = pd.to_datetime(data["Date"])

#         data = moving_average(data,20)
#         data = moving_average(data,50)
#         data = compute_rsi(data)
#         data = bollinger_bands(data)

#         tab1, tab2 = st.tabs(["📈 Price Chart", "📊 Indicators"])

#         with tab1:

#             fig = px.line(data, x="Date", y="Close")
#             st.plotly_chart(fig)

#         with tab2:

#             st.dataframe(data.tail())
# ---------------------------------------------------
# AI STOCK SCREENER
# ---------------------------------------------------
elif menu == "🤖 AI Stock Screener":

    st.header("🤖 AI Stock Screener")

    default_stocks = "AAPL,MSFT,NVDA,TSLA,GOOGL,AMZN"

    symbols_input = st.text_input(
        "Enter stocks to scan (comma separated)",
        default_stocks
    )

    if st.button("Run AI Screener"):

        symbols = [s.strip() for s in symbols_input.split(",")]

        st.info("Scanning stocks using AI...")

        results = screen_stocks(symbols)

        st.subheader("AI Stock Picks")

        st.dataframe(results)

        strong_buys = results[results["Signal"] == "Strong Buy"]

        if not strong_buys.empty:

            st.success("🔥 Strong Buy Stocks")

            st.dataframe(strong_buys)

elif menu == "📊 Portfolio Optimizer":

    st.header("📊 Portfolio Optimizer")

    stocks = st.text_input(
        "Enter Stocks",
        "AAPL,MSFT,NVDA,TSLA"
    )

    if st.button("Optimize Portfolio"):

        symbols = [s.strip() for s in stocks.split(",")]

        allocation, ret, vol = optimize_portfolio(symbols)

        st.subheader("Recommended Allocation")

        st.dataframe(allocation)

        st.metric("Expected Return", f"{ret:.2%}")
        st.metric("Portfolio Risk", f"{vol:.2%}")

        fig = px.pie(
            allocation,
            values="Weight",
            names="Stock"
        )

        st.plotly_chart(fig)
# ---------------------------------------------------
# PAPER TRADING
# ---------------------------------------------------
elif menu == "💰 Paper Trading":

    st.header("💰 Paper Trading")

    st.metric("Cash Balance", f"${portfolio['cash']:.2f}")

    symbol = st.text_input("Stock", "AAPL")
    amount = st.number_input("Amount", value=1000)

    col1, col2 = st.columns(2)

    if col1.button("Buy"):
        st.success(buy_stock(symbol, amount))

    if col2.button("Sell"):
        st.warning(sell_stock(symbol))

    st.subheader("Portfolio")
    st.write(portfolio["positions"])

    total = portfolio_value()

    st.metric("Total Portfolio Value", f"${total:.2f}")
# ---------------------------------------------------
# AI PREDICTION
# ---------------------------------------------------

elif menu == "🤖 AI Prediction":

    st.header("🤖 AI Stock Prediction")

    symbol = st.text_input("Enter Stock Symbol","AAPL")

    if st.button("Predict"):

        data = load_stock(symbol)
        data.columns = data.columns.get_level_values(0)

        data = moving_average(data,20)
        data = moving_average(data,50)
        data = compute_rsi(data)

        with st.spinner("Training AI Model..."):

            model, scaler = train_lstm(data)
            lstm_prediction = predict_next_price(model, scaler, data)

        signal,current_price = generate_signal(data,lstm_prediction)

        rsi = data["RSI"].iloc[-1]

        col1,col2,col3 = st.columns(3)

        col1.metric("Current Price",f"${current_price:.2f}")
        col2.metric("Predicted Price",f"${lstm_prediction:.2f}")
        col3.metric("RSI",f"{rsi:.2f}")

        if signal=="BUY":
            st.success("📈 BUY Signal")
        elif signal=="SELL":
            st.error("📉 SELL Signal")
        else:
            st.warning("⚠ HOLD Signal")

        sentiment = market_sentiment(data,lstm_prediction)

        st.subheader("Market Sentiment")

        if sentiment == "Bullish 📈":
            st.success(sentiment)
        elif sentiment == "Bearish 📉":
            st.error(sentiment)
        else:
            st.warning(sentiment)

# ---------------------------------------------------
# OTHER FEATURES (UNCHANGED)
# ---------------------------------------------------

elif menu == "📰 News Sentiment":

    st.header("📰 News Sentiment Analysis")

    symbol = st.text_input("Stock Symbol","AAPL")

    if st.button("Fetch News"):

        news = fetch_news(symbol)

        for n in news:
            st.write("-",n)

        sentiment = analyze_sentiment(news)

        st.info(sentiment)

elif menu == "💼 Portfolio Analyzer":

    st.header("💼 Portfolio Analyzer")

    symbols_input = st.text_input("Enter stocks","AAPL,TSLA,MSFT")

    if st.button("Analyze"):

        symbols = [s.strip() for s in symbols_input.split(",")]

        data = load_portfolio(symbols)

        returns = calculate_returns(data)
        risk = portfolio_risk(returns)

        st.line_chart(data)
        st.write(risk)

elif menu == "⭐ Watchlist":

    st.header("⭐ Watchlist")

    st_autorefresh(interval=60000,key="watch")

    symbol = st.text_input("Symbol","AAPL")
    alert = st.number_input("Alert Price",value=0.0)

    col1,col2 = st.columns(2)

    if col1.button("Add"):
        add_stock(symbol,alert)
        st.success("Added")

    if col2.button("Remove"):
        remove_stock(symbol)
        st.warning("Removed")

    watchlist = load_watchlist()

    if not watchlist.empty:

        symbols = watchlist["Symbol"].tolist()
        prices = get_live_prices(symbols)

        for i,row in watchlist.iterrows():

            sym=row["Symbol"]
            alert=row["AlertPrice"]
            price=prices.get(sym)

            if price:
                st.write(f"{sym} : ${price:.2f}")

                if alert>0 and price>=alert:
                    st.error(f"{sym} crossed alert price")

elif menu == "💹 Trading Simulator":

    st.header("💹 Trading Simulator")

    symbol = st.text_input("Stock","AAPL")

    initial_cash = st.number_input("Initial Investment",value=10000)

    strategy = st.selectbox("Strategy",["MA Crossover","RSI"])

    if st.button("Run Simulation"):

        final_value,profit,trades = simulate_trading(symbol,strategy,initial_cash)

        st.metric("Final Portfolio Value",f"${final_value:.2f}")
        st.metric("Profit",f"${profit:.2f}")

        st.dataframe(trades)
# ---------------------------------------------------
# SIDEBAR TICKER SEARCH
# ---------------------------------------------------

st.sidebar.subheader("🔎 Find Stock Ticker")

company = st.sidebar.text_input("Company Name")

if company:

    results = search_ticker(company)

    if results:
        for c,t in results.items():
            st.sidebar.write(f"{c} → {t}")
    else:
        st.sidebar.warning("No ticker found")
# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("---")

st.markdown(
"""
<div style='text-align:center'>

📈 **AI Stock Market Analyzer**

Built with **Streamlit • Python • Machine Learning**

</div>
""",
unsafe_allow_html=True
)