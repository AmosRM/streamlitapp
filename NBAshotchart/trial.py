import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

from shot_chart import draw_court, get_league_shots, shot_chart

seasons = '2000-01', '2002-03', '2004-05', '2006-07', '2008-09','2010-11','2012-13','2014-15','2016-17','2018-19'

shots = {s: get_league_shots(s) for s in seasons}

threshold = 100
shot_chart_options = {
    'threshold': threshold,
    'color': 'pct',
    'markersize': [25, 100],
    'nbins': 4,
    'gridsize': 50,
    'legend_args': {'columnspacing': 0.1},}

fig, ax = plt.subplots(figsize=(12, 8), dpi=100)
def plots(seasony):
    ax.clear()
    title = f'NBA Leage-wide Shot Chart: {seasony}\nMinimum {threshold} Attempts'
    shot_chart(shots[seasony], ax, title=title, **shot_chart_options)
    draw_court(ax=ax)
    plt.xlim(-260, 260)
    plt.ylim(-60, 300)
    plt.axis('off')

animation = FuncAnimation(
    fig,
    plots,
    frames= seasons
)
plt.show()