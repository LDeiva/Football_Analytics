# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 11:10:16 2021

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

#open Data 
sb.competitions()
sb.matches(competition_id=16,season_id=2)
events=sb.events(match_id=18244)

#filter Data
events=events[['team','type','minute','location','pass_end_location','player','pass_outcome','substitution_replacement', 'id','shot_outcome']]

Succesfull_Pjanic_Pass=events[(events['player']=='Miralem Pjanić') & (events['type']=='Pass') & (events['pass_outcome']!='Incomplete') & (events['pass_outcome']!='Out')]

#create x and y columns
x=[]
y=[]
for i in range(len(Succesfull_Pjanic_Pass['location'])):
    
    x.append(Succesfull_Pjanic_Pass['location'].iloc[i][0])
    y.append(Succesfull_Pjanic_Pass['location'].iloc[i][1])
    
Succesfull_Pjanic_Pass['x']=x
Succesfull_Pjanic_Pass['y']=y
#plot pitch and pass map

pitch = Pitch(pitch_type='statsbomb',orientation='horizontal', pitch_color='#22312b', line_color='#c7d5cc'
              ,figsize=(10,6), constrained_layout=True,tight_layout=False)
fig, ax = pitch.draw()
plt.gca().invert_yaxis()

for i in range(len(Succesfull_Pjanic_Pass['location'])):
    plt.plot((Succesfull_Pjanic_Pass['location'].iloc[i][0],Succesfull_Pjanic_Pass['pass_end_location'].iloc[i][0]),(Succesfull_Pjanic_Pass['location'].iloc[i][1],Succesfull_Pjanic_Pass['pass_end_location'].iloc[i][1]),color='r')
    plt.scatter(Succesfull_Pjanic_Pass['location'].iloc[i][0],Succesfull_Pjanic_Pass['location'].iloc[i][1],color='r')
    plt.scatter(Succesfull_Pjanic_Pass['pass_end_location'].iloc[i][0],Succesfull_Pjanic_Pass['pass_end_location'].iloc[i][1],color='r')
#kde=sns.kdeplot(Succesfull_Pjanic_Pass['x'],Succesfull_Pjanic_Pass['y'],shade=True,Shade_lowest=False,alpha=0.5,n_lavels=10,cmap='magma')
plt.show()

#Create heatmap
pitch = Pitch(pitch_type='statsbomb',orientation='horizontal', pitch_color='#22312b', line_color='#c7d5cc'
              ,figsize=(10,6), constrained_layout=True,tight_layout=False)
fig, ax = pitch.draw()
plt.gca().invert_yaxis()
kde=sns.kdeplot(Succesfull_Pjanic_Pass['x'],Succesfull_Pjanic_Pass['y'],shade=True,Shade_lowest=False,alpha=0.5,n_lavels=10,cmap='magma')
plt.show()
