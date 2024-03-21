import yfinance as yf
import json
from datetime import datetime


def get_stock_prices(ticker, days):
    try:
        # Fetch stock data
        stock_data = yf.download(ticker, period=f"{days}d", interval="1d")

        # Format the DateTimeIndex to dd/mm/yyyy format
        stock_data.index = stock_data.index.strftime("%d/%m/%Y")

        # Convert to JSON format, ensuring dates are strings
        stock_json = stock_data.to_json(orient="index")

        # Parse JSON string to JSON object
        stock_prices = json.loads(stock_json)

        return stock_prices

    except Exception as e:
        return {"error": str(e)}


# Example usage:
ticker = "AAPL"  # Example ticker
days = 30  # Example number of days
prices = get_stock_prices(ticker, days)
print(prices)
