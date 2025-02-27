import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.axes_grid1 import make_axes_locatable
import pymannkendall as mk
from scipy.stats import variation 
import scipy.stats as stats
import pymannkendall as mk


a = np.load('../notebooks/resumen_merra_eolicos_2022.npy', allow_pickle = True).item()
# ~ print(a)
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

limay = pd.read_csv('/home/emi/Documents/vientohidro2/datos/limay.txt',header=None)
limay.index = pd.date_range(start="1980-01-01", end="2017-12-01",freq=pd.offsets.MonthBegin(1))

nqn = pd.read_csv('/home/emi/Documents/vientohidro2/datos/nqn.txt',header=None)
nqn.index = pd.date_range(start="1980-01-01", end="2017-12-01",freq=pd.offsets.MonthBegin(1))
# ~ print(nqn)
blob = pd.read_csv('/home/emi/Documents/vientohidro2/datos/blob.csv',header=None,delimiter = ';')
blob = blob.iloc[: , 1:]
blob = blob.stack()
blob.index = pd.date_range(start="1980-01-01", end="2017-12-01",freq=pd.offsets.MonthBegin(1))
# ~ print(blob)
pdo = pd.read_csv('/home/emi/Documents/vientohidro2/datos/pdo.csv',header=None,delimiter = ';')
pdo = pdo.iloc[: , 1:]
pdo = pdo.stack()
pdo.index = pd.date_range(start="1980-01-01", end="2017-12-01",freq=pd.offsets.MonthBegin(1))

aao = pd.read_csv('/home/emi/Documents/vientohidro2/datos/aao.csv',header=None,delimiter = ';')
aao = aao.iloc[: , 1:]
aao = aao.stack()
aao.index = pd.date_range(start="1980-01-01", end="2017-12-01",freq=pd.offsets.MonthBegin(1))
print(aao)
######## prom y prom movil ##########
#########gr 6 ###########
gr6PM = series[2].rolling(12).mean().iloc[11::12]
mask1 = series[2].index <= '2002-02-01'
mask2 = series[2].index > '2002-09-01'
gr6pre = series[2].loc[mask1]
gr6pos = series[2].loc[mask2]
media1 = pd.DataFrame()
media2 = pd.DataFrame()
media1.index = gr6pre.index
media2.index = gr6pos.index
media1[0] = gr6pre.mean()
media2[0] = gr6pos.mean()

#########gr 7 ###########
gr7PM = series[1].rolling(12).mean().iloc[11::12]
print(gr7PM)
mask3 = series[1].index <= '2002-09-01'
mask4 = series[1].index > '2002-09-01'
gr7pre = series[1].loc[mask3]
gr7pos = series[1].loc[mask4]
media3 = pd.DataFrame()
media4 = pd.DataFrame()
media3.index = gr7pre.index
media4.index = gr7pos.index
media3[0] = gr7pre.mean()
media4[0] = gr7pos.mean()

######### Neuquen ###########
nqnPM = nqn.rolling(12).mean().iloc[11::12]
mask5 = nqn.index <= '2006-12-01'
mask6 = nqn.index > '2009-12-01'
nqnpre = nqn.loc[mask5]
nqnpos = nqn.loc[mask6]
media5 = pd.DataFrame()
media6 = pd.DataFrame()
media5.index = nqnpre.index
media6.index = nqnpos.index
media5[0] = nqnpre.mean()[0]
media6[0] = nqnpos.mean()[0]

######### Blob ###########
blobPM = blob.rolling(12).mean().iloc[11::12]
mask7 = blob.index <= '1995-06-01'
mask8 = blob.index > '1995-06-01'
blobpre = blob.loc[mask7]
blobpos = blob.loc[mask8]
media7 = pd.DataFrame()
media8 = pd.DataFrame()
media7.index = blobpre.index
media8.index = blobpos.index
media7[0] = blobpre.mean()
media8[0] = blobpos.mean()

######### PDO ###########
pdoPM = pdo.rolling(12).mean().iloc[11::12]
mask9 = pdo.index <= '1997-06-01'
mask10 = pdo.index > '1997-06-01'
pdopre = pdo.loc[mask9]
pdopos = pdo.loc[mask10]
media9 = pd.DataFrame()
media10 = pd.DataFrame()
media9.index = pdopre.index
media10.index = pdopos.index
media9[0] = pdopre.mean()
media10[0] = pdopos.mean()

######### AAO ###########
aaoPM = aao.rolling(12).mean().iloc[11::12]
t_aao = mk.original_test(aaoPM)
mask11 = aao.index > '2002-09-01'
aaopos = aao.loc[mask11]
x = np.arange(38)
x2 = np.arange(183)


fig = plt.figure(figsize=(7, 5))

ax1= fig.add_subplot(3,3,1)
ax2= fig.add_subplot(3,3,2)
ax3= fig.add_subplot(3,3,3)
ax4= fig.add_subplot(3,3,4)
ax5= fig.add_subplot(3,3,5)
ax6= fig.add_subplot(3,3,6)


############ grafico 1 ###########
ax1.plot(gr6PM)
ax1.plot(media1, color="black")
ax1.plot(media2, color="black")
ax1.set_ylabel('[m/s]', fontsize=11)
ax1.set_xlim([pd.Timestamp('1980-01-01'), pd.Timestamp('2017-12-01')])
ax1.xaxis.set_tick_params(labelsize = 0, labelcolor = 'white')
ax1.yaxis.set_tick_params(labelsize=11)
ax1.set_title('Group 6 ', fontsize=11)
ax1.text(pd.Timestamp('1985-01-01'),7.6, 'CP = 2002', fontsize=10)
# ~ ax1.tick_params(axis='x', labelrotation = 90, labelsize=11)

############ grafico 2 ###########
ax2.plot(gr7PM)
ax2.plot(media3, color="black")
ax2.plot(media4, color="black")
ax2.set_ylabel('[m/s]', fontsize=11)
ax2.set_xlim([pd.Timestamp('1980-01-01'), pd.Timestamp('2017-12-01')])
ax2.xaxis.set_tick_params(labelsize = 0, labelcolor = 'white')
ax2.yaxis.set_tick_params(labelsize=11)
ax2.set_title('Group 7 ', fontsize=11)
ax2.text(pd.Timestamp('1985-01-01'),8.2, 'CP = 2002', fontsize=10)
# ~ ax2.tick_params(axis='x', labelrotation = 90, labelsize=11)

# ~ ############ grafico 3 ###########
ax3.plot(nqnPM)
ax3.plot(media5, color="black")
ax3.plot(media6, color="black")
ax3.set_ylabel('[$m^{3}$/s]', fontsize=11)
ax3.set_xlim([pd.Timestamp('1980-01-01'), pd.Timestamp('2017-12-01')])
# ~ ax3.xaxis.set_tick_params(length=0)
ax3.xaxis.set_tick_params(labelsize = 0, labelcolor = 'white')
ax3.yaxis.set_tick_params(labelsize=11)
ax3.set_title('Neuquén', fontsize=11)
ax3.text(pd.Timestamp('1983-01-01'),100, 'CP = 2006-2009', fontsize=10)
ax3.tick_params(axis='x', labelrotation = 90, labelsize=11)

# ~ ############ grafico 4 ###########
ax4.plot(blobPM)
ax4.plot(media7, color="black")
ax4.plot(media8, color="black")
ax4.set_ylabel('[°c]', fontsize=11)
ax4.set_xlim([pd.Timestamp('1980-01-01'), pd.Timestamp('2017-12-01')])
ax4.xaxis.set_tick_params(labelsize=11)
ax4.yaxis.set_tick_params(labelsize=11)
ax4.set_title('Blob ', fontsize=11)
ax4.text(pd.Timestamp('1983-01-01'),0.5, 'CP = 1995', fontsize=10)
ax4.tick_params(axis='x', labelrotation = 90, labelsize=11)

# ~ ############ grafico 5 ###########
ax5.plot(pdoPM)
ax5.plot(media9, color="black")
ax5.plot(media10, color="black")
ax5.set_ylabel('[°c]', fontsize=11)
ax5.set_xlim([pd.Timestamp('1980-01-01'), pd.Timestamp('2017-12-01')])
ax5.xaxis.set_tick_params(labelsize=11)
ax5.yaxis.set_tick_params(labelsize=11)
ax5.set_title('PDO', fontsize=11)
ax5.text(pd.Timestamp('1983-01-01'),-1.7, 'CP = 1997', fontsize=10)
ax5.tick_params(axis='x', labelrotation = 90, labelsize=11)

# ~ ############ grafico 5 ###########
ax6.plot(aaoPM)
ax6.tick_params(axis='x', labelrotation = 90, labelsize=11)
params = np.polyfit(x, aaoPM.values, 1) # 1 order
function = np.poly1d(params)
ax6.plot(aaoPM.index, function(x), color='red')
params2 = np.polyfit(x2, aaopos.values, 1) # 1 order
function2 = np.poly1d(params2)
ax6.plot(aaopos.index, function2(x2), color='red')
ax6.set_ylabel('[]', fontsize=11)
ax6.set_title('AAO', fontsize=11)



fig.subplots_adjust(hspace=0.4,wspace=0.5)
plt.savefig('saltos2.png', dpi=600, bbox_inches="tight")
plt.show()



