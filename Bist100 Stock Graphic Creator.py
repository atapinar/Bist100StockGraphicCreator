import datetime as dt
import pandas as pd
import yfinance as yf
import pytz
import plotly.graph_objects as go
import plotly.offline as pyo

end = dt.datetime.now(pytz.UTC)
start = end - dt.timedelta(days=250)

user_input = input("Enter stock symbols separated by commas (e.g., VAKKO, DOCO, FROTO, SASA): ")
stocklist = [symbol.strip().upper() for symbol in user_input.split(',')]
stocks = [i + ".IS" for i in stocklist]

df = yf.download(stocks, start=start, end=end)

if not df.empty:
    close = df['Close']
    available_stocks = [stock for stock in stocks if stock in close.columns]

    fig = go.Figure()

    for stock_symbol, original_name in zip(stocks, stocklist):
        if stock_symbol in available_stocks:
            fig.add_trace(go.Scatter(
                x=close.index,
                y=close[stock_symbol],
                mode='lines',
                name=original_name
            ))

    fig.update_layout(
        title='Stock Adjusted Close Prices Over the Last 250 Days',
        xaxis_title='Date',
        yaxis_title='Adjusted Close Price',
        legend_title='Stock Symbol',
        template='plotly_dark',
        width=1200,
        height=800
    )

    pyo.plot(fig, filename='stock_prices.html', auto_open=True)
