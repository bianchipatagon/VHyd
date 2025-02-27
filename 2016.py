import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from netCDF4 import Dataset
import numpy as np
import cartopy.feature as cfeatur
import cartopy as cart
import pandas as pd
import numpy.ma as ma


SST = '/home/emi/Documents/vientohidro2/datos/SST2016.nc'
H = '/home/emi/Documents/vientohidro2/datos/H9252016.nc'
VEL = '/home/emi/Documents/vientohidro2/datos/V9252016.nc'
T = '/home/emi/Documents/vientohidro2/datos/T2016.nc'
PP = '/home/emi/Documents/vientohidro2/datos/PP2016.nc'
OLR = '/home/emi/Documents/vientohidro2/datos/OLR2016.nc'
H250 = '/home/emi/Documents/vientohidro2/datos/H2502016.nc'
elevat = '/home/emi/Documents/vientohidro2/datos/elev.0.5-deg.nc'

archivo1 = Dataset(SST, mode='r')
archivo2 = Dataset(H, mode='r')
archivo3 = Dataset(VEL, mode='r')
archivo4 = Dataset(T, mode='r')
archivo5 = Dataset(PP, mode='r')
archivo6 = Dataset(OLR, mode='r')
archivo7 = Dataset(H250, mode='r')
archivo8 = Dataset(elevat, mode ='r')

sst = archivo1.variables['sst'][:]
hgt = archivo2.variables['hgt'][:]
wsp = archivo3.variables['wspd'][:]
temp = archivo4.variables['air'][:]
pp = archivo5.variables['precip'][:]
olr = archivo6.variables['ulwrf'][:]
hgt250 = archivo7.variables['hgt'][:]

lons_sst = archivo1.variables['lon'][:]
lats_sst = archivo1.variables['lat'][:]

lons_h = archivo2.variables['lon'][:]
lats_h = archivo2.variables['lat'][:]

lons_wsp = archivo3.variables['lon'][:]
lats_wsp = archivo3.variables['lat'][:]

lons_t = archivo4.variables['lon'][:]
lats_t = archivo4.variables['lat'][:]

lons_pp = archivo5.variables['lon'][:]
lats_pp = archivo5.variables['lat'][:]

lons_olr = archivo6.variables['lon'][:]
lats_olr = archivo6.variables['lat'][:]

lons_h250 = archivo2.variables['lon'][:]
lats_h250 = archivo2.variables['lat'][:]

lons_ele = archivo8.variables['lon'][:]
lats_ele = archivo8.variables['lat'][:]
lons_ele = lons_ele - 180
elev = archivo8.variables['data'][:]
elev = ma.masked_where(elev < 1500, elev)


df = pd.read_json("/home/emi/Dropbox/DTEC/Parques/python/eolicos.json").T
lats_w = []
lons_w = []
cap = []
for iparque in df.index:
    lats_w.append(df.loc[iparque]['Lat'][0])
    lons_w.append(df.loc[iparque]['Lat'][1])
    cap.append(df.loc[iparque]['Potencia'])

df = pd.read_json("/home/emi/Dropbox/DTEC/Parques/python/solares.json").T


lats_s = []
lons_s = []
caps = []
for iparque in df.index:
    lats_s.append(df.loc[iparque]['Lat'][0])
    lons_s.append(df.loc[iparque]['Lat'][1])
    caps.append(df.loc[iparque]['Potencia'])

lats_hidro = [-38.53, -40.51, -50.25]
lons_hidro = [-69.4, -70.45, -71.88]

levels1 = [-35, -25, -15, -5]
# ~ levels2 = [1, 5, 15, 25, 35]
levels2 = [1, 10, 20, 30, 40]

fig, ax = plt.subplots(nrows=3,ncols=2,subplot_kw={'projection': ccrs.PlateCarree(central_longitude=180)}, figsize=(18,9))
fig.delaxes(ax[2,1])

######### mapa 1 ###########
ax[0,0].set_extent([-300, -20, 5,-79], crs=ccrs.PlateCarree())
ax[0,0].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[0,0].contour(lons_h250,lats_h250,np.squeeze(hgt250), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1, zorder=101)
line_c2 = ax[0,0].contour(lons_h250,lats_h250,np.squeeze(hgt250), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2, zorder=101)
cs1=ax[0,0].contourf(lons_sst,lats_sst,np.squeeze(sst), levels = [-1.75,-1.5,-1.25, -1, -0.75, -0.5,-0.25, 0,0.25 ,0.5,0.75,1, 1.25, 1.5, 1.75], transform = ccrs.PlateCarree(),cmap='RdYlBu_r')
# ~ cs1=ax[0].contourf(lons_sst,lats_sst,np.squeeze(sst), transform = ccrs.PlateCarree(),cmap='RdYlBu_r')
ax[0,0].coastlines(resolution="10m",linewidth=1, color='black')
ax[0,0].add_feature(cart.feature.LAND, zorder=100, edgecolor='k')
ax[0,0].gridlines(linewidth = 0)
ax[0,0].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[0,0].set_title('a) SST + h250', fontsize = 18)
cbar = plt.colorbar(cs1,ax=ax[0,0], fraction=0.014, pad=0.04)
cbar.set_label('[°c]', fontsize = 18)
cbar.ax.tick_params(labelsize=16) 

######### mapa 2 ###########
ax[0,1].set_extent([-300, -20, 5,-79], crs=ccrs.PlateCarree())
ax[0,1].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=100)
line_c1 = ax[0,1].contour(lons_h,lats_h,np.squeeze(hgt), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[0,1].contour(lons_h,lats_h,np.squeeze(hgt), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs1=ax[0,1].contourf(lons_wsp,lats_wsp,np.squeeze(wsp),levels = [-3,-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5,3, 3.5,4],transform = ccrs.PlateCarree(),cmap='RdBu')
ax[0,1].coastlines(resolution="10m",linewidth=1, color='black')
ax[0,1].gridlines(linewidth = 0)
ax[0,1].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[0,1].plot(lons_w, lats_w, 'o', color='blue', ms="2", transform=ccrs.PlateCarree())
ax[0,1].clabel(line_c1)
ax[0,1].clabel(line_c2)
ax[0,1].set_title('b) w. speed + h925', fontsize = 18)
cbar = plt.colorbar(cs1,ax=ax[0,1], fraction=0.014, pad=0.04)
cbar.set_label('[m/s]', fontsize = 18)
cbar.ax.tick_params(labelsize=16) 

######### mapa 3 ###########
ax[1,0].set_extent([-300, -20, 5,-79], crs=ccrs.PlateCarree())
ax[1,0].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=100)
line_c1 = ax[1,0].contour(lons_h,lats_h,np.squeeze(hgt), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[1,0].contour(lons_h,lats_h,np.squeeze(hgt), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs1=ax[1,0].contourf(lons_t,lats_t,np.squeeze(temp),levels=[-3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5,2,2.5,3, 3.5, 4], transform = ccrs.PlateCarree(),cmap='RdYlBu_r')
ax[1,0].coastlines(resolution="10m",linewidth=1, color='black')
ax[1,0].gridlines(linewidth = 0)
ax[1,0].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[1,0].clabel(line_c1)
ax[1,0].clabel(line_c2)
ax[1,0].set_title('c) SAT + h925', fontsize = 18)
cbar = plt.colorbar(cs1,ax=ax[1,0], fraction=0.014, pad=0.04)
cbar.set_label('[°c]', fontsize = 18)
cbar.ax.tick_params(labelsize=16) 

######### mapa 4 ###########
ax[1,1].set_extent([-300, -20, 5,-79], crs=ccrs.PlateCarree())
ax[1,1].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=100)
line_c1 = ax[1,1].contour(lons_h,lats_h,np.squeeze(hgt), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[1,1].contour(lons_h,lats_h,np.squeeze(hgt), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs1=ax[1,1].contourf(lons_pp,lats_pp,np.squeeze(pp),levels = [-4.5, -4, -3.5, -3, -2.5, -2, -1.5,-1, -0.5, 0, 0.5, 1, 1.5,2, 2.5, 3, 3.5, 4,4.5, 5, 5.5, 6], transform = ccrs.PlateCarree(),cmap='PuOr')
ax[1,1].coastlines(resolution="10m",linewidth=1, color='black')
ax[1,1].gridlines(linewidth = 0)
ax[1,1].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[1,1].clabel(line_c1)
ax[1,1].clabel(line_c2)
ax[1,1].set_title('d) rainfall + h925', fontsize = 18)
cbar = plt.colorbar(cs1,ax=ax[1,1], fraction=0.014, pad=0.04)
cbar.set_label('[mm]', fontsize = 18)
cbar.ax.tick_params(labelsize=16) 

######### mapa 5 ###########
ax[2,0].set_extent([-300, -20, 5,-79], crs=ccrs.PlateCarree())
ax[2,0].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=100)
line_c1 = ax[2,0].contour(lons_h,lats_h,np.squeeze(hgt), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[2,0].contour(lons_h,lats_h,np.squeeze(hgt), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs1=ax[2,0].contourf(lons_olr,lats_olr,np.squeeze(olr),levels = [-32,-30, -28, -26, -22, -18, -14, -10, -6, -2, 2, 6, 10, 14, 18, 22, 26], transform = ccrs.PlateCarree(),cmap='binary_r')
ax[2,0].coastlines(resolution="10m",linewidth=1, color='white')
ax[2,0].gridlines(linewidth = 0)
ax[2,0].plot(lons_s, lats_s, 'o', color='orange', ms="2", transform=ccrs.PlateCarree(), zorder=101)
ax[2,0].clabel(line_c1)
ax[2,0].clabel(line_c2)
ax[2,0].set_title('e) OLR + h925', fontsize = 18)
cbar = plt.colorbar(cs1,ax=ax[2,0], fraction=0.014, pad=0.04)
cbar.set_label('[W/$m^{2}$]', fontsize = 18)
cbar.ax.tick_params(labelsize=16) 

plt.subplots_adjust(wspace=0.15)
plt.subplots_adjust(hspace=0.05)
plt.savefig('2016.png',dpi = 600 ,bbox_inches="tight")
plt.show()

