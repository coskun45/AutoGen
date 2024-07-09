# filename: nvidia_stock_data.py
import yfinance as yf
import pandas as pd

# Set the ticker symbol for Nvidia
ticker_symbol = "NVDA"

# Set the start and end dates
start_date = "2024-03-23"
end_date = "2024-04-23"

# Fetch the historical stock data
nvidia_data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Display the data
print(nvidia_data)

# Optionally, save the data to a CSV file
nvidia_data.to_csv("nvidia_stock_data.csv")