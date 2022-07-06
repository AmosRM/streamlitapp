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

###################################################################
# First figure for new cases and new deaths

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

###################################################################
# Second figure last 30 days new cases and new deaths with 7 days average

fig1 , ax3 = plt.subplots(figsize=(12,9))

ax3_x = new_df['date'].tail(30)
ax3_y = new_df['new_cases'].tail(30)

ax3.set_xlabel('Date')
ax3.set_ylabel('NEW CASES')
ax3.bar(ax3_x,ax3_y,label='new cases')
ax3.tick_params(axis='y', labelcolor=color)
ax4 = ax3.twinx()
ax4.plot(ax3_x,ax3_y.tail(30),color=color,label='new cases')



st.pyplot(fig)
st.pyplot(fig1)