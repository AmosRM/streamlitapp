import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

import fastf1 as ff
from fastf1 import plotting, utils

# Fetch data from FastF1_api

races = pd.read_html('https://en.wikipedia.org/wiki/2022_Formula_One_World_Championship')
all_races = races[1]
race = all_races['Grand Prix'].str.replace(' Grand Prix','').tolist()

year = range(2020,2023)
session1 = ['FP1', 'FP2', 'FP3', 'Q', 'SQ', 'R']



# STREAMLIT APP

st.title("Formula 1 Analysis")

with st.sidebar:
    year_choice = st.selectbox("Year", year)
    race_choice = st.selectbox("Race", race)
    session_choice = st.selectbox("Session", session1)

# Get data

# ff.Cache.enable_cache('Users/amos/Downloads')
plotting.setup_mpl()

selected_race = ff.get_session(year_choice,race_choice,session_choice)
driver = pd.unique(selected_race['Driver'])
driver_choice = st.selectbox("Driver's to compare", driver)

fastest_lap = selected_race.laps.pick_driver(driver_choice).pick_fastest()
fastest_lap
