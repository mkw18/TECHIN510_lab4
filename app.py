"""
Change this to a world clock app
"""

import time

import streamlit as st
from datetime import datetime
import pytz
import yfinance as yf

def world_clock():
    st.title("World Clock")
    def showTime():
        while True:
            with placeholder.container():
                placeholder.metric('Time', datetime.now(pytz.timezone(st.session_state.timezone)).ctime())
                timestamp.metric('UNIX timestamp', datetime.timestamp(datetime.now()))
            time.sleep(1)

    st.selectbox('Time zone', ['US/Pacific', "US/Eastern", 'UTC', "Asia/Shanghai"], key='timezone', on_change=showTime)
    placeholder = st.empty()
    timestamp = st.empty()

    showTime()

def unix_converter():
    st.title("Unix Converter")
    unix_time_input = st.number_input("UNIX Timestamp:", min_value=0, step=1, value=int(datetime.timestamp(datetime.now())))
    st.metric("Human Time - Your Time zone", datetime.fromtimestamp(unix_time_input).strftime('%Y-%m-%d %H:%M:%S'))
    st.metric("Human Time - UTC", datetime.utcfromtimestamp(unix_time_input).strftime('%Y-%m-%d %H:%M:%S'))

def fetch_financial_data_page():
    st.title("Real-time Stock Data")

    symbol = st.text_input("Enter Stock Symbol (e.g., AAPL for Apple):")

    if symbol:
        stock = yf.Ticker(symbol)
        data = stock.history(period='1d')
        if data is not None:
            st.write(f"Real-time Stock Data for {symbol}:")
            st.write(data)
        else:
            st.write("No data available for the entered stock symbol.")
    else:
        st.write("No data available for the entered stock symbol.")

pages = {
    "World Clock": world_clock,
    "Unix Converter": unix_converter,
    "Realtime Stock Data": fetch_financial_data_page,
}
st.sidebar.title("Navigation")
selected_page = st.sidebar.selectbox("Go to", list(pages.keys()))

pages[selected_page]()