import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

from shot_chart import draw_court, get_league_shots, shot_chart

plt.rc('font', family='serif')
choose_year = 11

# DATA
df = pd.read_csv(f'shots_{choose_year}.csv')
year = df['GAME_DATE'].astype(str).str[:4].unique()
years = f'{year[0]}-{year[1]}'


# Plot Parameters
threshold = 100
shot_chart_options = {
    'threshold': threshold,
    'color': 'pct',
    'markersize': [25, 100],
    'nbins': 4,
    'gridsize': 50,
    'legend_args': {'columnspacing': 0.1},}

# title = f'NBA Leage-wide Shot Chart: {years}\nMinimum {threshold} Attempts'


# PLOT
# fig, ax = plt.subplots(figsize=(12,8), dpi=100)
# shot_chart(df, ax, **shot_chart_options, title=title)
# draw_court(ax=ax)
# plt.xlim(-260, 260)
# plt.ylim(-60, 300)
# plt.axis('off')
# plt.show()
fig, ax = plt.subplots(figsize=(12,8), dpi=100)

def plot(choose_year):
    title = f'NBA Leage-wide Shot Chart: {choose_year}\nMinimum {threshold} Attempts'
    ax.clear()
    shot_chart(df, ax, **shot_chart_options, title=title)
    draw_court(ax=ax)
    plt.xlim(-260, 260)
    plt.ylim(-60, 300)
    plt.axis('off')
    plt.show()

anim = FuncAnimation(
    fig,
    plot,
    frames=range(16,22,1)
)

anim.save('shot.gif', dpi=300, writer=PillowWriter(fps=5))