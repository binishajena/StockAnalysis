import yfinance as yf

class DataFetchingAgent:
    def fetch_stock_data(self, ticker):
        stock = yf.Ticker(ticker)
        return stock.history(period="3mo")
