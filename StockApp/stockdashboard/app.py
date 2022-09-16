import streamlit as st
import pandas as pd
import numpy as np
import requests
from sympy import symbols
import tweepy
import config 
import psycopg2, psycopg2.extras
import plotly.graph_objects as go


option = st.sidebar.selectbox("Which Dashboard?", ('twitter', 'chart', 'pattern'), 3)

st.header(option)

if option == 'Twitter':
    pass

if option == 'Chart':
    pass

if option