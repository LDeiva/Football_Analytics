# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 17:17:53 2021

@author: hp
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba
from statsbombpy import sb
from mplsoccer import Pitch, FontManager
from mplsoccer.statsbomb import read_event, EVENT_SLUG
import seaborn as sns
import json
#open Data 
#sb.competitions()
#sb.matches(competition_id=16,season_id=2)
#events=sb.events(match_id=18244)

#open data from jason
#season_id=input('insert season id')
match_id=input('insert match id')

with open(rf'C:\Users\hp\Desktop\Script python\Calcio\Da modificare\David\statsbomb_data\data\events\{match_id}.json') as data_file:
    #print (mypath+'events/'+file)
    data = json.load(data_file)
    
file_name=str(match_id)+'.json'    
    
from pandas.io.json import json_normalize
df= json_normalize(data, sep = "_").assign(match_id = file_name[:-5])


#filter Data
events=df[['team_name','type_name','minute','shot_statsbomb_xg']]

#filtra per avere solo i tiri
Shots=events[events['type_name']=='Shot']

Shots_home=events[(events['type_name']=='Shot') & (events['team_name']=='Portugal')]

Shots_away=events[(events['type_name']=='Shot') & (events['team_name']=='Spain')]

#crea lista con expected golas
xG_home=[]

xG_away=[]

#a_team=Shots['team_name'].iloc[-1]
a_team=Shots['team_name'].iloc[1]
#h_team=Shots['team_name'].iloc[0]
h_team=Shots['team_name'].iloc[0]

a_time=[]

h_time=[]

for i in range(len(Shots['team_name'])):
    if Shots['team_name'].iloc[i]==a_team:
        xG_away.append(Shots['shot_statsbomb_xg'].iloc[i])
        a_time.append(Shots['minute'].iloc[i])
    
    if Shots['team_name'].iloc[i]==h_team:
        xG_home.append(Shots['shot_statsbomb_xg'].iloc[i])
        h_time.append(Shots['minute'].iloc[i])

xG_away.insert(0, 0)
xG_home.insert(0, 0)
a_time.insert(0, 0)
h_time.insert(0, 0)
#crea liste con expected goals flow cioè come variano minuto per minuto gli xG della partita
xG_home_Flow=[sum(xG_home[:i+1]) for i in range(len(xG_home))]

xG_away_Flow=[sum(xG_away[:i+1]) for i in range(len(xG_away))]

#estrai xG totla per entrambi
xG_home_sum=xG_home_Flow[-1]

xG_away_sum=xG_away_Flow[-1]



#plottiamo gli xG_flow Away team
fig,ax=plt.subplots(figsize=(16,11))
fig.set_facecolor('#3d4849') #cambia colore fuori assi cioè la parte più esterna del grafico
ax.patch.set_facecolor('#3d4849') #cambia colore dentro gli assi
ax.step(a_time,xG_away_Flow)
plt.show()


#plottiamo gli xG_flow_Home Team
fig,ax=plt.subplots(figsize=(16,11))
fig.set_facecolor('#3d4849') #cambia colore fuori assi cioè la parte più esterna del grafico
ax.patch.set_facecolor('#3d4849') #cambia colore dentro gli assi
ax.step(h_time,xG_home_Flow)
plt.show()



#plottiamo gli xG Away Team
fig,ax=plt.subplots(figsize=(16,11))
fig.set_facecolor('#3d4849') #cambia colore fuori assi cioè la parte più esterna del grafico
ax.patch.set_facecolor('#3d4849') #cambia colore dentro gli assi
ax.step(a_time,xG_away)
ax.set_xticks([0,15,30,45,90])
plt.show()


#plottiamo gli xG Home Team
fig,ax=plt.subplots(figsize=(16,11))
fig.set_facecolor('#3d4849') #cambia colore fuori assi cioè la parte più esterna del grafico
ax.patch.set_facecolor('#3d4849') #cambia colore dentro gli assi
ax.step(h_time,xG_home)
plt.show()

