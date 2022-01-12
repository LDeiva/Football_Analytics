# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 17:05:14 2021

@author: hp
"""

import pandas as pd
from mplsoccer import Radar, FontManager
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
Ramos=pd.read_excel(r'C:\Users\hp\Desktop\Script python\Calcio\Da modificare\McKay Johns\Fatti da me\Dati\Fbref\Ramos.xlsx', skiprows=[0])
Chiellini=pd.read_excel(r'C:\Users\hp\Desktop\Script python\Calcio\Da modificare\McKay Johns\Fatti da me\Dati\Fbref\Chiellini.xlsx')
#Prendo i dati solo della stagione 2018/2019
C=Chiellini.iloc[[17]]

C=C.drop(['Tkl%','%','Season','Age','Squad','Country','Comp','LgRank','90s','Matches','Mid 3rd','Att 3rd','Past','Att 3rd.1','ShSv','Err'], axis = 1)
colonne=C.columns
C=C.values
C=list(C)
C=C[0]
C=list(C)
C=[float(i) for i in C]
Colonne=list(colonne)
R=Ramos.iloc[[16]]

frames=[colonne,C,R]
result = pd.concat(frames).reset_index()
prova=Ramos['Tkl']
#crea low e high value

low=[]
high=[]
for i in range((len(C.columns))):
    x=result.iloc[1,i]
    y=result.iloc[2,i]
    if x>y:
        
#Riporto esempi su sito
# parameter names of the statistics we want to show
params = ["npxG", "Non-Penalty Goals", "xA", "Key Passes", "Through Balls", "Progressive Passes", "Shot-Creating Actions", "Goal-Creating Actions","Dribbles Completed", "Pressure Regains", "Touches In Box"]

URL4 = 'https://github.com/googlefonts/roboto/blob/main/src/hinted/Roboto-Thin.ttf?raw=true'
robotto_thin = FontManager(URL4)
URL5 = 'https://github.com/googlefonts/roboto/blob/main/src/hinted/Roboto-Regular.ttf?raw=true'
robotto_regular = FontManager(URL5)
# The lower and upper boundaries for the statistics
Min=[]
Max=[]

for i in C:
    Min.append(i-i*0.3)
    Max.append(i+i*0.3)

low =  [0.08, 0.0, 0.1, 1, 0.6,  4, 3, 0.3, 0.3, 2.0, 2,0.08, 0.0, 0.1, 1]
high = [0.37, 0.6, 0.6, 4, 1.2, 10, 8, 1.3, 1.5, 5.5, 5,0.37, 0.6, 0.6, 4]

#Players values
bruno_values =  [0.25, 0.42, 0.42, 3.47, 1.04, 8.06, 5.62, 0.97, 0.56, 5.14, 3.54]
bruyne_values = [0.32, 0.00, 0.43, 3.50, 0.98, 7.72, 6.18, 0.98, 1.71, 4.88, 4.96]
#inizalizzo radar
Radar = Radar(Colonne,Min,Max,
              # whether to round any of the labels to integers instead of decimal places
              round_int=[False]*15,
              num_rings=4,  # the number of concentric circles (excluding center circle)
              # if the ring_width is more than the center_circle_radius then
              # the center circle radius will be wider than the width of the concentric circles
              ring_width=1, center_circle_radius=1)
#plotto radar
fig, ax = Radar.setup_axis()  # format axis as a radar
rings_inner = Radar.draw_circles(ax=ax, facecolor='#ffb2b2', edgecolor='#fc5f5f')  # draw circles
radar_output = Radar.draw_radar(C, ax=ax,
                                kwargs_radar={'facecolor': '#aa65b2'},
                                kwargs_rings={'facecolor': '#66d8ba'})  # draw the radar
radar_poly, rings_outer, vertices = radar_output
range_labels = Radar.draw_range_labels(ax=ax, fontsize=15,
                                       fontproperties=robotto_thin.prop)  # draw the range labels
param_labels = Radar.draw_param_labels(ax=ax, fontsize=15,
                                       fontproperties=robotto_regular.prop)  # draw the param labels

#nuovo metodo
plt.style.use('ggplot')
angles=np.linspace(0,2*np.pi,len(Colonne), endpoint=False)
print(angles)

angles=np.linspace(0,2*np.pi,len(Colonne), endpoint=False)
print(angles)

angles=np.concatenate((angles,[angles[0]]))
print(angles)

Colonne.append(Colonne[0])
C.append(C[0])


fig=plt.figure(figsize=(6,6))
ax=fig.add_subplot(polar=True)
ax.plot(angles,C)
plt.show()