import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.axes_grid1 import make_axes_locatable

a = np.load('../notebooks/resumen_merra_eolicos_2022.npy', allow_pickle = True).item()
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

series = pd.DataFrame()
series[0] = viento.loc[:,"1"]
series[1] = viento[["2","3","4","5","6","7","8","9"]].mean(axis=1)
series[2] = viento[["10","11","12","13"]].mean(axis=1)
series[3] = viento.loc[:,"14"]
series[4] = viento[["15","16","17","18","19","20"]].mean(axis=1)
series[5] = viento[["21","22","23"]].mean(axis=1)
series[6] = viento[["24","25"]].mean(axis=1)
series[7] = viento.loc[:,"26"]

iparques = [0,1,2,3,4,5,6,7]
grupos = ["Group 8", "Group 7", "Group 6", "Group 5","Group 4", "Group 3","Group 2", "Group 1"]
series = series.div(series.mean())
print("series")
print(series)
base=[]
baseY=[]
baseM=[]

for i in iparques:
  base.append(np.append(series[i].to_numpy(), np.array([np.nan]*0)).reshape(38,12) )  #tomo de a 12 y apilo
  baseY.append( series[i].groupby(series.index.year).aggregate({np.mean}) )
  baseM.append( series[i].groupby(series.index.month).aggregate({np.mean}) )


#############################################################3
def custom_plot(meses, anios, serie , ax, title = None, **plt_kwargs):
  img = ax.pcolormesh(anios.index,meses.index,serie.T,shading = 'nearest',cmap = 'jet',vmin=.75,vmax=1.25)
  ax.set_aspect(1.)
    
  ax.set_yticks([3, 6, 9, 12])
  ax.set_yticklabels(['3', '', '9', ''])
  ax.set_xticks([1980, 1990, 2000, 2010])
  # ~ ax.set_ylabel('Months', fontsize = 16)
  # ~ ax.set_title()
  ax.axvline(x=2016, color="black", linestyle="--")
  ax.tick_params(labelsize=16)
  ax.set_title(title, fontsize=16)
    # ~ ax.set_xticklabels(labels,rotation='vertical', fontsize=20)
    # ~ ax.set_yticklabels(labels2,rotation='horizontal', fontsize=20)
  
  # create new axes on the right and on the top of the current axes.
  '''
  divider = make_axes_locatable(ax)
  axMeanY = divider.append_axes("top", size=1, pad=0.02, sharex=ax)
  axMeanM = divider.append_axes("right", size=1, pad=0.02, sharey=ax)
  axMeanM.plot(meses.values,meses.index)
  axMeanY.plot(anios.index,anios.values)
  axMeanY.set_ylim(.9,1.1)
  axMeanM.set_xlim(.85,1.15)
  axMeanM.grid()
  axMeanY.grid()
  axMeanY.axvline(x=2016, color="black", linestyle="--")
  axMeanY.xaxis.set_tick_params(labelbottom=False)
  axMeanY.set_yticks([.95,1,1.05])
  axMeanY.set_yticklabels(['-5%','','+5%'])
  axMeanY.tick_params(labelsize=14)

  axMeanM.yaxis.set_tick_params(labelbottom=False)
  axMeanM.set_xticks([.95,1,1.05])
  axMeanM.set_xticklabels(['-5%  ','','  +5%'])
  axMeanM.tick_params(labelsize=14)
  
  ax.invert_yaxis()
  axMeanM.set_title(title, fontsize=16)
  '''
  return img;  #devuelvo la imagen para ponerle el cbar una sola vez

fig, axes = plt.subplots(nrows=4,ncols=2,figsize=(6,7), sharey=True, sharex=True)

for i,ax in enumerate(axes.flat):
  im = custom_plot(baseM[i],baseY[i],base[i],ax,title=grupos[i])
  
    
fig.subplots_adjust(bottom=0.15)
#le meto colorbar
axCb    = fig.add_axes([0.2, 0.1, .6, 0.02])
cbar = fig.colorbar(im, cax=axCb, orientation = 'horizontal') 
cbar.set_ticks([0.8,0.9,1,1.1,1.2])
cbar.set_ticklabels(['-20%','-10%','','+10%','+20%'])
cbar.set_label("wind speed variations", fontsize=16)
cbar.ax.tick_params(labelsize=16) 
fig.subplots_adjust(hspace=0.01,wspace=0.05)
plt.savefig('HPLOTgrupos.jpg', dpi=300, bbox_inches="tight")
fig.text(0.05,0.45, 'months',rotation= 'vertical',fontsize=16)

plt.savefig('HPLOTgrupos.jpg', dpi=300, bbox_inches="tight")

plt.show()

