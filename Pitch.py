# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 10:59:05 2021

@author: hp
"""

import pandas as pd
from mplsoccer.pitch import Pitch
from matplotlib import pyplot as plt
from Shot_maps_function import Shot_OneColumns_maps,Shot_TwoColumns_maps



df=pd.read_csv(r'C:\Users\hp\Desktop\Script python\Calcio\Da modificare\McKay Johns\Parma_Atalanta.csv')
messi=pd.read_csv(r'C:\Users\hp\Desktop\Script python\Calcio\Da modificare\McKay Johns\messibetis.csv')
df['x']=df['x']*19
df['y']=df['y']*95.31

df=df[df['team']=='Atalanta']
messi['x']=messi['x']*1.2
messi['y']=messi['y']*0.8
pitch=Pitch(pitch_color='grass',line_color='white',stripe=True)
fig,ax=pitch.draw()

plt.scatter(messi['x'],messi['y'])


