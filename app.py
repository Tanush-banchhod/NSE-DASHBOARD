# Importing necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.express as px
from alpha_vantage.fundamentaldata import FundamentalData
from stocknews import StockNews
from pyChatGPT import ChatGPT

# Setting the title of the Streamlit app
st.title("Stock Dashboard")

# Adding sidebar inputs for the user to specify the stock ticker and date range
ticker = st.sidebar.text_input("Ticker")
start_date = st.sidebar.date_input('Start Date')
end_date = st.sidebar.date_input('End Date')

# Downloading stock data from Yahoo Finance based on the user input
data = yf.download(ticker, start=start_date, end=end_date)

# Displaying the stock data
st.write(data)

# Creating a line chart for the Adjusted Close price using Plotly
fig = px.line(data, x=data.index, y=data['Adj Close'], title=ticker)
st.plotly_chart(fig)

# Creating tabs for different sections of the dashboard
pricing_data, fundamental_data, news, openai1 = st.tabs(["Pricing Data", "Fundamental Data", "Top 10 news", "OpenAI ChatGPT"])

# Pricing Data tab
with pricing_data:
    st.write('Price')
    st.header('Price Movements')
    
    # Calculating daily percentage change in Adjusted Close price
    data2 = data.copy()
    data2['%Change'] = data['Adj Close'] / data['Adj Close'].shift(1) - 1
    data.dropna(inplace=True)
    
    # Displaying the data with percentage change
    st.write(data2)
    
    # Calculating and displaying annual return
    annual_return = data2['%Change'].mean() * 252 * 100
    st.write('Annual Return is ', annual_return, '%')
    
    # Calculating and displaying standard deviation
    stdev = np.std(data2['%Change']) * np.sqrt(252)
    st.write("Standard Deviation is ", stdev * 100, '%')
    
    # Calculating and displaying risk-adjusted return
    st.write("Risk Adj. Return is", annual_return / (stdev * 100))

# Fundamental Data tab
with fundamental_data:
    st.write('Fundamental')
    
    # Initializing Alpha Vantage API key and FundamentalData object
    key = "91UR0VOFQXXXXXXX"  #Key will be generated from https://www.alphavantage.co/support/#support 
    fd = FundamentalData(key, output_format='pandas')
    
    # Fetching and displaying the balance sheet
    st.subheader('Balance Sheet')
    balance_sheet = fd.get_balance_sheet_annual(ticker)[0]
    bs = balance_sheet.T[2:]
    bs.columns = list(balance_sheet.T.iloc[0])
    st.write(bs)
    
    # Fetching and displaying the income statement
    st.subheader('Income Statement')
    income_statement = fd.get_income_statement_annual(ticker)[0]
    is1 = income_statement.T[2:]
    is1.columns = list(income_statement.T.iloc[0])
    st.write(is1)
    
    # Fetching and displaying the cash flow statement
    st.subheader('Cash Flow Statement')
    cash_flow = fd.get_cash_flow_annual(ticker)[0]
    cf = cash_flow.T[2:]
    cf.columns = list(cash_flow.T.iloc[0])
    st.write(cf)

# News tab
with news:
    st.write('News')
    st.header(f'News of {ticker}')
    
    # Initializing StockNews object and fetching news
    sn = StockNews(ticker, save_news=False)
    df_news = sn.read_rss()
    
    # Displaying the top 10 news articles with sentiments
    for i in range(10):
        st.subheader(f'News{i+1}')
        st.write(df_news['published'][i])
        st.write(df_news['title'][i])
        st.write(df_news['summary'][i])
        title_sentiment = df_news['sentiment_title'][i]
        st.write(f'Title Sentiment {title_sentiment}')
        news_sentiment = df_news['sentiment_summary'][i]
        st.write(f'News Sentiment {news_sentiment}')

# The OpenAI ChatGPT tab is not implemented in this example
