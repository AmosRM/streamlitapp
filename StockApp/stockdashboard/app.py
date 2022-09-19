import streamlit as st
import pandas as pd
import numpy as np
import requests
from sympy import symbols
import tweepy
import config 
import psycopg2, psycopg2.extras
import plotly.graph_objects as go

# Twitter API Key -

# auth = tweepy.OAuthHandler(config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET)
# auth.set_access_token(config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_TOKEN_SECRET)
# api = tweepy.API(auth)

# DataBase connection with psycpg2 -

# connection = psycopg2.connect(host=config.DB_HOST, database=config.DB_NAME, user=config.DB_USER, password=config.DB_PASS)
# cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)


option = st.sidebar.selectbox("Which Dashboard?", ('twitter', 'chart', 'pattern'), 3)

st.header(option)

if option == 'Twitter':
    pass

if option == 'Chart':
    pass

if option