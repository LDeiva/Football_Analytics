# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 17:17:29 2022

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

df['type_name'].value_counts()
HomeTeam_name=df['team_name'].iloc[0]

AwayTeam_name=df['team_name'].iloc[1]

Home=df[df['team_name']==HomeTeam_name]

# add on the position abbreviation
formation_dict = {1: 'GK', 2: 'RB', 3: 'RCB', 4: 'CB', 5: 'LCB', 6: 'LB', 7: 'RWB',
                  8: 'LWB', 9: 'RDM', 10: 'CDM', 11: 'LDM', 12: 'RM', 13: 'RCM',
                  14: 'CM', 15: 'LCM', 16: 'LM', 17: 'RW', 18: 'RAM', 19: 'CAM',
                  20: 'LAM', 21: 'LW', 22: 'RCF', 23: 'ST', 24: 'LCF', 25: 'SS'}
Home['position_abbreviation'] = Home.position_id.map(formation_dict)
columns=Home.columns
time_off =Home.loc[(Home.type_name == 'Substitution'),
                      ['player_name', 'minute']]

time_on =Home.loc[(Home.type_name == 'Substitution'),
                      [ 'substitution_replacement_name','minute']]
time_on.rename({'substitution_replacement_name': 'player_name','minute':'on'}, axis='columns', inplace=True)
time_off.rename({'minute':'off'}, axis='columns', inplace=True)
player_positions = (Home[['player_name', 'position_id','position_abbreviation']]
                    .dropna(how='any', axis='rows')
                    .drop_duplicates('player_name', keep='first'))

unique_1=pd.DataFrame(Home['player_name'].unique(),columns=['player_name'])
unique_1=unique_1[~pd.isna(unique_1)]
unique_2=Home['position_abbreviation'].unique()
unique_2=unique_2[~pd.isnull(unique_2)]

unique_1 = unique_1.merge(time_off, on='player_name', how='left')
unique_1 = unique_1.merge(player_positions , on='player_name', how='left')

unique_1 = unique_1.merge(time_on, on='player_name', how='left')
unique_1=unique_1.append(time_on)

unique_1.sort_values(['position_id','minute_x','minute_y'],
                   ascending=[True, True, True], inplace=True)

player_name=list(np.unique(Home[['player_name','position_name']]))
player_name=player_name[1:]


set_pieces = ['From Throw In', 'From Free Kick', 'From Corner', 'From Kick Off', 'From Goal Kick']

complete_pass=df[(df['type_name']=='Pass') & (df['pass_outcome_name'].isnull()) & (~df['play_pattern_name'].isin(set_pieces) & (df['possession_team_name']==AwayTeam_name))]

incomplete_pass = df[ (df['type_name']=='Pass') & (df.pass_outcome_name.notnull()) & (~df['play_pattern_name'].isin(set_pieces) & (df['possession_team_name']==AwayTeam_name))]

pitch = Pitch(linewidth=4,pitch_type='statsbomb',  pitch_color='#22312b')


#Subplot one for HomeTeam and one for AwayTeam
fig, axs = pitch.grid(nrows=6, ncols=3, figheight=30,
                      endnote_height=0.03, endnote_space=0,
                      # Turn off the endnote/title axis. I usually do this after
                      # I am happy with the chart layout and text placement
                      axis=False,
                      title_height=0.08, grid_height=0.84)        


for idx, ax in enumerate(axs['pitch'].flat):
    
    incomplete_pass = df[ (df['type_name']=='Pass') & (df.pass_outcome_name.notnull()) & (~df['play_pattern_name'].isin(set_pieces) & (df['player_name']==player_name[idx]))]
    complete_pass=df[(df['type_name']=='Pass') & (df['pass_outcome_name'].isnull()) & (~df['play_pattern_name'].isin(set_pieces) & (df['player_name']==player_name[idx]))]
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


