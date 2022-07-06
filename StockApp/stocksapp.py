from telnetlib import LOGOUT
from urllib import response
import pandas as pd
import numpy as np
from sympy import comp
import streamlit as st
import requests
import StockApp.config as config, StockApp.iex as iex

IEX_TOKEN = 'pk_a76555e5564549eb8277b0960f70135e'

symbol = st.sidebar.text_input("Symbol", value='MSFT')

stock = iex.IEXStock(config.IEX_TOKEN, symbol)

screen = st.sidebar.selectbox("View", ('Overview', 'Fundamentals', 'Technicals'))

st.write(symbol)

st.title(screen)

if screen == 'Overview':
    company = stock.get_company_info()
    logo = stock.get_logo()

    col1, col2 = st.columns([1, 4])

    with col1:
        st.image(logo['url'])

    with col2:    
        st.subheader(company['companyName'])
        st.write(company['industry'])
        st.subheader('Description')
        st.write(company['description'])
        st.subheader('CEO')
        st.write(company['CEO'])

def format_number(number):
    return f"{number:,}"

if screen == 'Fundamentals':
    stats = stock.get_stats()

    st.header('Ratios')

    col1, col2 = st.columns(2)

    with col1:
        st.subheader('P/E')
        st.write(stats['peRatio'])
        st.subheader('Marketcap')
        st.write(stats['marketcap'])
        st.subheader('Employees')
        st.write(stats['employees'])
        st.subheader('ttm EPS')
        st.write(stats['ttmEPS'])
        st.subheader('Beta')
        st.write(stats['beta'])
    with col2:
        st.subheader('Revenue')
        # st.write(format_number(stats['revenue']))
        st.subheader('Cash')
        # st.write(format_number(stats['totalCash']))
        st.subheader('Debt')
        #st.write(format_number(stats['currentDebt']))
        st.subheader('200 Day Moving Average')
        #st.write(stats['day200MovingAvg'])
        st.subheader('50 Day Moving Average')
        #st.write(stats['day50MovingAvg'])