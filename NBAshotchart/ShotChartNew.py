import streamlit as st
import matplotlib.pyplot as plt
from shot_chart import draw_court, get_league_shots, shot_chart

plt.rc('font', family='serif')

seasons = '2000-01', '2018-19'
shots = {s: get_league_shots(s) for s in seasons}

season = seasons[1]
threshold = 100

shot_chart_options = {
    'threshold': threshold,
    'color': 'pct',
    'markersize': [100, 400],
    'nbins': 4,
    'gridsize': 50,
    'legend_args': {'fontsize': 20, 'title_fontsize': 20},
    'title_args': {'fontsize': 30}}

title = f'NBA Leage-wide Shot Chart: {season}\nMinimum {threshold} Attempts'

def compare_shot_charts(shots, seasons, options):
    fig, axs = plt.subplots(ncols=len(seasons), figsize=(30, 12), constrained_layout=True)

    for season, ax in zip(seasons, axs):
        shot_chart(shots[season], ax, title=season, **options)
        draw_court(ax=ax)
        ax.set_xlim(-260, 260)
        ax.set_ylim(-60, 300)
        ax.axis('off')
        
    return fig, ax

fig, ax = compare_shot_charts(shots, seasons, shot_chart_options)
fig.suptitle(f'NBA Leage-wide Shot Chart\nMinimum {threshold} Attempts', fontsize=40)
plt.show()