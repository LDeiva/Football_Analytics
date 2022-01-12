# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 16:02:45 2021

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



def Shot_OneColumns_maps(dataframe,hometeamname,awayteamname):
    #Shot first half home team
    homefirsthalf=dataframe[((dataframe['type_name']=='Shot') & (dataframe['period']==1) & (dataframe['possession_team_name']==hometeamname))]
    for i in range(len(homefirsthalf['type_name'])):
        
        if (homefirsthalf['shot_outcome_name'].iloc[i]=='Goal'):
            plt.scatter(120-homefirsthalf['location'].iloc[i][0],homefirsthalf['location'].iloc[i][1],color='red',s=homefirsthalf['shot_statsbomb_xg'].iloc[i]*500)   
            plt.arrow(120-homefirsthalf['location'].iloc[i][0],homefirsthalf['location'].iloc[i][1],120-homefirsthalf['shot_end_location'].iloc[i][0]-(120-homefirsthalf['location'].iloc[i][0]),homefirsthalf['shot_end_location'].iloc[i][1]-homefirsthalf['location'].iloc[i][1], shape='full', color='b', length_includes_head=True, zorder=0, head_length=3., head_width=1.5)
        else:
            plt.scatter(120-homefirsthalf['location'].iloc[i][0],homefirsthalf['location'].iloc[i][1],color='green',s=homefirsthalf['shot_statsbomb_xg'].iloc[i]*500)   
            plt.arrow(120-homefirsthalf['location'].iloc[i][0],homefirsthalf['location'].iloc[i][1],120-homefirsthalf['shot_end_location'].iloc[i][0]-(120-homefirsthalf['location'].iloc[i][0]),homefirsthalf['shot_end_location'].iloc[i][1]-homefirsthalf['location'].iloc[i][1], shape='full', color='b', length_includes_head=True, zorder=0, head_length=3., head_width=1.5)
    #Shot second half home team
    homesecondhalf=dataframe[((dataframe['type_name']=='Shot') & (dataframe['period']==2) & (dataframe['possession_team_name']==hometeamname))]
    for i in range(len(homesecondhalf['type_name'])):
        if ( homesecondhalf['shot_outcome_name'].iloc[i]=='Goal'):
            plt.scatter(120- homesecondhalf['location'].iloc[i][0], homesecondhalf['location'].iloc[i][1],color='red',s= homesecondhalf['shot_statsbomb_xg'].iloc[i]*500)   
            plt.arrow(120- homesecondhalf['location'].iloc[i][0], homesecondhalf['location'].iloc[i][1],120-homesecondhalf['shot_end_location'].iloc[i][0]-(120- homesecondhalf['location'].iloc[i][0]), homesecondhalf['shot_end_location'].iloc[i][1]- homesecondhalf['location'].iloc[i][1], shape='full', color='b', length_includes_head=True, zorder=0, head_length=3., head_width=1.5)
        else:
            plt.scatter(120- homesecondhalf['location'].iloc[i][0], homesecondhalf['location'].iloc[i][1],color='green',s= homesecondhalf['shot_statsbomb_xg'].iloc[i]*500)   
            plt.arrow(120- homesecondhalf['location'].iloc[i][0], homesecondhalf['location'].iloc[i][1],120- homesecondhalf['shot_end_location'].iloc[i][0]-(120- homesecondhalf['location'].iloc[i][0]), homesecondhalf['shot_end_location'].iloc[i][1]- homesecondhalf['location'].iloc[i][1], shape='full', color='b', length_includes_head=True, zorder=0, head_length=3., head_width=1.5)
    #Shot first half away team
    awayfirsthalf=dataframe[((dataframe['type_name']=='Shot') & (dataframe['period']==1) & (dataframe['possession_team_name']==awayteamname))]
    for i in range(len(awayfirsthalf['type_name'])):
        
        if (awayfirsthalf['shot_outcome_name'].iloc[i]=='Goal'):
            plt.scatter(awayfirsthalf['location'].iloc[i][0],80-awayfirsthalf['location'].iloc[i][1],color='red',s=awayfirsthalf['shot_statsbomb_xg'].iloc[i]*500)   
            plt.arrow(awayfirsthalf['location'].iloc[i][0],80-awayfirsthalf['location'].iloc[i][1],awayfirsthalf['shot_end_location'].iloc[i][0]-awayfirsthalf['location'].iloc[i][0],80-awayfirsthalf['shot_end_location'].iloc[i][1]-(80-awayfirsthalf['location'].iloc[i][1]), shape='full', color='b', length_includes_head=True, zorder=0, head_length=3., head_width=1.5)
        else:
            plt.scatter(awayfirsthalf['location'].iloc[i][0],80-awayfirsthalf['location'].iloc[i][1],color='green',s=awayfirsthalf['shot_statsbomb_xg'].iloc[i]*500)   
            plt.arrow(awayfirsthalf['location'].iloc[i][0],80-awayfirsthalf['location'].iloc[i][1],awayfirsthalf['shot_end_location'].iloc[i][0]-awayfirsthalf['location'].iloc[i][0],80-awayfirsthalf['shot_end_location'].iloc[i][1]-(80-awayfirsthalf['location'].iloc[i][1]), shape='full', color='b', length_includes_head=True, zorder=0, head_length=3., head_width=1.5)
    #Shot second half away team
    awaysecondhalf=dataframe[((dataframe['type_name']=='Shot') & (dataframe['period']==2) & (dataframe['possession_team_name']==awayteamname))]
    for i in range(len(awaysecondhalf['type_name'])):
        if ( awaysecondhalf['shot_outcome_name'].iloc[i]=='Goal'):
            plt.scatter(awaysecondhalf['location'].iloc[i][0], 80-awaysecondhalf['location'].iloc[i][1],color='red',s= awaysecondhalf['shot_statsbomb_xg'].iloc[i]*500)   
            plt.arrow( awaysecondhalf['location'].iloc[i][0], 80-awaysecondhalf['location'].iloc[i][1],awaysecondhalf['shot_end_location'].iloc[i][0]-awaysecondhalf['location'].iloc[i][0], 80-awaysecondhalf['shot_end_location'].iloc[i][1]-(80- awaysecondhalf['location'].iloc[i][1]), shape='full', color='b', length_includes_head=True, zorder=0, head_length=3., head_width=1.5)
        else:
            plt.scatter( awaysecondhalf['location'].iloc[i][0], 80-awaysecondhalf['location'].iloc[i][1],color='green',s= awaysecondhalf['shot_statsbomb_xg'].iloc[i]*500)   
            plt.arrow( awaysecondhalf['location'].iloc[i][0], 80-awaysecondhalf['location'].iloc[i][1], awaysecondhalf['shot_end_location'].iloc[i][0]- awaysecondhalf['location'].iloc[i][0],80- awaysecondhalf['shot_end_location'].iloc[i][1]-(80-awaysecondhalf['location'].iloc[i][1]), shape='full', color='b', length_includes_head=True, zorder=0, head_length=3., head_width=1.5)
    
    #Shot first half extra Time home team
    homefirsthalf=dataframe[((dataframe['type_name']=='Shot') & (dataframe['period']==3) & (dataframe['possession_team_name']==hometeamname))]
    for i in range(len(homefirsthalf['type_name'])):
        
        if (homefirsthalf['shot_outcome_name'].iloc[i]=='Goal'):
            plt.scatter(120-homefirsthalf['location'].iloc[i][0],homefirsthalf['location'].iloc[i][1],color='red',s=homefirsthalf['shot_statsbomb_xg'].iloc[i]*500)   
            plt.arrow(120-homefirsthalf['location'].iloc[i][0],homefirsthalf['location'].iloc[i][1],120-homefirsthalf['shot_end_location'].iloc[i][0]-(120-homefirsthalf['location'].iloc[i][0]),homefirsthalf['shot_end_location'].iloc[i][1]-homefirsthalf['location'].iloc[i][1], shape='full', color='b', length_includes_head=True, zorder=0, head_length=3., head_width=1.5)
        else:
            plt.scatter(120-homefirsthalf['location'].iloc[i][0],homefirsthalf['location'].iloc[i][1],color='green',s=homefirsthalf['shot_statsbomb_xg'].iloc[i]*500)   
            plt.arrow(120-homefirsthalf['location'].iloc[i][0],homefirsthalf['location'].iloc[i][1],120-homefirsthalf['shot_end_location'].iloc[i][0]-(120-homefirsthalf['location'].iloc[i][0]),homefirsthalf['shot_end_location'].iloc[i][1]-homefirsthalf['location'].iloc[i][1], shape='full', color='b', length_includes_head=True, zorder=0, head_length=3., head_width=1.5)
    #Shot second half extra Time  home team
    homesecondhalf=dataframe[((dataframe['type_name']=='Shot') & (dataframe['period']==4) & (dataframe['possession_team_name']==hometeamname))]
    for i in range(len(homesecondhalf['type_name'])):
        if ( homesecondhalf['shot_outcome_name'].iloc[i]=='Goal'):
            plt.scatter(120- homesecondhalf['location'].iloc[i][0], homesecondhalf['location'].iloc[i][1],color='red',s= homesecondhalf['shot_statsbomb_xg'].iloc[i]*500)   
            plt.arrow(120- homesecondhalf['location'].iloc[i][0], homesecondhalf['location'].iloc[i][1],120-homesecondhalf['shot_end_location'].iloc[i][0]-(120- homesecondhalf['location'].iloc[i][0]), homesecondhalf['shot_end_location'].iloc[i][1]- homesecondhalf['location'].iloc[i][1], shape='full', color='b', length_includes_head=True, zorder=0, head_length=3., head_width=1.5)
        else:
            plt.scatter(120- homesecondhalf['location'].iloc[i][0], homesecondhalf['location'].iloc[i][1],color='green',s= homesecondhalf['shot_statsbomb_xg'].iloc[i]*500)   
            plt.arrow(120- homesecondhalf['location'].iloc[i][0], homesecondhalf['location'].iloc[i][1],120- homesecondhalf['shot_end_location'].iloc[i][0]-(120- homesecondhalf['location'].iloc[i][0]), homesecondhalf['shot_end_location'].iloc[i][1]- homesecondhalf['location'].iloc[i][1], shape='full', color='b', length_includes_head=True, zorder=0, head_length=3., head_width=1.5)
    
        #Shot first half Extra Time away team
    awayfirsthalf=dataframe[((dataframe['type_name']=='Shot') & (dataframe['period']==3) & (dataframe['possession_team_name']==awayteamname))]
    for i in range(len(awayfirsthalf['type_name'])):
        
        if (awayfirsthalf['shot_outcome_name'].iloc[i]=='Goal'):
            plt.scatter(awayfirsthalf['location'].iloc[i][0],80-awayfirsthalf['location'].iloc[i][1],color='red',s=awayfirsthalf['shot_statsbomb_xg'].iloc[i]*500)   
            plt.arrow(awayfirsthalf['location'].iloc[i][0],80-awayfirsthalf['location'].iloc[i][1],awayfirsthalf['shot_end_location'].iloc[i][0]-awayfirsthalf['location'].iloc[i][0],80-awayfirsthalf['shot_end_location'].iloc[i][1]-(80-awayfirsthalf['location'].iloc[i][1]), shape='full', color='b', length_includes_head=True, zorder=0, head_length=3., head_width=1.5)
        else:
            plt.scatter(awayfirsthalf['location'].iloc[i][0],80-awayfirsthalf['location'].iloc[i][1],color='green',s=awayfirsthalf['shot_statsbomb_xg'].iloc[i]*500)   
            plt.arrow(awayfirsthalf['location'].iloc[i][0],80-awayfirsthalf['location'].iloc[i][1],awayfirsthalf['shot_end_location'].iloc[i][0]-awayfirsthalf['location'].iloc[i][0],80-awayfirsthalf['shot_end_location'].iloc[i][1]-(80-awayfirsthalf['location'].iloc[i][1]), shape='full', color='b', length_includes_head=True, zorder=0, head_length=3., head_width=1.5)
    #Shot second half Extra Time away team
    awaysecondhalf=dataframe[((dataframe['type_name']=='Shot') & (dataframe['period']==4) & (dataframe['possession_team_name']==awayteamname))]
    for i in range(len(awaysecondhalf['type_name'])):
        if ( awaysecondhalf['shot_outcome_name'].iloc[i]=='Goal'):
            plt.scatter(awaysecondhalf['location'].iloc[i][0], 80-awaysecondhalf['location'].iloc[i][1],color='red',s= awaysecondhalf['shot_statsbomb_xg'].iloc[i]*500)   
            plt.arrow( awaysecondhalf['location'].iloc[i][0], 80-awaysecondhalf['location'].iloc[i][1],awaysecondhalf['shot_end_location'].iloc[i][0]-awaysecondhalf['location'].iloc[i][0], 80-awaysecondhalf['shot_end_location'].iloc[i][1]-(80- awaysecondhalf['location'].iloc[i][1]), shape='full', color='b', length_includes_head=True, zorder=0, head_length=3., head_width=1.5)
        else:
            plt.scatter( awaysecondhalf['location'].iloc[i][0], 80-awaysecondhalf['location'].iloc[i][1],color='green',s= awaysecondhalf['shot_statsbomb_xg'].iloc[i]*500)   
            plt.arrow( awaysecondhalf['location'].iloc[i][0], 80-awaysecondhalf['location'].iloc[i][1], awaysecondhalf['shot_end_location'].iloc[i][0]- awaysecondhalf['location'].iloc[i][0],80- awaysecondhalf['shot_end_location'].iloc[i][1]-(80-awaysecondhalf['location'].iloc[i][1]), shape='full', color='b', length_includes_head=True, zorder=0, head_length=3., head_width=1.5)
    plt.scatter([],[],color='red',s= 100,label='Goal')   
    plt.scatter([],[],color='green',s= 100,label='Shot')   
    return plt
            

def print_result(dataframe,hometeamname,awayteamname):
    Home_goal=dataframe[(dataframe['possession_team_name']==hometeamname) & (dataframe['shot_outcome_name']=='Goal') | (dataframe['type_name']=='Own Goal Against') & (dataframe['period']!=5)]
    home_goal=0
    for i in range(len(Home_goal)):
        home_goal+=1
    
    Away_goal=dataframe[(dataframe['possession_team_name']==awayteamname) & (dataframe['shot_outcome_name']=='Goal') | (dataframe['type_name']=='Own Goal Against') & (dataframe['period']!=5)]
    away_goal=0
    for i in range(len(Away_goal)):
        away_goal+=1
    #print(f'{home_goal} - {away_goal}')
    return f'{home_goal} - {away_goal}'

        










                        
            
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                     