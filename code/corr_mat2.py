import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np
import os

# ~ viento = pd.read_csv('/home/emi/Documents/vientohidro2/datos/viento.csv',header=0, delimiter = ';')
# ~ viento.index = pd.date_range(start="1980-01-01", end="2017-12-01",freq=pd.offsets.MonthBegin(1))

a = np.load('/home/emi/Documents/vientohidro2/notebooks/resumen_merra_eolicos_2022.npy', allow_pickle = True).item()
v50_m = a['v50_m']
v50_m.index = pd.date_range(start="1980-01-01", end="2022-06-01",freq=pd.offsets.MonthBegin(1))
mask = v50_m.index <= '2017-12-01'
v50_m = v50_m.loc[mask]

cols = v50_m.columns.tolist()
cols[0], cols[13] = cols[13], cols[0]
cols[8], cols[12] = cols[12], cols[8]
cols[8], cols[13] = cols[13], cols[8]
cols[19], cols[21] = cols[21], cols[19]
viento = v50_m[cols]
columnas = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26"]
viento.columns = columnas

sol = pd.read_csv('/home/emi/Documents/vientohidro2/datos/sol.csv',header=0, delimiter = ';')
sol.index = pd.date_range(start="1980-01-01", end="2017-12-01",freq=pd.offsets.MonthBegin(1))

cruz = pd.read_csv('/home/emi/Documents/vientohidro2/datos/sta_cruz.txt',header=None, na_values='-99')
cruz.index = pd.date_range(start="1980-01-01", end="2017-12-01",freq=pd.offsets.MonthBegin(1))

nqn = pd.read_csv('/home/emi/Documents/vientohidro2/datos/nqn.txt',header=None)
nqn.index = pd.date_range(start="1980-01-01", end="2017-12-01",freq=pd.offsets.MonthBegin(1))

limay = pd.read_csv('/home/emi/Documents/vientohidro2/datos/limay.txt',header=None)
limay.index = pd.date_range(start="1980-01-01", end="2017-12-01",freq=pd.offsets.MonthBegin(1))

series_v = pd.DataFrame()

series_v[0] = viento.loc[:,"1"]
series_v[1] = viento[["2","3","4","5","6","7","8","9"]].mean(axis=1)
series_v[2] = viento[["10","11","12","13"]].mean(axis=1)
series_v[3] = viento.loc[:,"14"]
series_v[4] = viento[["15","16","17","18","19","20"]].mean(axis=1)
series_v[5] = viento[["21","22","23"]].mean(axis=1)
series_v[6] = viento[["24","25"]].mean(axis=1)
series_v[7] = viento.loc[:,"26"]

series_s = pd.DataFrame()
series_s[0] = sol[["47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67"]].mean(axis=1)

##### promedios verano #####
cruz_ver = cruz.rolling(3).sum().iloc[13::12]
nqn_ver = nqn.rolling(6).sum().iloc[13::12]
limay_ver = limay.rolling(6).sum().iloc[13::12]
gr8_ver = series_v[0].rolling(3).mean().iloc[13::12]
gr7_ver = series_v[1].rolling(3).mean().iloc[13::12]
gr6_ver = series_v[2].rolling(3).mean().iloc[13::12]
gr5_ver = series_v[3].rolling(3).mean().iloc[13::12]
gr4_ver = series_v[4].rolling(3).mean().iloc[13::12]
gr3_ver = series_v[5].rolling(3).mean().iloc[13::12]
gr2_ver = series_v[6].rolling(3).mean().iloc[13::12]
gr1_ver = series_v[7].rolling(3).mean().iloc[13::12]
sol_ver = series_s[0].rolling(3).mean().iloc[13::12]

##### promedios invierno #####
cruz_inv = cruz.rolling(3).sum().iloc[7::12]
nqn_inv = nqn.rolling(6).sum().iloc[7::12]
limay_inv = limay.rolling(6).sum().iloc[7::12]
gr8_inv = series_v[0].rolling(3).mean().iloc[7::12]
gr7_inv = series_v[1].rolling(3).mean().iloc[7::12]
gr6_inv = series_v[2].rolling(3).mean().iloc[7::12]
gr5_inv = series_v[3].rolling(3).mean().iloc[7::12]
gr4_inv = series_v[4].rolling(3).mean().iloc[7::12]
gr3_inv = series_v[5].rolling(3).mean().iloc[7::12]
gr2_inv = series_v[6].rolling(3).mean().iloc[7::12]
gr1_inv = series_v[7].rolling(3).mean().iloc[7::12]
sol_inv = series_s[0].rolling(3).mean().iloc[7::12]


ver1 = pd.DataFrame()
ver1[0] = limay_ver
ver1[1] = nqn_ver
ver1[2] = cruz_ver
ver1[3] = sol_ver
ver2 = pd.DataFrame()
ver2[0] = gr1_ver
ver2[1] = gr2_ver
ver2[2] = gr3_ver
ver2[3] = gr4_ver
ver2[4] = gr5_ver
ver2[5] = gr6_ver
ver2[6] = gr7_ver
ver2[7] = gr8_ver
ver2[8] = sol_ver
ver1.columns =['Limay', 'Neuquen', 'S. Cruz', 'radiation']
ver2.columns = ['wind 1','wind 2','wind 3','wind 4','wind 5','wind 6','wind 7','wind 8','radiation']
corr_ver=pd.concat([ver2, ver1], axis=1, keys=['ver2', 'ver1']).corr().loc['ver1', 'ver2']

inv1 = pd.DataFrame()
inv1[0] = limay_inv
inv1[1] = nqn_inv
inv1[2] = cruz_inv
inv1[3] = sol_inv
inv2 = pd.DataFrame()
inv2[0] = gr1_inv
inv2[1] = gr2_inv
inv2[2] = gr3_inv
inv2[3] = gr4_inv
inv2[4] = gr5_inv
inv2[5] = gr6_inv
inv2[6] = gr7_inv
inv2[7] = gr8_inv
inv2[8] = sol_inv
inv1.columns =['Limay', 'Neuquen', 'S. Cruz', 'radiation']
inv2.columns = ['wind 1','wind 2','wind 3','wind 4','wind 5','wind 6','wind 7','wind 8','radiation']
corr_inv=pd.concat([inv2, inv1], axis=1, keys=['inv2', 'inv1']).corr().loc['inv1', 'inv2']


labels2 = ['Limay', 'Neuquen', 'S. Cruz', 'radiation']
labels = ['wind 1','wind 2','wind 3','wind 4','wind 5','wind 6','wind 7','wind 8', 'radiation']
estaciones = ["summer", "winter"]
mydfs = [corr_ver, corr_inv]

def custom_plot(corr, ax, title = None, **plt_kwargs):
    corr_mask = corr[(corr >= 0.312) | (corr <= -0.312)]
    sn.heatmap(corr_mask, annot=True, annot_kws={"size": 15}, cmap="PuOr",ax=ax, vmin= -1, vmax=1, linewidths=2,cbar=False)
    sn.heatmap(corr, cmap="PuOr",ax=ax,cbar=i == 0, vmin= -1, vmax=1, linewidths=2,cbar_ax=None if i else cbar_ax, cbar_kws={'label': 'corr. coefficient []'})
    ax.tick_params(labelsize=18, length=0)
    ax.set_title(title, fontsize=30)
    ax.set_xticklabels(labels,rotation='vertical', fontsize=20)
    ax.set_yticklabels(labels2,rotation='horizontal', fontsize=20)
    cbar_ax.yaxis.label.set_size(20)
    cbar_ax.tick_params(labelsize=20, length=0)  
    
fig, axes = plt.subplots(nrows=1,ncols=2,figsize=(18,4), sharey=True, sharex=True)
cbar_ax = fig.add_axes([.91, .3, .03, .4])

for i,ax in enumerate(axes.flat):
    im = custom_plot(mydfs[i],ax,title=estaciones[i])

fig.subplots_adjust(wspace=0.03)
plt.savefig('matrices2.png',dpi = 600,bbox_inches="tight")
plt.show()

