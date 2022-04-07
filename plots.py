import math
import numpy as np
import scipy
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
import mesa_reader as mr
import os
from os.path import exists

MS_to_MJ = 1048
RS_to_RJ = 9.7
mas_names=['3','5','7','10','12']
mas=[3,5,7,10,12]
fenv_names=['0.1','0.01']

names=[]
for i in mas_names:
    name1 = 'm'+i+'f01'
    name2 = 'm'+i+'f001'
    locals()[name1] = mr.MesaData('LOGS/history_1e_evolve_'+i+'ME_0.1_9.0.data')
    locals()[name2] = mr.MesaData('LOGS/history_1e_evolve_'+i+'ME_0.01_9.0.data')
    names.append(name1)
    names.append(name2)
    
prfl_names=[]
for i in mas_names:
    for j in fenv_names:
        lis=[]
        for k in range(100):
            nam='LOGS/profile_'+i+'ME_'+j+'_9.0_'+str(k)+'.data'
            if exists(nam):
                lis.append(k)
            
            
        last_profile='LOGS/profile_'+i+'ME_'+j+'_9.0_'+str(lis[-1])+'.data'
        prfl_names.append('prfl_m'+i+'f0'+j.split('.')[-1])
        locals()['prfl_m'+i+'f0'+j.split('.')[-1]] = mr.MesaData(last_profile)

for i in names:
    locals()['age_'+i]=locals()[i].star_age
    locals()['r_'+i]=locals()[i].radius* RS_to_RJ 
    locals()['m_'+i]=locals()[i].star_mass* MS_to_MJ
    
fig5, ax = plt.subplots(2,5,figsize=[16,4])

for i in range(len(prfl_names)):
    flag1=i%2
    flag2=i//2
    axis=ax[flag1,flag2]
    axis.plot(locals()[prfl_names[i]].pressure,locals()[prfl_names[i]].T,color='r')
    #axis.plot(locals()[prfl_names[i]].R,locals()[prfl_names[i]].gradr,label=r'Radiative Gradient')
    #if i==0:
    #   axis.set_xticks([0.012,0.015,0.018,0.021,0.024])
    axis.set_ylim(0,2800)
    axis.set_yticks([0,500,1000,1500,2000,2500])
    axis.grid(axis='y')

fig5.text(0.088, 0.5, r'Temperature in Kelvin', va='center', rotation='vertical',size='11')
fig5.text(0.055, 0.8, r'$f_{env}=0.1$', va='center', size='10')
fig5.text(0.055, 0.2, r'$f_{env}=0.01$', va='center', size='10')
fig5.text(0.48, 0.03, r'Pressure', va='center',size='13')
fig5.text(0.16, .90, r'$M_{core}=3M_\bigoplus$', va='center',size='10')
fig5.text(0.32, .90, r'$M_{core}=5M_\bigoplus$', va='center',size='10')
fig5.text(0.48, .90, r'$M_{core}=7M_\bigoplus$', va='center',size='10')
fig5.text(0.64, .90, r'$M_{core}=10M_\bigoplus$', va='center',size='10')
fig5.text(0.80, .90, r'$M_{core}=12M_\bigoplus$', va='center',size='10')


plt.savefig('results/T-P.pdf')
plt.show()


    


