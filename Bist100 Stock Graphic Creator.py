import datetime as dt
import pandas as pd
import yfinance as yf
import pytz
import plotly.graph_objects as go
import plotly.offline as pyo

# Make `end` timezone-aware
end = dt.datetime.now(pytz.UTC)
start = end - dt.timedelta(days=250)
print(f"Data Range: {start} to {end}")

# Ask the user for a list of stock symbols (comma-separated)
user_input = input("Enter stock symbols separated by commas (e.g., VAKKO, DOCO, FROTO, SASA): ")
stocklist = [symbol.strip().upper() for symbol in user_input.split(',')]
stocks = [i + ".IS" for i in stocklist]  # Adjust for Turkish stocks on Yahoo Finance

print(f"Selected Stocks: {stocks}")

# Use yfinance directly to download the data
df = yf.download(stocks, start=start, end=end)

# Check if data was retrieved
if df.empty:
    print("No data retrieved. Please check your stock symbols.")
else:
    # Access the 'Close' prices
    close = df['Close']
    print("Close Prices Sample:")
    print(close.head())

    # Check if each symbol's data is available
    available_stocks = [stock for stock in stocks if stock in close.columns]
    unavailable_stocks = [stock for stock in stocks if stock not in close.columns]

    if unavailable_stocks:
        print(f"Data not available for: {', '.join(unavailable_stocks)}")

    # Plot using Plotly in offline mode
    fig = go.Figure()

    # Add each stock's Adjusted Close prices to the plot (only if data is available)
    for stock_symbol, original_name in zip(stocks, stocklist):
        if stock_symbol in available_stocks:
            fig.add_trace(go.Scatter(
                x=close.index,
                y=close[stock_symbol],
                mode='lines',
                name=original_name  # Use the original name provided by the user for clarity
            ))
        else:
            print(f"Skipping {original_name} as no data is available.")

    # Update layout for better visualization
    fig.update_layout(
        title='Stock Adjusted Close Prices Over the Last 250 Days',
        xaxis_title='Date',
        yaxis_title='Adjusted Close Price',
        legend_title='Stock Symbol',
        template='plotly_dark',
        width=1200,
        height=800
    )

    # Display the interactive plot offline and save it to an HTML file
    pyo.plot(fig, filename='stock_prices.html', auto_open=True)
