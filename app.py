"""
Change this to a world clock app
"""

import time

import streamlit as st
from datetime import datetime
import pytz

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


pages = {
    "World Clock": world_clock,
    "Unix Converter": unix_converter,
}
st.sidebar.title("Navigation")
selected_page = st.sidebar.selectbox("Go to", list(pages.keys()))

pages[selected_page]()