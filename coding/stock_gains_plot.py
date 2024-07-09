# filename: stock_gains_plot.py
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Define the ticker symbols
symbols = ['NVDA', 'TSLA']

# Define the start of the year
start_date = '2024-01-01'
end_date = '2024-07-09'
# Load the data
data = yf.download(symbols, start=start_date, end=end_date)

# Calculate the YTD gain as a percentage
ytd_gains = (data['Adj Close'].pct_change() + 1).cumprod() * 100

# Plot the gains
plt.figure(figsize=(10, 5))
for symbol in symbols:
    plt.plot(ytd_gains.index, ytd_gains[symbol], label=f'{symbol} YTD Gain')
plt.title('YTD Stock Gains 2024')
plt.xlabel('Date')
plt.ylabel('Gain %')
plt.legend()
plt.grid(True)

# Save the figure
plt.savefig('ytd_stock_gains.png')
print("Plot has been saved as 'ytd_stock_gains.png'.")