# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 16:02:01 2021
7576
@author: hp
"""

import matplotlib.pyplot as plt
import numpy as np
import json
from matplotlib.colors import to_rgba
from statsbombpy import sb
from mplsoccer import Pitch, FontManager,VerticalPitch, pitch
from mplsoccer.statsbomb import read_event, EVENT_SLUG
import seaborn as sns
from Shot_maps_and_results_function import Shot_OneColumns_maps,print_result
from matplotlib.cm import get_cmap
from XG_function import XG_home,XG_away,Most_involved


#Produciamo la Shot Map
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


# Estraiamo il nome della squadra di casa e i traferta 
HomeTeam_name=df['team_name'].iloc[0]

AwayTeam_name=df['team_name'].iloc[1]


#plottiamo il campo e i tiri tramite la funzione 
pitch = Pitch(pitch_type='statsbomb', pitch_color='#22312b', line_color='#c7d5cc')
fig, ax = pitch.draw(figsize=(9, 8), constrained_layout=True, tight_layout=False)
fig.set_facecolor("#22312b")
plt.gca().invert_yaxis()

Shot_OneColumns_maps(df,HomeTeam_name,AwayTeam_name)    


# setup a mplsoccer FontManager to download google fonts (Roboto-Regular / SigmarOne-Regular)
fm_rubik = FontManager(('https://github.com/google/fonts/blob/main/ofl/rubikmonoone/'
                        'RubikMonoOne-Regular.ttf?raw=true'))

#Inseriamo i testi con le informazioni della partita

title1 = fig.text(x=0.35, y=0.94, s=f' World Cup: {HomeTeam_name} - {AwayTeam_name} {print_result(df,HomeTeam_name,AwayTeam_name)} ', 
                  va='center', ha='center',size=15, color=pitch.line_color,fontproperties=fm_rubik.prop)
                  

title2 = fig.text(x=0.185, y=0.90, s=f'xG: {XG_home(match_id,HomeTeam_name)} - {XG_away(match_id,AwayTeam_name)}', 
                  va='center', ha='center', size=15, color=pitch.line_color, fontproperties=fm_rubik.prop)
                 
title3 = fig.text(x=0.53, y=0.87, s=f'{Most_involved(match_id,HomeTeam_name,AwayTeam_name)}', va='center',       
                  ha='center', size=15, color=pitch.line_color, fontproperties=fm_rubik.prop)

title4 = fig.text(x=0.76, y=0.17, s='Created by Davide Bernardi', va='center',
                  ha='center', size=10, color=pitch.line_color, fontproperties=fm_rubik.prop)

ax.legend(facecolor='#22312b', handlelength=5, edgecolor='None', fontsize=20,loc=[0.01,0.80])

#plt.title(f' World Cup: {HomeTeam_name} - {AwayTeam_name} {print_result(df,HomeTeam_name,AwayTeam_name)} \n xG: {XG_home(match_id,HomeTeam_name)} - {XG_away(match_id,AwayTeam_name)}\n{Most_involved(match_id,HomeTeam_name,AwayTeam_name)}',size=15, color=pitch.line_color)    

