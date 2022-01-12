# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 17:50:09 2021

@author: hp
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba
from statsbombpy import sb
from mplsoccer import Pitch, FontManager,VerticalPitch
from mplsoccer.statsbomb import read_event, EVENT_SLUG
from matplotlib.cm import get_cmap

#open Data 
sb.competitions()
sb.matches(competition_id=16,season_id=2)
events=sb.events(match_id=18244)

#filter Data
events=events[['team','type','minute','location','pass_end_location','player','pass_outcome', 'id']]

Real_Pass=events[(events['type']=='Pass') & (events['team']=='Real Madrid') & (events['pass_outcome'].isna())]

#create 4 columns with cordinates
x=[]
y=[]
end_x=[]
end_y=[]
for i in range(len(Real_Pass['location'])):
    
    x.append(Real_Pass['location'].iloc[i][0])
    y.append(Real_Pass['location'].iloc[i][1])
    end_x.append(Real_Pass['pass_end_location'].iloc[i][0])
    end_y.append(Real_Pass['pass_end_location'].iloc[i][1])
    
Real_Pass['x']=x
Real_Pass['y']=y
Real_Pass['end_x']=end_x
Real_Pass['end_y']=end_y

#calculate distance and which passes are progressive_passes
Real_Pass['start_distance']=np.sqrt(np.square(120-Real_Pass['x']) + (np.square(40-Real_Pass['y'])))
Real_Pass['end_distance']=np.sqrt(np.square(120-Real_Pass['end_x']) + (np.square(40-Real_Pass['end_y'])))
Real_Pass['Progressive']=[(Real_Pass['end_distance'].iloc[i]/Real_Pass['start_distance'].iloc[i])<0.75 for i in range(len(Real_Pass['start_distance']))]      

#select one player and only progressive_passes

Real_Pass=Real_Pass[(Real_Pass['player']=='Luka Modrić') & (Real_Pass['Progressive']==True)].reset_index()

#Plot Progressive_Passes
pitch = Pitch(pitch_type='statsbomb', pitch_color='#22312b', line_color='#c7d5cc')
fig, ax = pitch.draw(figsize=(16, 11), constrained_layout=True, tight_layout=False)
fig.set_facecolor("#22312b")
pitch.lines(Real_Pass.x,Real_Pass.y,Real_Pass.end_x,Real_Pass.end_y,comet=True,ax=ax) #questo ha più stile 
#plt.plot((Real_Pass.x,Real_Pass.end_x),(Real_Pass.y,Real_Pass.end_y))
plt.show()




