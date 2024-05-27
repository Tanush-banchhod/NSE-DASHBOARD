# Stock Dashboard

## Overview

The Stock Dashboard is a Streamlit-based web application that allows users to analyze the performance of a specific stock. It provides pricing data, fundamental data, news articles, and sentiment analysis for the specified stock.

## Features

- **Pricing Data**: Displays historical stock prices and calculates key metrics such as annual return, standard deviation, and risk-adjusted return.
- **Fundamental Data**: Shows the balance sheet, income statement, and cash flow statement of the specified stock.
- **Top 10 News**: Provides the latest news articles related to the stock along with sentiment analysis of the news titles and summaries.
- **OpenAI ChatGPT**: Placeholder for potential integration with OpenAI's ChatGPT for additional insights and analysis.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Tanush-banchhod/stock-dashboard.git
   cd stock-dashboard
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
3. Run the streamlit app:
   ```bash
   streamlit run app.py
##Usage

Enter the stock ticker symbol in the sidebar.
Select the start date and end date for the analysis.
Navigate through the tabs to view pricing data, fundamental data, news articles, and sentiment analysis.

##Requirements
Python 3.x
Streamlit
pandas
numpy
yfinance
plotly
alpha_vantage
stocknews
pyChatGPT

##Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
