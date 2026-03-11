# AI Stock Market Analyzer

## Overview

The AI Stock Market Analyzer is a comprehensive financial platform designed to provide a quick overview of the stock market so users can understand overall market trends.

The application helps investors analyze the performance of a particular stock using technical indicators, predicts the future stock price using machine learning models, and automatically finds potential investment opportunities. 

This project is built utilizing modern data and visualization libraries, specifically Streamlit, Pandas, Plotly, and yFinance.

## Features

### 1. Market Dashboard

Provides a quick visual overview of stock movement.

#### Key Features

- Displays top gainers and top losers.
- Shows market performance charts.
- Visualizes data using bar charts for market performance and tables for gainers and losers.
- Fetches stock data using the Yahoo Finance API (yfinance) to calculate percentage changes.

### 2. Stock Analyzer

Helps investors analyze the performance of a particular stock using technical indicators.

#### Key Features

- Historical stock price analysis.
- Interactive price charts including a price trend chart.
- Technical indicators table.

#### Technical Indicators Used

- Moving Average (MA20, MA50) for trend analysis.
- RSI for overbought/oversold detection.
- Bollinger Bands for price volatility.

### 3. AI Stock Prediction

Predicts the future stock price using machine learning models.

#### Models Used

- Linear Regression: Uses historical stock prices to fit a regression model, detect trends, and predict the next price.
- LSTM Neural Network: A deep learning recurrent neural network that captures long-term dependencies in stock price sequences.

### 4. Trading Simulation & Paper Trading

#### Trading Simulation Mode
- Provides buy, sell, or hold recommendations based on AI predictions and technical indicators.
- Outputs actionable signals to help investors make decisions quickly.

#### Paper Trading
- Simulates real trading without real money.
- Users invest virtual money and the system records positions.
- Portfolio value is calculated dynamically based on cash and current stock values.

### 5. News Sentiment Analysis

Analyzes financial news sentiment related to a stock.

#### How it Works

- News articles are collected for the selected stock.
- Natural Language Processing (NLP) is used to classify sentiment.
- Sentiment is categorized into Positive, Neutral, or Negative to gauge market influence.

### 6. Watchlist System

Allows users to track their favorite stocks.

#### Key Features

- Add or remove stocks from a custom list.
- Live price updates.
- Price alert system that triggers a notification if the price crosses a set threshold.

### 7. AI Stock Screener

Automatically finds potential investment opportunities.

#### Key Features

- Scans multiple stocks simultaneously.
- Applies AI predictions and technical indicators.
- Filters and recommends the best stocks based on factors like RSI, moving averages, and predicted price changes.

### 8. Portfolio Optimizer

Suggests optimal asset allocation for an investment portfolio.

#### How it Works

- Uses financial optimization models like mean-variance optimization.
- Fetches stock returns, computes expected return, calculates the covariance matrix, and determines optimal stock weights.

### 9. Find Ticker Feature

Helps users easily search for stock ticker symbols using company names.

#### How it Works

- The user enters a company name.
- The system searches a predefined database and returns matching stock tickers to improve usability for beginners.

## Project Structure
```
ai-stock-analyzer/
│
├── app.py                       # Main Streamlit application entry point
├── doc.pdf                      # Project documentation/specification
├── README.md                    # Project overview and setup instructions
│
├── src/                         # Source code for modular components
│   ├── __init__.py              # Makes src a Python package
│   ├── data_loader.py           # Functions for fetching stock data via yFinance
│   ├── indicators.py            # Logic for MA, RSI, and Bollinger Bands
│   ├── predictor.py             # Linear Regression model training and prediction
│   ├── lstm_model.py            # Deep learning LSTM model architecture and training
│   ├── recommendation.py        # Trading signal logic (Buy/Sell/Hold)
│   ├── news_sentiment.py        # NLP-based news fetching and sentiment analysis
│   ├── watchlist.py             # CRUD operations for the user watchlist system
│   ├── stock_screener.py        # Multi-stock scanning and filtering logic
│   ├── portfolio_optimizer.py   # Mean-variance optimization algorithms
│   ├── paper_trading.py         # Virtual cash and portfolio management
│   ├── trading_simulator.py     # Backtesting strategies against historical data
│   ├── market_dashboard.py      # Global market overview and gainer/loser logic
│   ├── market_sentiment.py      # High-level bullish/bearish market gauges
│   └── tickers.py               # Search utility for company-to-ticker mapping
│
└── requirements.txt             # List of Python dependencies
```

## Installation
#### 1. Clone the repository to your local machine:
   ```bash
   git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/ishwarya100/Financial-Analysis-Team_1.git)
   cd your-repo-name
```
#### 2. Create and activate a virtual environment (recommended):
##### On macOS and Linux
```
python3 -m venv venv
source venv/bin/activate
```
##### On Windows
```
python -m venv venv
venv\Scripts\activate
```
#### 3. Install the required dependencies:
```
pip install -r requirements.txt
```
## How to Run
Ensure your virtual environment is activated.
```
streamlit run app.py
```
Open your web browser and navigate to the local URL provided in your terminal (typically http://localhost:8501)

-------------------------------------------------------------------------------------------------------------------
### Note ❗
**This application is for educational purposes only and should not be used for real investment decisions.**


Developed by **Team Byte Storms**.


*Thank you for exploring this project :)*
