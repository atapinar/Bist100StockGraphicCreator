# Bist100 Stock Graphic Creator
Borsa Istanbul

# 📈 Plotting Stock Data with Python and Plotly
Project Overview
This project enables users to quickly retrieve and visualize stock price data from the Turkish stock market using Python. With just a list of stock symbols, the script downloads the last 250 days of data for the requested stocks and plots their adjusted close prices using Plotly. The interactive plot is saved as an HTML file, allowing you to explore it offline.

# 💼 Key Features

* Flexible Stock Selection: You can input multiple stock symbols for quick visualization of any Turkish stocks listed on Yahoo Finance.

* Real-Time Data: The script automatically fetches data up to the current date, ensuring that you get the latest prices.

* Interactive Plotting: Using Plotly, the visualization is fully interactive, allowing for zooming, panning, and inspecting values.

* Error Handling: If data for a particular stock is unavailable, the script informs you and skips that stock.

# 📋 Requirements
Ensure you have the following Python libraries installed:

```pandas```: For handling and analyzing the stock data.

```yfinance```: To fetch data from Yahoo Finance.

```pytz```: To manage timezone settings.

```plotly```: For creating interactive visualizations.

# You can install these libraries with:

```
pip install pandas yfinance pytz plotly
```

## 🔧 How to Use the Script
* Set Up Timeframe: The script automatically calculates a 250-day range ending today to capture recent stock performance.

* Enter Stock Symbols: When prompted, enter stock symbols separated by commas. The script will adapt these to Yahoo Finance's format for Turkish stocks (by adding .IS).

* Run the Script: The script fetches adjusted closing prices for each stock. If any data is missing, you'll be notified.

* View the Plot: An interactive plot is generated and saved as an HTML file named stock_prices.html, which will open automatically in your default browser.

# 📊 Sample Output
The generated plot will include a distinct line for each stock’s adjusted closing price.

# 📁 Repository Structure
```
📂 Stock-Data-Visualization

├── README.md                # Project overview and instructions
├── stock_plot.py            # Main script for fetching data and plotting
└── stock_prices.html        # Generated HTML file for offline interactive viewing
```
# 🚀 Future Enhancements
* Customizable Timeframe: Allow users to specify their own start and end dates.
* Multi-Market Support: Enable fetching data from other markets with proper symbol formatting.
* Additional Indicators: Include common indicators like moving averages to enrich the analysis.
