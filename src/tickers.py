ticker_map = {
    "Apple": "AAPL",
    "Tesla": "TSLA",
    "Microsoft": "MSFT",
    "Amazon": "AMZN",
    "Google": "GOOGL",
    "Nvidia": "NVDA",
    "Meta": "META",
    "Netflix": "NFLX",
    "AMD": "AMD",
    "Intel": "INTC"
}

def search_ticker(query):

    results = {}

    for company, ticker in ticker_map.items():

        if query.lower() in company.lower():
            results[company] = ticker

    return results