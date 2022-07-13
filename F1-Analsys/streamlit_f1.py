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

ff.Cache.enable_cache('/Users/amos/Downloads/cache')

selected_race = ff.get_session(year_choice,race_choice,session_choice)
selected_race.load()
driver = pd.unique(selected_race.laps['Driver'])
driver_choice = st.multiselect("Driver's to compare", driver)

driver_1 = selected_race.laps.pick_driver(driver_choice[0])
driver_2 = selected_race.laps.pick_driver(driver_choice[1])

fastest1 = driver_1.pick_fastest()
fastest2 = driver_2.pick_fastest()

t1 = fastest1.get_telemetry().add_distance()
t2 = fastest2.get_telemetry().add_distance()


# delta_time, ref_tel, compare_tel = utils.delta_time(fastest1)

# plt.rcParams['figure.figsize'] = [10,10]
# plotting.setup_mpl()

fig , ax = plt.subplots()
ax.plot(t1['Distance'], t1['Speed'])
ax.plot(t2['Distance'], t2['Speed'])
# ax.set(ylabel='Speed')
# ax.legend(loc="lower right")
st.write(fig)