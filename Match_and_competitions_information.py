# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 11:54:02 2021

@author: hp
"""
import matplotlib.pyplot as plt
import numpy as np
import json
import pandas as pd
from matplotlib.colors import to_rgba
from statsbombpy import sb
from mplsoccer import Pitch, FontManager,VerticalPitch
from mplsoccer.statsbomb import read_event, EVENT_SLUG
import seaborn as sns
from Shot_maps_function import Shot_OneColumns_maps,Shot_TwoColumns_maps_2
from matplotlib.cm import get_cmap

#C:\Users\hp\Desktop\Script python\Calcio\Da modificare\David\statsbomb_data\data
with open(rf'C:\Users\hp\Desktop\Script python\Calcio\Da modificare\Con Messi e euro2020\open-data-master\data\competitions.json') as data_file:
    #print (mypath+'events/'+file)
    competitions = json.load(data_file)


season_id=input('insert season id')
match_id=input('insert match id')

#encoding="utf8" solo per euro 2020 e forse messi
#:\Users\hp\Desktop\Script python\Calcio\Da modificare\David\statsbomb_data\data\
with open(rf'C:\Users\hp\Desktop\Script python\Calcio\Da modificare\Con Messi e euro2020\open-data-master\data\matches\{season_id}\{match_id}.json',  encoding="utf8") as data_file:
    #print (mypath+'events/'+file)
    data = json.load(data_file)
    
    
file_name=str(match_id)+'.json'    
    
from pandas.io.json import json_normalize
df = json_normalize(data, sep = "_").assign(match_id = file_name[:-5])

