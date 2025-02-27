import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path 

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

aao = pd.read_csv('/home/emi/Documents/vientohidro2/datos/aao.csv',header=None,delimiter = ';')
aao = aao.iloc[: , 1:]
aao = aao.stack()
aao.index = pd.date_range(start="1980-01-01", end="2017-12-01",freq=pd.offsets.MonthBegin(1))

nino34 = pd.read_csv('/home/emi/Documents/vientohidro2/datos/nino34.csv',header=None,delimiter = ';')
nino34 = nino34.iloc[: , 1:]
nino34 = nino34.stack()
nino34.index = pd.date_range(start="1980-01-01", end="2017-12-01",freq=pd.offsets.MonthBegin(1))

soi = pd.read_csv('/home/emi/Documents/vientohidro2/datos/soi.csv',header=None,delimiter = ';')
soi = soi.iloc[: , 1:]
soi = soi.stack()
soi.index = pd.date_range(start="1980-01-01", end="2017-12-01",freq=pd.offsets.MonthBegin(1))

tsa = pd.read_csv('/home/emi/Documents/vientohidro2/datos/tsa.csv',header=None,delimiter = ';')
tsa = tsa.iloc[: , 1:]
tsa = tsa.stack()
tsa.index = pd.date_range(start="1980-01-01", end="2017-12-01",freq=pd.offsets.MonthBegin(1))

blob = pd.read_csv('/home/emi/Documents/vientohidro2/datos/blob.csv',header=None,delimiter = ';')
blob = blob.iloc[: , 1:]
blob = blob.stack()
blob.index = pd.date_range(start="1980-01-01", end="2017-12-01",freq=pd.offsets.MonthBegin(1))

pdo = pd.read_csv('/home/emi/Documents/vientohidro2/datos/pdo.csv',header=None,delimiter = ';')
pdo = pdo.iloc[: , 1:]
pdo = pdo.stack()
pdo.index = pd.date_range(start="1980-01-01", end="2017-12-01",freq=pd.offsets.MonthBegin(1))

ipo = pd.read_csv('/home/emi/Documents/vientohidro2/datos/IPO.csv',header=None,delimiter = ';')
ipo = ipo.iloc[: , 1:]
ipo = ipo.stack()
ipo.index = pd.date_range(start="1980-01-01", end="2017-12-01",freq=pd.offsets.MonthBegin(1))

ea = pd.read_csv('/home/emi/Documents/vientohidro2/datos/EA.csv',header=None,delimiter = ';')
ea = ea.iloc[: , 1:]
ea = ea.stack()
ea.index = pd.date_range(start="1980-01-01", end="2017-12-01",freq=pd.offsets.MonthBegin(1))

whwp = pd.read_csv('/home/emi/Documents/vientohidro2/datos/WHWP.csv',header=None,delimiter = ';')
whwp = whwp.iloc[: , 1:]
whwp = whwp.stack()
whwp.index = pd.date_range(start="1980-01-01", end="2017-12-01",freq=pd.offsets.MonthBegin(1))

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
cruz_efm = cruz.rolling(3).mean().iloc[2::12]
nqn_efm = nqn.rolling(3).mean().iloc[2::12]
limay_efm = limay.rolling(3).mean().iloc[2::12]
gr8_efm = series_v[0].rolling(3).mean().iloc[2::12]
gr7_efm = series_v[1].rolling(3).mean().iloc[2::12]
gr6_efm = series_v[2].rolling(3).mean().iloc[2::12]
gr5_efm = series_v[3].rolling(3).mean().iloc[2::12]
gr4_efm = series_v[4].rolling(3).mean().iloc[2::12]
gr3_efm = series_v[5].rolling(3).mean().iloc[2::12]
gr2_efm = series_v[6].rolling(3).mean().iloc[2::12]
gr1_efm = series_v[7].rolling(3).mean().iloc[2::12]
sol_efm = series_s[0].rolling(3).mean().iloc[2::12]
aao_efm = aao.rolling(3).mean().iloc[2::12]
nino34_efm = nino34.rolling(3).mean().iloc[2::12]
soi_efm = soi.rolling(3).mean().iloc[2::12]
tsa_efm = tsa.rolling(3).mean().iloc[2::12]
blob_efm = blob.rolling(3).mean().iloc[2::12]
pdo_efm = pdo.rolling(3).mean().iloc[2::12]
# ~ ipo_efm = ipo.rolling(3).mean().iloc[2::12]
# ~ ea_efm = ea.rolling(3).mean().iloc[2::12]
# ~ whwp_efm = whwp.rolling(3).mean().iloc[2::12]

##### promedios otoño #####
cruz_amj = cruz.rolling(3).mean().iloc[5::12]
nqn_amj = nqn.rolling(3).mean().iloc[5::12]
limay_amj = limay.rolling(3).mean().iloc[5::12]
gr8_amj = series_v[0].rolling(3).mean().iloc[5::12]
gr7_amj = series_v[1].rolling(3).mean().iloc[5::12]
gr6_amj = series_v[2].rolling(3).mean().iloc[5::12]
gr5_amj = series_v[3].rolling(3).mean().iloc[5::12]
gr4_amj = series_v[4].rolling(3).mean().iloc[5::12]
gr3_amj = series_v[5].rolling(3).mean().iloc[5::12]
gr2_amj = series_v[6].rolling(3).mean().iloc[5::12]
gr1_amj = series_v[7].rolling(3).mean().iloc[5::12]
sol_amj = series_s[0].rolling(3).mean().iloc[5::12]
aao_amj = aao.rolling(3).mean().iloc[5::12]
nino34_amj = nino34.rolling(3).mean().iloc[5::12]
soi_amj = soi.rolling(3).mean().iloc[5::12]
tsa_amj = tsa.rolling(3).mean().iloc[5::12]
blob_amj = blob.rolling(3).mean().iloc[5::12]
pdo_amj = pdo.rolling(3).mean().iloc[5::12]
# ~ ipo_amj = ipo.rolling(3).mean().iloc[5::12]
# ~ ea_amj = ea.rolling(3).mean().iloc[5::12]
# ~ whwp_amj = whwp.rolling(3).mean().iloc[5::12]

##### promedios invierno #####
cruz_jas = cruz.rolling(3).mean().iloc[8::12]
nqn_jas = nqn.rolling(3).mean().iloc[8::12]
limay_jas = limay.rolling(3).mean().iloc[8::12]
gr8_jas = series_v[0].rolling(3).mean().iloc[8::12]
gr7_jas = series_v[1].rolling(3).mean().iloc[8::12]
gr6_jas = series_v[2].rolling(3).mean().iloc[8::12]
gr5_jas = series_v[3].rolling(3).mean().iloc[8::12]
gr4_jas = series_v[4].rolling(3).mean().iloc[8::12]
gr3_jas = series_v[5].rolling(3).mean().iloc[8::12]
gr2_jas = series_v[6].rolling(3).mean().iloc[8::12]
gr1_jas = series_v[7].rolling(3).mean().iloc[8::12]
sol_jas = series_s[0].rolling(3).mean().iloc[8::12]
aao_jas = aao.rolling(3).mean().iloc[8::12]
nino34_jas = nino34.rolling(3).mean().iloc[8::12]
soi_jas = soi.rolling(3).mean().iloc[8::12]
tsa_jas = tsa.rolling(3).mean().iloc[8::12]
blob_jas = blob.rolling(3).mean().iloc[8::12]
pdo_jas = pdo.rolling(3).mean().iloc[8::12]
# ~ ipo_jas = ipo.rolling(3).mean().iloc[8::12]
# ~ ea_jas = ea.rolling(3).mean().iloc[8::12]
# ~ whwp_jas = whwp.rolling(3).mean().iloc[8::12]

##### promedios primavera #####
cruz_ond = cruz.rolling(3).mean().iloc[11::12]
nqn_ond = nqn.rolling(3).mean().iloc[11::12]
limay_ond = limay.rolling(3).mean().iloc[11::12]
gr8_ond = series_v[0].rolling(3).mean().iloc[11::12]
gr7_ond = series_v[1].rolling(3).mean().iloc[11::12]
gr6_ond = series_v[2].rolling(3).mean().iloc[11::12]
gr5_ond = series_v[3].rolling(3).mean().iloc[11::12]
gr4_ond = series_v[4].rolling(3).mean().iloc[11::12]
gr3_ond = series_v[5].rolling(3).mean().iloc[11::12]
gr2_ond = series_v[6].rolling(3).mean().iloc[11::12]
gr1_ond = series_v[7].rolling(3).mean().iloc[11::12]
sol_ond = series_s[0].rolling(3).mean().iloc[11::12]
aao_ond = aao.rolling(3).mean().iloc[11::12]
nino34_ond = nino34.rolling(3).mean().iloc[11::12]
soi_ond = soi.rolling(3).mean().iloc[11::12]
tsa_ond = tsa.rolling(3).mean().iloc[11::12]
blob_ond = blob.rolling(3).mean().iloc[11::12]
pdo_ond = pdo.rolling(3).mean().iloc[11::12]
# ~ ipo_ond = ipo.rolling(3).mean().iloc[11::12]
# ~ ea_ond = ea.rolling(3).mean().iloc[11::12]
# ~ whwp_ond = whwp.rolling(3).mean().iloc[11::12]

efm = pd.DataFrame()
efm[0] = limay_efm
efm[1] = nqn_efm
efm[2] = cruz_efm
efm[3] = gr1_efm
efm[4] = gr2_efm
efm[5] = gr3_efm
efm[6] = gr4_efm
efm[7] = gr5_efm
efm[8] = gr6_efm
efm[9] = gr7_efm
efm[10] = gr8_efm
efm[11] = sol_efm
efm2 = pd.DataFrame()
efm2[0] = aao_efm
efm2[1] = soi_efm
efm2[2] = nino34_efm
efm2[3] = tsa_efm
efm2[4] = blob_efm
efm2[5] = pdo_efm
# ~ efm2[6] = ipo_efm
# ~ efm2[7] = whwp_efm
# ~ efm2[8] = ea_efm
efm.columns =['Limay', 'Neuquen', 'S. Cruz', 'wind 1','wind 2','wind 3','wind 4','wind 5','wind 6','wind 7','wind 8', 'radiation']
# ~ efm2.columns =['aao', 'soi', 'n3.4', 'tsa', 'blob','pdo','ipo','whwp','ea']
efm2.columns =['aao', 'soi', 'n3.4', 'tsa', 'blob','pdo']

corr_efm=pd.concat([efm, efm2], axis=1, keys=['efm', 'efm2']).corr(method='spearman').loc['efm2', 'efm']

amj = pd.DataFrame()
amj[0] = limay_amj
amj[1] = nqn_amj
amj[2] = cruz_amj
amj[3] = gr1_amj
amj[4] = gr2_amj
amj[5] = gr3_amj
amj[6] = gr4_amj
amj[7] = gr5_amj
amj[8] = gr6_amj
amj[9] = gr7_amj
amj[10] = gr8_amj
amj[11] = sol_amj
amj2 = pd.DataFrame()
amj2[0] = aao_amj
amj2[1] = soi_amj
amj2[2] = nino34_amj
amj2[3] = tsa_amj
amj2[4] = blob_amj
amj2[5] = pdo_amj
# ~ amj2[6] = ipo_amj
# ~ amj2[7] = whwp_amj
# ~ amj2[8] = ea_amj
amj.columns =['Limay', 'Neuquen', 'S. Cruz', 'wind 1','wind 2','wind 3','wind 4','wind 5','wind 6','wind 7','wind 8', 'radiation']
# ~ amj2.columns =['aao', 'soi', 'n3.4', 'tsa', 'blob', 'pdo','ipo','whwp','ea']
amj2.columns =['aao', 'soi', 'n3.4', 'tsa', 'blob', 'pdo']
corr_amj=pd.concat([amj, amj2], axis=1, keys=['amj', 'amj2']).corr(method='spearman').loc['amj2', 'amj']

jas = pd.DataFrame()
jas[0] = limay_jas
jas[1] = nqn_jas
jas[2] = cruz_jas
jas[3] = gr1_jas
jas[4] = gr2_jas
jas[5] = gr3_jas
jas[6] = gr4_jas
jas[7] = gr5_jas
jas[8] = gr6_jas
jas[9] = gr7_jas
jas[10] = gr8_jas
jas[11] = sol_jas
jas2 = pd.DataFrame()
jas2[0] = aao_jas
jas2[1] = soi_jas
jas2[2] = nino34_jas
jas2[3] = tsa_jas
jas2[4] = blob_jas
jas2[5] = pdo_jas
# ~ jas2[6] = ipo_jas
# ~ jas2[7] = whwp_jas
# ~ jas2[8] = ea_jas
jas.columns =['Limay', 'Neuquen', 'S. Cruz', 'wind 1','wind 2','wind 3','wind 4','wind 5','wind 6','wind 7','wind 8', 'radiation']
# ~ jas2.columns =['aao', 'soi', 'n3.4', 'tsa', 'blob','pdo','ipo','whwp','ea']
jas2.columns =['aao', 'soi', 'n3.4', 'tsa', 'blob','pdo']

corr_jas=pd.concat([jas, jas2], axis=1, keys=['jas', 'jas2']).corr(method='spearman').loc['jas2', 'jas']

ond = pd.DataFrame()
ond[0] = limay_ond
ond[1] = nqn_ond
ond[2] = cruz_ond
ond[3] = gr1_ond
ond[4] = gr2_ond
ond[5] = gr3_ond
ond[6] = gr4_ond
ond[7] = gr5_ond
ond[8] = gr6_ond
ond[9] = gr7_ond
ond[10] = gr8_ond
ond[11] = sol_ond
ond2 = pd.DataFrame()
ond2[0] = aao_ond
ond2[1] = soi_ond
ond2[2] = nino34_ond
ond2[3] = tsa_ond
ond2[4] = blob_ond
ond2[5] = pdo_ond
# ~ ond2[6] = ipo_ond
# ~ ond2[7] = whwp_ond
# ~ ond2[8] = ea_ond
ond.columns =['Limay', 'Neuquen', 'S. Cruz', 'wind 1','wind 2','wind 3','wind 4','wind 5','wind 6','wind 7','wind 8', 'radiation']
# ~ ond2.columns =['aao', 'soi', 'n3.4', 'tsa', 'blob','pdo','ipo','whwp','ea']
ond2.columns =['aao', 'soi', 'n3.4', 'tsa', 'blob','pdo']
corr_ond=pd.concat([ond, ond2], axis=1, keys=['ond', 'ond2']).corr(method='spearman').loc['ond2', 'ond']

labels = ['Limay', 'Neuquen', 'S. Cruz', 'wind 1','wind 2','wind 3','wind 4','wind 5','wind 6','wind 7','wind 8', 'radiation']
# ~ labels2 = ['aao', 'soi', 'n3.4', 'tsa', 'blob','pdo','ipo','whwp','ea']
labels2 = ['aao', 'soi', 'n3.4', 'tsa', 'sb','pdo']

estaciones = ["summer", "autumn", "winter", "spring"]
mydfs = [corr_efm, corr_amj, corr_jas, corr_ond]

def custom_plot(corr, ax, title = None, **plt_kwargs):
    corr_mask = corr[(corr >= 0.321) | (corr <= -0.321)]
    sn.heatmap(corr_mask, annot=True, annot_kws={"size": 13}, cmap="PuOr",ax=ax, vmin= -1, vmax=1, linewidths=2,cbar=False)
    sn.heatmap(corr, cmap="PuOr",ax=ax,cbar=i == 0, vmin= -1, vmax=1, linewidths=2,cbar_ax=None if i else cbar_ax, cbar_kws={'label': 'corr. coefficient []'})
    ax.tick_params(labelsize=18, length=0)
    ax.set_title(title, fontsize=30)
    ax.set_xticklabels(labels,rotation='vertical', fontsize=20)
    ax.set_yticklabels(labels2,rotation='horizontal', fontsize=20)
    cbar_ax.yaxis.label.set_size(20)
    cbar_ax.tick_params(labelsize=20, length=0)  
    
fig, axes = plt.subplots(nrows=2,ncols=2,figsize=(15,6), sharey=True, sharex=True)

cbar_ax = fig.add_axes([.91, .3, .03, .4])

for i,ax in enumerate(axes.flat):
    im = custom_plot(mydfs[i],ax,title=estaciones[i])

fig.subplots_adjust(wspace=0.03)
plt.savefig('corr_indices.png',dpi = 600,bbox_inches="tight")
plt.show()


