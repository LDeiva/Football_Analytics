# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 18:22:43 2022

@author: hp
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba
import json
from statsbombpy import sb
from mplsoccer import Pitch, FontManager
from mplsoccer.statsbomb import read_event, EVENT_SLUG
import seaborn as sns

#Produciamo la Pass Map
#season_id=input('insert season id')

#inseriamo l'ID del Match di nostro interesse 
match_id=input('insert match id')

#Apriamo il File Json con i dati del Match 
with open(rf'C:\Users\hp\Desktop\Script python\Calcio\Da modificare\Con Messi e euro2020\open-data-master\data\events\{match_id}.json') as data_file:
    #print (mypath+'events/'+file)
    data = json.load(data_file)
    
file_name=str(match_id)+'.json'    
   
#Trasformiamo i dati da Json a dataframe leggibile da Pandas 
from pandas.io.json import json_normalize
df = json_normalize(data, sep = "_").assign(match_id = file_name[:-5])

HomeTeam_name=df['team_name'].iloc[0]

AwayTeam_name=df['team_name'].iloc[1]

set_pieces = ['From Throw In', 'From Free Kick', 'From Corner', 'From Kick Off', 'From Goal Kick']

complete_pass=df[(df['type_name']=='Pass') & (df['pass_outcome_name'].isnull()) & (~df['play_pattern_name'].isin(set_pieces) & (df['possession_team_name']==AwayTeam_name))]

incomplete_pass = df[ (df['type_name']=='Pass') & (df.pass_outcome_name.notnull()) & (~df['play_pattern_name'].isin(set_pieces) & (df['possession_team_name']==AwayTeam_name))]


#single plot only Home or Away team
pitch = Pitch(linewidth=4,pitch_type='statsbomb',  pitch_color='#22312b')
fig, ax = pitch.draw(figsize=(9, 8), constrained_layout=True, tight_layout=False)
fig.set_facecolor("#22312b")

for i in range(len(incomplete_pass)):
    pitch.arrows(incomplete_pass.location.iloc[i][0], incomplete_pass.location.iloc[i][1],
                     incomplete_pass.pass_end_location.iloc[i][0], incomplete_pass.pass_end_location.iloc[i][1],
                     color='#ba4f45', width=2, headwidth=4, headlength=6,ax=ax)

for i in range(len(complete_pass)):
    pitch.arrows(complete_pass.location.iloc[i][0], complete_pass.location.iloc[i][1],
                     complete_pass.pass_end_location.iloc[i][0], complete_pass.pass_end_location.iloc[i][1],
                     color='#ad993c', width=2, headwidth=4, headlength=6, ax=ax)
pitch.arrows([], [],[], [],color='#ad993c', width=2, headwidth=4, headlength=6, ax=ax, label='completed passes')   
pitch.arrows([], [],[], [],color='#ba4f45', width=2, headwidth=4, headlength=6, ax=ax, label='incompleted passes')                  
ax.legend(facecolor='#22312b', handlelength=5, edgecolor='None', fontsize=20,loc=[0.01,0.80])
plt.show()

#Subplot one for HomeTeam and one for AwayTeam
fig, axs = pitch.grid(nrows=1, ncols=2,  # number of rows/ columns
                      figheight=25,  # the figure height in inches
                      bottom=0.025,  # starts 2.5% in from the figure bottom
                      # grid takes up 83% of the figure height
                      # I calculated this so most of the figure is pitches
                      # 1 - (bottom + endnote_height + endnote_space +
                      # title_height + title_space) - 0.025 [space at top]
                      grid_height=0.83,
                      # reduced the amount of the figure height reserved
                      # for the ax_endnote and ax_title since it is in
                      # fractions of the figure height and the figure height
                      # has increased. e.g. now the title_height is
                      # 8% of the figheight (25).
                      grid_width=0.95,  # the grid takes up 95% of the figwidth
                      # 5% of the grid_height is the space between pitches.
                      space=0.05,
                      endnote_height=0.0, endnote_space=0.0,
                      title_height=0.0, title_space=0.0)

lista=[HomeTeam_name,AwayTeam_name]
for idx, ax in enumerate(axs['pitch'].flat):
    
    incomplete_pass = df[ (df['type_name']=='Pass') & (df.pass_outcome_name.notnull()) & (~df['play_pattern_name'].isin(set_pieces) & (df['possession_team_name']==lista[idx]))]
    complete_pass=df[(df['type_name']=='Pass') & (df['pass_outcome_name'].isnull()) & (~df['play_pattern_name'].isin(set_pieces) & (df['possession_team_name']==lista[idx]))]
    for i in range(len(incomplete_pass)):
        pitch.arrows(incomplete_pass.location.iloc[i][0], incomplete_pass.location.iloc[i][1],
                         incomplete_pass.pass_end_location.iloc[i][0], incomplete_pass.pass_end_location.iloc[i][1],
                         color='#ba4f45', width=2, headwidth=4, headlength=6,ax=ax)

    for i in range(len(complete_pass)):
        pitch.arrows(complete_pass.location.iloc[i][0], complete_pass.location.iloc[i][1],
                         complete_pass.pass_end_location.iloc[i][0], complete_pass.pass_end_location.iloc[i][1],
                         color='#ad993c', width=2, headwidth=4, headlength=6, ax=ax)
    pitch.arrows([], [],[], [],color='#ad993c', width=2, headwidth=4, headlength=6, ax=ax, label='completed passes')   
    pitch.arrows([], [],[], [],color='#ba4f45', width=2, headwidth=4, headlength=6, ax=ax, label='incompleted passes')                  
    ax.legend(facecolor='#22312b', handlelength=5, edgecolor='None', fontsize=20,loc=[0.01,0.90])
plt.show()



