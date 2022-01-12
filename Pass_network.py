# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 16:25:34 2021

@author: hp
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba
from statsbombpy import sb
from mplsoccer import Pitch, FontManager
from mplsoccer.statsbomb import read_event, EVENT_SLUG


sb.competitions()
sb.matches(competition_id=16,season_id=2)
events=sb.events(match_id=18244)
events=events[['team','type','minute','location','pass_end_location','player','pass_outcome','substitution_replacement', 'id']]
Max_time=events[(events['type']=='Substitution')]
time=Max_time['minute'].min()
juventus=events[(events['team']=='Juventus')]
juventus=juventus[(juventus['minute']<time)]

juventus=juventus[(juventus['type']=='Pass')].reset_index()

x=[]
y=[]
for i in range(len(juventus['location'])):
    
    x.append(juventus['location'][i][0])
    y.append(juventus['location'][i][1])
    
juventus['x']=x
juventus['y']=y
juventus['recived_player']=juventus['player'].shift(-1)
juventus=juventus[(juventus['pass_outcome']!='Incomplete')]

# average locations of players
average_locs_and_count = (juventus.groupby('player').agg({'x': ['mean'], 'y': ['mean', 'count']}))
average_locs_and_count.columns = ['x', 'y', 'count']


# calculate the number of passes between each position (using min/ max so we get passes both ways)

passes_between = juventus.groupby(['player', 'recived_player']).id.count().reset_index()
passes_between.rename({'id': 'pass_count'}, axis='columns', inplace=True)

# add on the location of each player so we have the start and end positions of the lines
passes_between = passes_between.merge(average_locs_and_count, left_on='player', right_index=True)
passes_between = passes_between.merge(average_locs_and_count, left_on='recived_player', right_index=True,
                                      suffixes=['', '_end'])

#Calculate the line width and marker sizes relative to the largest counts
MAX_LINE_WIDTH = 18
MAX_MARKER_SIZE = 3000
passes_between['width'] = (passes_between.pass_count / passes_between.pass_count.max() *
                           MAX_LINE_WIDTH)
average_locs_and_count['marker_size'] = (average_locs_and_count['count']
                                         / average_locs_and_count['count'].max() * MAX_MARKER_SIZE)

#Plot Data
pitch = Pitch(pitch_type='statsbomb', pitch_color='#22312b', line_color='#c7d5cc')
fig, ax = pitch.draw(figsize=(16, 11), constrained_layout=True, tight_layout=False)
fig.set_facecolor("#22312b")
pass_lines = pitch.lines(passes_between.x, passes_between.y,
                         passes_between.x_end, passes_between.y_end, lw=passes_between.width,
                         color='k', zorder=1, ax=ax)
pass_nodes = pitch.scatter(average_locs_and_count.x, average_locs_and_count.y,
                           s=average_locs_and_count.marker_size,
                           color='red', edgecolors='black', linewidth=1, alpha=1, ax=ax)
#Put Labels on the average position for Players
for index, row in average_locs_and_count.iterrows():
    pitch.annotate(row.name, xy=(row.x, row.y), c='white', va='center',
                   ha='center', size=16, weight='bold', ax=ax)


# Load a custom font.
URL = 'https://github.com/googlefonts/roboto/blob/main/src/hinted/Roboto-Regular.ttf?raw=true'
robotto_regular = FontManager(URL)
#ax.text(0.5, 1, 'Pass Network Juventus Vs Real Madrid  UCL Final', color='#c7d5cc',va='center', ha='center', fontproperties=robotto_regular.prop, fontsize=30)
plt.title('Pass Network Juventus Vs Real Madrid  UCL Final', color='white',fontsize=30)
plt.show()

