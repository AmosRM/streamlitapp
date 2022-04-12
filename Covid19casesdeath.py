import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# @st.cache

st.title("My COVID 19 streamlit")

url = 'https://raw.githubusercontent.com/AmosRM/streamlitapp/main/Book2.csv'
df = pd.read_csv(url)
df['date'] = pd.to_datetime(df['date'])

countries_list = df['location'].unique()

country = st.sidebar.selectbox(
     'Select Country',
     countries_list)

new_df = df[df['location']==country]

start = st.sidebar.date_input('Start',value=pd.to_datetime('2020-03-01'))
end = st.sidebar.date_input('End')
range = pd.date_range(start, end, freq='D')

new_df = new_df[new_df['date'].isin(range)]

x = new_df['date']
y = new_df['new_cases_smoothed']
z = new_df['new_deaths_smoothed']

fig, ax1 = plt.subplots(figsize=(12,9))

color = 'tab:blue'
ax1.set_xlabel('Date')
ax1.set_ylabel('NEW CASES')
ax1.plot(x,y,color=color,label='new cases')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()

color = 'tab:red'
ax2.set_ylabel('NEW DEATHS')
ax2.plot(x,z,color=color,label='new deaths')
ax2.tick_params(axis='y', labelcolor=color)

fig.legend(bbox_to_anchor=(0.3, 0.95),fontsize=18)
ax1.grid()
ax1.xaxis.set_tick_params(rotation=45)
fig.tight_layout()

st.pyplot(fig)
