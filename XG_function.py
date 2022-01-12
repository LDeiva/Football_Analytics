# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 17:35:08 2021

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

def XG_home(match_id,HomeTeam_name):
  
    with open(rf'C:\Users\hp\Desktop\Script python\Calcio\Da modificare\Con Messi e euro2020\open-data-master\data\events\{match_id}.json') as data_file:
        #print (mypath+'events/'+file)
        data = json.load(data_file)
        
    file_name=str(match_id)+'.json'    
        
    from pandas.io.json import json_normalize
    df= json_normalize(data, sep = "_").assign(match_id = file_name[:-5])
       
    #filter Data
    events=df[['team_name','type_name','minute','shot_statsbomb_xg','period']]
    
    #filtra per avere solo i tiri
    Shots=events[events['type_name']=='Shot']
    
    Shots_home=events[(events['type_name']=='Shot') & (events['team_name']==f'{HomeTeam_name}')  & (events['period']!= 3 ) & (events['period']!= 4 ) & (events['period']!= 5 )]
        
    #crea lista con expected golas
    xG_home=[]
    
    h_team=f'{HomeTeam_name}'
    #h_team=Shots['team_name'].iloc[0]
     
    h_time=[]
    
    for i in range(len(Shots_home['team_name'])):  
        if Shots_home['team_name'].iloc[i]==f'{h_team}':
            xG_home.append(Shots_home['shot_statsbomb_xg'].iloc[i])
            h_time.append(Shots_home['minute'].iloc[i])
           
        xG_home.insert(0, 0)
        
        h_time.insert(0, 0)
        #crea liste con expected goals flow cioè come variano minuto per minuto gli xG della partita
        xG_home_Flow=[sum(xG_home[:i+1]) for i in range(len(xG_home))]
        
        
    #estrai xG totala per entrambi
    xG_home_sum=xG_home_Flow[-1]
    
    xG_home_sum=str(xG_home_sum)
    xG_home_sum=xG_home_sum[:4]
    
    return xG_home_sum


def XG_away(match_id,AwayTeam_name):
    
    #match_id=7576
    #AwayTeam_name='Spain'
    with open(rf'C:\Users\hp\Desktop\Script python\Calcio\Da modificare\Con Messi e euro2020\open-data-master\data\events\{match_id}.json') as data_file:
        #print (mypath+'events/'+file)
        data = json.load(data_file)
        
    file_name=str(match_id)+'.json'    
        
    from pandas.io.json import json_normalize
    df= json_normalize(data, sep = "_").assign(match_id = file_name[:-5])
    
    
    #filter Data
    events=df[['team_name','type_name','minute','shot_statsbomb_xg','period']]
    
    #filtra per avere solo i tiri
    Shots=events[events['type_name']=='Shot']
    
    
    
    Shots_away=events[(events['type_name']=='Shot') & (events['team_name']==f'{AwayTeam_name}') & (events['period']!= 3 ) & (events['period']!= 4 ) & (events['period']!= 5 )]
    
    #crea lista con expected golas
    
    xG_away=[]
    
    a_team=f'{AwayTeam_name}'
    #a_team=Shots['team_name'].iloc[1]
        
    a_time=[]
      
    for i in range(len(Shots_away['team_name'])):
        if Shots_away['team_name'].iloc[i]==f'{a_team}':
            xG_away.append(Shots_away['shot_statsbomb_xg'].iloc[i])
            a_time.append(Shots_away['minute'].iloc[i])
        
        
    
    xG_away.insert(0, 0)
   
    a_time.insert(0, 0)

    #crea liste con expected goals flow cioè come variano minuto per minuto gli xG della partita
    
    
    xG_away_Flow=[sum(xG_away[:i+1]) for i in range(len(xG_away))]
    
    #estrai xG totla per entrambi
    
    
    xG_away_sum=xG_away_Flow[-1]
    xG_away_sum=str(xG_away_sum)
    xG_away_sum=xG_away_sum[:4]
    #xG_away_sum
    return xG_away_sum



def Most_involved(match_id,HomeTeam_name,AwayTeam_name):
    #match_id=8658
    #HomeTeam_name='France'
    #AwayTeam_name='Croatia'
    #Facciamo il most involved player per l'away team
    with open(rf'C:\Users\hp\Desktop\Script python\Calcio\Da modificare\Con Messi e euro2020\open-data-master\data\events\{match_id}.json') as data_file:
       #print (mypath+'events/'+file)
       data = json.load(data_file)
        
    file_name=str(match_id)+'.json'    
        
    from pandas.io.json import json_normalize
    df= json_normalize(data, sep = "_").assign(match_id = file_name[:-5])
    
    Filt=df[['shot_statsbomb_xg','player_name','possession_team_name','period']]
    Filt=Filt.dropna(subset=['shot_statsbomb_xg','player_name'])
    Filt=Filt[(Filt['possession_team_name']==AwayTeam_name)  & (Filt['period']!= 3 ) & (Filt['period']!= 4 ) & (Filt['period']!= 5 )]
    
    dictionary={}
    for i in range(len(Filt['shot_statsbomb_xg'])):
        #xG=Filt['shot_statsbomb_xg'].iloc[i]
        player_name=Filt['player_name'].iloc[i]
        dictionary[player_name] =  0
        
    for i in range(len(Filt['shot_statsbomb_xg'])):
        xG=Filt['shot_statsbomb_xg'].iloc[i]
        player_name=Filt['player_name'].iloc[i]
        dictionary[player_name] = dictionary[player_name] + xG
    
    lista=[]
    for i in dictionary:  
       lista.append(dictionary[i])
       
    Max=max(lista)
    key_list=list(dictionary.keys())
    val_list=list(dictionary.values())
    ind=val_list.index(Max)
    key_list[ind]
    
    Max=str(Max)
    Max=Max[:4]
    player=key_list[ind]
    player=player[:20]
    player=player.strip()
    
    #Facciamo il most involved player per l'home team
    Filt_home=df[['shot_statsbomb_xg','player_name','possession_team_name','period']]
    Filt_home=Filt_home.dropna(subset=['shot_statsbomb_xg','player_name'])
    Filt_home=Filt_home[(Filt_home['possession_team_name']==HomeTeam_name) & (Filt_home['period']!= 3 ) & (Filt_home['period']!= 4 ) & (Filt_home['period']!= 5 )]
    
    dictionary_home={}
    for i in range(len(Filt_home['shot_statsbomb_xg'])):
        #xG_home=Filt_home['shot_statsbomb_xg'].iloc[i]
        player_name_home=Filt_home['player_name'].iloc[i]
        dictionary_home[player_name_home] =  0
        
    for i in range(len(Filt_home['shot_statsbomb_xg'])):
        xG_home=Filt_home['shot_statsbomb_xg'].iloc[i]
        player_name_home=Filt_home['player_name'].iloc[i]
        dictionary_home[player_name_home] = dictionary_home[player_name_home] + xG_home
    
    lista_home=[]
    for i in dictionary_home:  
       lista_home.append(dictionary_home[i])
       
    Max_home=max(lista_home)
    key_list_home=list(dictionary_home.keys())
    val_list_home=list(dictionary_home.values())
    ind_home=val_list_home.index(Max_home)
    key_list_home[ind_home]
    
    Max_home=str(Max_home)
    Max_home=Max_home[:4]
    player_home=key_list_home[ind_home]
    player_home=player_home[:20]
    player_home=player_home.strip()
    
    
    if Max>Max_home:
       return f'Most involved player:{player} with {Max} xG'
    else:
        return f'Most involved player:{player_home} with {Max_home} xG'
    #return f'Most involved player:{player} with {Max} xG'
    
    
