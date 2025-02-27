import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.axes_grid1 import make_axes_locatable
from scipy.stats import variation 
import scipy.stats as stats

a = np.load('../notebooks/resumen_merra_eolicos_2022.npy', allow_pickle = True).item()

v50_m = a['v50_m']
v50_m.index = pd.date_range(start="1980-01-01", end="2022-06-01",freq=pd.offsets.MonthBegin(1))
mask = v50_m.index <= '2017-12-01'
v50_m = v50_m.loc[mask]
viento = v50_m.mean(axis=1)
array_v =  viento.values
std_v = stats.tstd(array_v)
std_v = "{:.2f}".format(std_v)
cv_v = variation(array_v)
cv_v = "{:.2f}".format(cv_v)

b = np.load('../notebooks/resumen_merra_solares_2022.npy', allow_pickle = True).item()
rad_m = b['rad_m']
rad_m.index = pd.date_range(start="1980-01-01", end="2022-06-01",freq=pd.offsets.MonthBegin(1))
mask = rad_m.index <= '2017-12-01'
rad_m = rad_m.loc[mask]
sol = rad_m.mean(axis=1)
array_s =  sol.values
std_s = stats.tstd(array_s)
std_s = "{:.2f}".format(std_s)
cv_s = variation(array_s)
cv_s = "{:.2f}".format(cv_s)

cruz = pd.read_csv('/home/emi/Documents/vientohidro2/datos/sta_cruz.txt',header=None, na_values='-99')
cruz.index = pd.date_range(start="1980-01-01", end="2017-12-01",freq=pd.offsets.MonthBegin(1))
cruz2 = cruz.fillna(value=cruz.mean())
array_sc =  cruz2.values
std_sc = stats.tstd(array_sc)
cv_sc = variation(array_sc)

nqn = pd.read_csv('/home/emi/Documents/vientohidro2/datos/nqn.txt',header=None)
nqn.index = pd.date_range(start="1980-01-01", end="2017-12-01",freq=pd.offsets.MonthBegin(1))
array_n =  nqn.values
std_n = stats.tstd(array_n)
cv_n = variation(array_n)

limay = pd.read_csv('/home/emi/Documents/vientohidro2/datos/limay.txt',header=None)
limay.index = pd.date_range(start="1980-01-01", end="2017-12-01",freq=pd.offsets.MonthBegin(1))
array_l =  limay.values
std_l = stats.tstd(array_l)
cv_l = variation(array_l)

base_v=[]
baseY_v=[]
baseM_v=[]

base_s=[]
baseY_s=[]
baseM_s=[]

base_c=[]
baseY_c=[]
baseM_c=[]

base_n=[]
baseY_n=[]
baseM_n=[]

base_l=[]
baseY_l=[]
baseM_l=[]

base_v = viento.to_numpy().reshape(38,12)
baseY_v = viento.groupby(viento.index.year).aggregate({np.mean})
baseM_v = viento.groupby(viento.index.month).aggregate({np.mean})
print(base_v)

base_s = sol.to_numpy().reshape(38,12)
baseY_s = sol.groupby(sol.index.year).aggregate({np.mean})
baseM_s = sol.groupby(sol.index.month).aggregate({np.mean})

base_c = cruz.to_numpy().reshape(38,12)
baseY_c = cruz.groupby(cruz.index.year).aggregate({np.mean})
baseM_c = cruz.groupby(cruz.index.month).aggregate({np.mean})
baseY_c.iloc[12, 0] = 'NaN'
baseY_c.iloc[36, 0] = 'NaN'

base_n = nqn.to_numpy().reshape(38,12)
baseY_n = nqn.groupby(nqn.index.year).aggregate({np.mean})
baseM_n = nqn.groupby(nqn.index.month).aggregate({np.mean})

base_l = limay.to_numpy().reshape(38,12)
baseY_l = limay.groupby(limay.index.year).aggregate({np.mean})
baseM_l = limay.groupby(limay.index.month).aggregate({np.mean})

#############################################################

# ~ fig = plt.figure(figsize=(16, 13))
fig, (ax1,ax2,ax3) = plt.subplots(3, 1,figsize=(4,10))

### ax 1 ###

img1 = ax1.pcolormesh(baseY_v.index,baseM_v.index,base_v.T,shading = 'nearest',cmap = 'jet')
ax1.set_aspect(1.) 
ax1.set_yticks([3, 6, 9, 12])
ax1.set_yticklabels(['3', '', '9', ''])
ax1.set_xticks([1980, 1990, 2000, 2010])
ax1.set_ylabel('Months', fontsize=15)
ax1.axvline(x=2016, color="black", linestyle="--")
# ~ ax1.set_title('a)')
# create new axes on the right and on the top of the current axes.
  
divider = make_axes_locatable(ax1)
ax1MeanY = divider.append_axes("top", size=1, pad=0.02, sharex=ax1)
ax1MeanM = divider.append_axes("right", size=1, pad=0.02, sharey=ax1)
ax1MeanM.plot(baseM_v.values,baseM_v.index)
ax1MeanM.set_xlabel('[m/s]')
ax1MeanY.plot(baseY_v.index,baseY_v.values)
ax1MeanM.grid()
ax1MeanY.grid()
ax1MeanY.set_ylabel('[m/s]')
ax1MeanY.axvline(x=2016, color="black", linestyle="--")
ax1MeanY.xaxis.set_tick_params(labelbottom=False)

ax1MeanM.yaxis.set_tick_params(labelbottom=False)
ax1.invert_yaxis()
# ~ ax1MeanM.set_title("wind", fontsize=15)
cbar1 = fig.colorbar(img1, ax=ax1, orientation = 'horizontal',  fraction=0.07, anchor= (-4,0), pad=0.01)
cbar1.set_label("wind speed [m/s]", fontsize=15)

### ax 2 ###
img2 = ax2.pcolormesh(baseY_s.index,baseM_s.index,base_s.T,shading = 'nearest',cmap = 'hot_r')
ax2.set_aspect(1.) 
ax2.set_yticks([3, 6, 9, 12])
ax2.set_yticklabels(['3', '', '9', ''])
ax2.set_xticks([1980, 1990, 2000, 2016])
ax2.set_ylabel('Months', fontsize=15)
ax2.axvline(x=2016, color="black", linestyle="--")
# ~ ax2.set_title('b)')

# create new axes on the right and on the top of the current axes.
  
divider = make_axes_locatable(ax2)
ax2MeanY = divider.append_axes("top", size=1, pad=0.02, sharex=ax2)
ax2MeanM = divider.append_axes("right", size=1, pad=0.02, sharey=ax2)
ax2MeanM.plot(baseM_s.values,baseM_s.index)
ax2MeanM.set_xlabel('[W/$m^{2}$]')
ax2MeanY.plot(baseY_s.index,baseY_s.values)
ax2MeanM.grid()
ax2MeanY.grid()
ax2MeanY.set_ylabel('[W/$m^{2}$]')
ax2MeanY.axvline(x=2016, color="black", linestyle="--")
ax2MeanY.xaxis.set_tick_params(labelbottom=False)
ax2MeanM.yaxis.set_tick_params(labelbottom=False)
ax2.invert_yaxis()
# ~ ax2MeanM.set_title("radiation", fontsize=15)
cbar2 = fig.colorbar(img2, ax=ax2, orientation = 'horizontal',  fraction=0.07, anchor= (-4,0), pad=0.01) 
cbar2.set_label("radiation [W/$m^{2}$]", fontsize=15)

### ax 3 ###
img3 = ax3.pcolormesh(baseY_n.index,baseM_n.index,base_n.T,shading = 'nearest',cmap = 'Blues')
ax3.set_aspect(1.) 
ax3.set_yticks([3, 6, 9, 12])
ax3.set_yticklabels(['3', '', '9', ''])
ax3.set_xticks([1980, 1990, 2000, 2016])
ax3.set_ylabel('Months', fontsize=15)
ax3.axvline(x=2016, color="black", linestyle="--")
# ~ ax3.set_title('d)')

# create new axes on the right and on the top of the current axes.
  
divider = make_axes_locatable(ax3)
ax3MeanY = divider.append_axes("top", size=1, pad=0.02)
ax3MeanM = divider.append_axes("right", size=1, pad=0.02)
ax3MeanM.plot(baseM_n.values,baseM_n.index)
ax3MeanM.set_xlabel('[$m^{3}$/s]')
ax3MeanY.plot(baseY_n.index,baseY_n.values)
ax3MeanM.grid()
ax3MeanY.grid()
ax3MeanY.set_ylabel('[$m^{3}$/s]')
ax3MeanY.axvline(x=2016, color="black", linestyle="--")
ax3MeanY.xaxis.set_tick_params(labelbottom=False)
ax3MeanM.yaxis.set_tick_params(labelbottom=False)
ax3.invert_yaxis()
# ~ ax3MeanM.set_title("Streamflow", fontsize=15)
cbar3 = fig.colorbar(img3, ax=ax3, orientation = 'horizontal',  fraction=0.07, anchor= (-4,0), pad=0.01) 
cbar3.set_label("streamflow [$m^{3}$/s]", fontsize=15)



# ~ fig.text(0.3, 0.81, 'a) \n STDV:' + str(std_v) + 'm/s \n CV:' + str(cv_v) )    
# ~ fig.text(0.57, 0.81, 'b) \n STDV:' + str(std_s) + 'W/$m^{2}$ \n CV:' + str(cv_s))    
# ~ fig.text(0.3, 0.56, 'c) \n STDV: 215 $m^{3}$/s \n CV: 0.75')    
# ~ fig.text(0.57, 0.56, 'd) \n STDV: 127 $m^{3}$/s \n CV: 0.53')   
# ~ fig.text(0.3, 0.31, 'e) \n STDV: 360 $m^{3}$/s \n CV: 0.49')     
fig.subplots_adjust(bottom=0.05)
fig.subplots_adjust(hspace=0.05,wspace=0.05)
plt.savefig('abstract.png', dpi=600, bbox_inches="tight")

plt.show()

