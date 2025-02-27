import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.axes_grid1 import make_axes_locatable
import seaborn as sns
import scipy.stats as stats

a = np.load('/home/emi/Documents/vientohidro2/VH2/data/resumen_merra_eolicos_2022.npy', allow_pickle = True).item()

####### aao #######
aao = pd.read_csv('/home/emi/Documents/vientohidro2/datos/aao.csv',header=None,delimiter = ';')
aao = aao.iloc[: , 1:]
aao = aao.stack()
aao.index = pd.date_range(start="1980-01-01", end="2017-12-01",freq=pd.offsets.MonthBegin(1))

####### niño #######
nino34 = pd.read_csv('/home/emi/Documents/vientohidro2/datos/nino34.csv',header=None,delimiter = ';')
nino34 = nino34.iloc[: , 1:]
nino34 = nino34.stack()
nino34.index = pd.date_range(start="1980-01-01", end="2017-12-01",freq=pd.offsets.MonthBegin(1))

####### soi #######
soi = pd.read_csv('/home/emi/Documents/vientohidro2/datos/soi.csv',header=None,delimiter = ';')
soi = soi.iloc[: , 1:]
soi = soi.stack()
soi.index = pd.date_range(start="1980-01-01", end="2017-12-01",freq=pd.offsets.MonthBegin(1))

####### tsa #######
tsa = pd.read_csv('/home/emi/Documents/vientohidro2/datos/tsa.csv',header=None,delimiter = ';')
tsa = tsa.iloc[: , 1:]
tsa = tsa.stack()
tsa.index = pd.date_range(start="1980-01-01", end="2017-12-01",freq=pd.offsets.MonthBegin(1))

####### blob #######
blob = pd.read_csv('/home/emi/Documents/vientohidro2/datos/blob.csv',header=None,delimiter = ';')
blob = blob.iloc[: , 1:]
blob = blob.stack()
blob.index = pd.date_range(start="1980-01-01", end="2017-12-01",freq=pd.offsets.MonthBegin(1))

#### viento ####
v50_m = a['v50_m']
v50_m.index = pd.date_range(start="1980-01-01", end="2022-06-01",freq=pd.offsets.MonthBegin(1))
mask = v50_m.index <= '2017-12-01'
v50_m = v50_m.loc[mask]
viento = v50_m.mean(axis=1)
array_v =  viento.values.reshape(38,12)
viento_meses = pd.DataFrame(array_v, columns = ['1','2','3','4','5','6','7','8','9','10','11','12'])

v_q10 = [viento_meses['1'].quantile(q=0.1), viento_meses['2'].quantile(q=0.1), viento_meses['3'].quantile(q=0.1),
viento_meses['4'].quantile(q=0.1), viento_meses['5'].quantile(q=0.1), viento_meses['6'].quantile(q=0.1),
viento_meses['7'].quantile(q=0.1), viento_meses['8'].quantile(q=0.1), viento_meses['9'].quantile(q=0.1),
viento_meses['10'].quantile(q=0.1), viento_meses['11'].quantile(q=0.1), viento_meses['12'].quantile(q=0.1)]

v_q90 = [viento_meses['1'].quantile(q=0.9), viento_meses['2'].quantile(q=0.9), viento_meses['3'].quantile(q=0.9),
viento_meses['4'].quantile(q=0.9), viento_meses['5'].quantile(q=0.9), viento_meses['6'].quantile(q=0.9),
viento_meses['7'].quantile(q=0.9), viento_meses['8'].quantile(q=0.9), viento_meses['9'].quantile(q=0.9),
viento_meses['10'].quantile(q=0.9), viento_meses['11'].quantile(q=0.9), viento_meses['12'].quantile(q=0.9)]

v_q10 =  v_q10*38
v_q90 =  v_q90*38

viento_bajo=np.zeros(456)	
viento_alto=np.zeros(456)

#### sol ####
b = np.load('/home/emi/Documents/vientohidro2/datos/resumen_merra_solares_2022.npy', allow_pickle = True).item()
rad_m = b['rad_m']
rad_m.index = pd.date_range(start="1980-01-01", end="2022-06-01",freq=pd.offsets.MonthBegin(1))
mask = rad_m.index <= '2017-12-01'
rad_m = rad_m.loc[mask]
sol = rad_m.mean(axis=1)
array_s =  sol.values.reshape(38,12)
sol_meses = pd.DataFrame(array_s, columns = ['1','2','3','4','5','6','7','8','9','10','11','12'])

s_q10 = [sol_meses['1'].quantile(q=0.1), sol_meses['2'].quantile(q=0.1), sol_meses['3'].quantile(q=0.1),
sol_meses['4'].quantile(q=0.1), sol_meses['5'].quantile(q=0.1), sol_meses['6'].quantile(q=0.1),
sol_meses['7'].quantile(q=0.1), sol_meses['8'].quantile(q=0.1), sol_meses['9'].quantile(q=0.1),
sol_meses['10'].quantile(q=0.1), sol_meses['11'].quantile(q=0.1), sol_meses['12'].quantile(q=0.1)]

s_q90 = [sol_meses['1'].quantile(q=0.9), sol_meses['2'].quantile(q=0.9), sol_meses['3'].quantile(q=0.9),
sol_meses['4'].quantile(q=0.9), sol_meses['5'].quantile(q=0.9), sol_meses['6'].quantile(q=0.9),
sol_meses['7'].quantile(q=0.9), sol_meses['8'].quantile(q=0.9), sol_meses['9'].quantile(q=0.9),
sol_meses['10'].quantile(q=0.9), sol_meses['11'].quantile(q=0.9), sol_meses['12'].quantile(q=0.9)]


s_q10 =  s_q10*38
s_q90 =  s_q90*38

sol_bajo=np.zeros(456)	
sol_alto=np.zeros(456)

#### s cruz ####
cruz = pd.read_csv('/home/emi/Documents/vientohidro2/datos/sta_cruz.txt',header=None, na_values='-99')
cruz.index = pd.date_range(start="1980-01-01", end="2017-12-01",freq=pd.offsets.MonthBegin(1))
cruz2 = cruz.fillna(value=cruz.mean())
cruz3 = cruz2.values
array_c =  cruz2.values.reshape(38,12)
cruz_meses = pd.DataFrame(array_c, columns = ['1','2','3','4','5','6','7','8','9','10','11','12'])

c_q10 = [cruz_meses['1'].quantile(q=0.1), cruz_meses['2'].quantile(q=0.1), cruz_meses['3'].quantile(q=0.1),
cruz_meses['4'].quantile(q=0.1), cruz_meses['5'].quantile(q=0.1), cruz_meses['6'].quantile(q=0.1),
cruz_meses['7'].quantile(q=0.1), cruz_meses['8'].quantile(q=0.1), cruz_meses['9'].quantile(q=0.1),
cruz_meses['10'].quantile(q=0.1), cruz_meses['11'].quantile(q=0.1), cruz_meses['12'].quantile(q=0.1)]

c_q90 = [cruz_meses['1'].quantile(q=0.9), cruz_meses['2'].quantile(q=0.9), cruz_meses['3'].quantile(q=0.9),
cruz_meses['4'].quantile(q=0.9), cruz_meses['5'].quantile(q=0.9), cruz_meses['6'].quantile(q=0.9),
cruz_meses['7'].quantile(q=0.9), cruz_meses['8'].quantile(q=0.9), cruz_meses['9'].quantile(q=0.9),
cruz_meses['10'].quantile(q=0.9), cruz_meses['11'].quantile(q=0.9), cruz_meses['12'].quantile(q=0.9)]

c_q10 =  c_q10*38
c_q90 =  c_q90*38

cruz_bajo=np.zeros(456)	
cruz_alto=np.zeros(456)

#### neuquén ####
nqn = pd.read_csv('/home/emi/Documents/vientohidro2/datos/nqn.txt',header=None)
nqn.index = pd.date_range(start="1980-01-01", end="2017-12-01",freq=pd.offsets.MonthBegin(1))
nqn2=nqn.values
array_n =  nqn.values.reshape(38,12)
nqn_meses = pd.DataFrame(array_n, columns = ['1','2','3','4','5','6','7','8','9','10','11','12'])

n_q10 = [nqn_meses['1'].quantile(q=0.1), nqn_meses['2'].quantile(q=0.1), nqn_meses['3'].quantile(q=0.1),
nqn_meses['4'].quantile(q=0.1), nqn_meses['5'].quantile(q=0.1), nqn_meses['6'].quantile(q=0.1),
nqn_meses['7'].quantile(q=0.1), nqn_meses['8'].quantile(q=0.1), nqn_meses['9'].quantile(q=0.1),
nqn_meses['10'].quantile(q=0.1), nqn_meses['11'].quantile(q=0.1), nqn_meses['12'].quantile(q=0.1)]
print(n_q10)
n_q90 = [nqn_meses['1'].quantile(q=0.9), nqn_meses['2'].quantile(q=0.9), nqn_meses['3'].quantile(q=0.9),
nqn_meses['4'].quantile(q=0.9), nqn_meses['5'].quantile(q=0.9), nqn_meses['6'].quantile(q=0.9),
nqn_meses['7'].quantile(q=0.9), nqn_meses['8'].quantile(q=0.9), nqn_meses['9'].quantile(q=0.9),
nqn_meses['10'].quantile(q=0.9), nqn_meses['11'].quantile(q=0.9), nqn_meses['12'].quantile(q=0.9)]

n_q10 =  n_q10*38
n_q90 =  n_q90*38

nqn_bajo=np.zeros(456)	
nqn_alto=np.zeros(456)

#### limay ####
limay = pd.read_csv('/home/emi/Documents/vientohidro2/datos/limay.txt',header=None)
limay.index = pd.date_range(start="1980-01-01", end="2017-12-01",freq=pd.offsets.MonthBegin(1))
limay2=limay.values
array_l =  limay.values.reshape(38,12)
lim_meses = pd.DataFrame(array_l, columns = ['1','2','3','4','5','6','7','8','9','10','11','12'])

l_q10 = [lim_meses['1'].quantile(q=0.1), lim_meses['2'].quantile(q=0.1), lim_meses['3'].quantile(q=0.1),
lim_meses['4'].quantile(q=0.1), lim_meses['5'].quantile(q=0.1), lim_meses['6'].quantile(q=0.1),
lim_meses['7'].quantile(q=0.1), lim_meses['8'].quantile(q=0.1), lim_meses['9'].quantile(q=0.1),
lim_meses['10'].quantile(q=0.1), lim_meses['11'].quantile(q=0.1), lim_meses['12'].quantile(q=0.1)]

l_q90 = [lim_meses['1'].quantile(q=0.9), lim_meses['2'].quantile(q=0.9), lim_meses['3'].quantile(q=0.9),
lim_meses['4'].quantile(q=0.9), lim_meses['5'].quantile(q=0.9), lim_meses['6'].quantile(q=0.9),
lim_meses['7'].quantile(q=0.9), lim_meses['8'].quantile(q=0.9), lim_meses['9'].quantile(q=0.9),
lim_meses['10'].quantile(q=0.9), lim_meses['11'].quantile(q=0.9), lim_meses['12'].quantile(q=0.9)]

l_q10 =  l_q10*38
l_q90 =  l_q90*38

lim_bajo=np.zeros(456)	
lim_alto=np.zeros(456)

###### cuenta casos #########

for i in range(len(v_q10)):
	if viento[i] < v_q10[i]: viento_bajo[i] =1
	if viento[i] > v_q90[i]: viento_alto[i] =1
	if sol[i] < s_q10[i]: sol_bajo[i] =1
	if sol[i] > s_q90[i]: sol_alto[i] =1
	if cruz3[i] < c_q10[i]: cruz_bajo[i] =1
	if cruz3[i] > c_q90[i]: cruz_alto[i] =1
	if nqn2[i] < n_q10[i]: nqn_bajo[i] =1
	if nqn2[i] > n_q90[i]: nqn_alto[i] =1
	if limay2[i] < l_q10[i]: lim_bajo[i] =1
	if limay2[i] > l_q90[i]: lim_alto[i] =1

####### totales bajos ########
tot_bajos = viento_bajo + sol_bajo + cruz_bajo + nqn_bajo + lim_bajo
df_bajos = pd.DataFrame(tot_bajos)
df_bajos.index = pd.date_range(start="1980-01-01", end="2017-12-01",freq=pd.offsets.MonthBegin(1))
base_bajos = df_bajos.to_numpy().reshape(38,12)
baseY_bajos = df_bajos.groupby(df_bajos.index.year).aggregate({np.mean})
baseM_bajos = df_bajos.groupby(df_bajos.index.month).aggregate({np.mean})

####### totales altos ########
tot_altos = viento_alto + sol_alto + cruz_alto + nqn_alto + lim_alto
df_altos = pd.DataFrame(tot_altos)
df_altos.index = pd.date_range(start="1980-01-01", end="2017-12-01",freq=pd.offsets.MonthBegin(1))
base_altos = df_altos.to_numpy().reshape(38,12)
baseY_altos = df_altos.groupby(df_altos.index.year).aggregate({np.mean})
baseM_altos = df_altos.groupby(df_altos.index.month).aggregate({np.mean})

####### totales  ########
tot_tot = tot_altos - tot_bajos
df_tot = pd.DataFrame(tot_tot, columns=['A. index'])
df_tot.index = pd.date_range(start="1980-01-01", end="2017-12-01",freq=pd.offsets.MonthBegin(1))
base_tot = df_tot.to_numpy().reshape(38,12)
baseY_tot = df_tot.groupby(df_tot.index.year).aggregate({np.mean})
baseM_tot = df_tot.groupby(df_tot.index.month).aggregate({np.mean})
print(tot_tot)
# ~ print('corr aao')
arr_aao = aao.values
# ~ print(np.corrcoef(arr_aao,tot_tot))

print('corr niño')
arr_nino = nino34.values
print(np.corrcoef(arr_nino,tot_tot))

# ~ print('corr soi')
arr_soi = soi.values
# ~ print(np.corrcoef(arr_soi,tot_tot))

# ~ print('corr tsa')
arr_tsa = tsa.values
# ~ print(np.corrcoef(arr_tsa,tot_tot))

# ~ print('corr blob')
arr_blob = blob.values
# ~ print(np.corrcoef(arr_blob,tot_tot))

# ~ fig, ax = plt.subplots(2, 1,figsize=(5,2))
fig, ax = plt.subplots(1,2,figsize=(6.8,2), gridspec_kw={'width_ratios': [3, 1]})

img1 = ax[0].pcolormesh(baseY_tot.index,baseM_tot.index,base_tot.T,shading = 'nearest',cmap = 'coolwarm_r')
ax[0].set_yticks([3, 6, 9, 12])
ax[0].set_yticklabels(['9', '', '3', ''])
ax[0].set_ylabel('months', fontsize = 12) 
ax[0].set_xlabel('years', fontsize = 12) 

####### histograma ########
# ~ ax[1].set_xticklabels(['-4', '-2', '0', '2', '4'])
# ~ ax[1].set_xticks([-4,-2,0,2,4])
ax[1].set_xlim(-5, 5)
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
print(df_tot)
sns.histplot(ax=ax[1],data=df_tot, x="A. index", binwidth=1, alpha=.2)


cbar1 = fig.colorbar(img1, ax=ax[0], orientation = 'vertical',  fraction=0.07, pad=0.01)
# ~ cbar1 = fig.colorbar(img1, ax=ax[0], orientation = 'horizontal',  fraction=0.07, anchor= (-4,0), pad=0.2)
cbar1.set_label("A index", fontsize=12)
# ~ fig.subplots_adjust(bottom=0.15)
plt.subplots_adjust(wspace=0.3)

plt.savefig('CASES.png', dpi=600, bbox_inches="tight")

plt.show()

