from nba_api.stats.endpoints import shotchartdetail
from nba_api.stats.endpoints import playercareerstats
import json
import requests
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image

# st.header('Shot Chart')

player_name = st.selectbox('Choose player',('Stephen Curry', 'Luka Doncic', 'Devin Booker', 'LeBron James', 'Giannis Antetokounmpo', 'Kevin Durant', 'Trae Young', 'Jimmy Butler'))

# Load team adn player files from bttmly/nba repo
#   (this can be done with nba_api but this will be faster)
players = json.loads(requests.get('https://raw.githubusercontent.com/bttmly/nba/master/data/players.json').text)
teams = json.loads(requests.get('https://raw.githubusercontent.com/bttmly/nba/master/data/teams.json').text)


# Get teams and players ID based on name
def get_player_details(player_name):
    for player in players:
        first = player_name.split()[0]
        last = player_name.split()[1]
        if player['firstName'] == first and player['lastName'] == last:
            return player['playerId'], player['teamId']
    return player['playerId'], player['teamId']

playerId = get_player_details(player_name)[0]

# Create JSON request
shot_json = shotchartdetail.ShotChartDetail(
            team_id = get_player_details(player_name)[1],
            player_id = get_player_details(player_name)[0],
            context_measure_simple = 'PTS',
            season_nullable = '2021-22',
            season_type_all_star = 'Regular Season')

# Load into python directory
shot_data = json.loads(shot_json.get_json())

relevant_data = shot_data['resultSets'][0]
headers = relevant_data['headers']
rows = relevant_data['rowSet']

# Create pandas DataFrame
player_data = pd.DataFrame(rows)
player_data.columns = headers

# Draw court ()
def create_court(ax, color):
    
    # Short corner 3PT lines
    ax.plot([-220, -220], [0, 140], linewidth=2, color=color)
    ax.plot([220, 220], [0, 140], linewidth=2, color=color)
    
    # 3PT Arc
    ax.add_artist(mpl.patches.Arc((0, 140), 440, 315, theta1=0, theta2=180, facecolor='none', edgecolor=color, lw=2))
    
    # Lane and Key
    ax.plot([-80, -80], [0, 190], linewidth=2, color=color)
    ax.plot([80, 80], [0, 190], linewidth=2, color=color)
    ax.plot([-60, -60], [0, 190], linewidth=2, color=color)
    ax.plot([60, 60], [0, 190], linewidth=2, color=color)
    ax.plot([-80, 80], [190, 190], linewidth=2, color=color)
    ax.add_artist(mpl.patches.Circle((0, 190), 60, facecolor='none', edgecolor=color, lw=2))
    
    # Rim
    ax.add_artist(mpl.patches.Circle((0, 60), 15, facecolor='none', edgecolor=color, lw=2))
    
    # Backboard
    ax.plot([-30, 30], [40, 40], linewidth=2, color=color)
    
    # Remove ticks
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Set axis limits
    ax.set_xlim(-250, 250)
    ax.set_ylim(0, 470)
    
    return ax

mpl.rcParams['font.family'] = 'Avenir'
mpl.rcParams['font.size'] = 18
mpl.rcParams['axes.linewidth'] = 2

# Create figure and axes
fig = plt.figure(figsize=(4, 3.76))
ax = fig.add_axes([0, 0, 1, 1])

# Draw court
ax = create_court(ax, 'black')

# Plot hexbin of shots
ax.hexbin(player_data['LOC_X'], player_data['LOC_Y'] + 60, gridsize=(30, 30), extent=(-300, 300, 0, 940), bins='log', cmap='Blues')

# Annotate player name and season
ax.text(0, 1.05, (player_name + '\n2021-22 Regular Season'), transform=ax.transAxes, ha='left', va='baseline')

playerstats = playercareerstats.PlayerCareerStats(player_id=playerId).get_data_frames()[0]
year_stats = playerstats[playerstats['SEASON_ID'] == '2021-22']
sd = year_stats[['GP','PTS','AST','REB']]
sd['PTSg'] = sd['PTS']/sd['GP']
sd['ASTg'] = sd['AST']/sd['GP']
sd['REBg'] = sd['REB']/sd['GP']
sd = sd.round(1)

photo_url = f"https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/{playerId}.png"

col1, col2 = st.columns([2,5])

with col2:
    st.pyplot(fig)
with col1:
    st.image(photo_url)
    st.metric('PTS', sd['PTSg'])
    st.metric('AST', sd['ASTg'])
    st.metric('REB', sd['REBg'])