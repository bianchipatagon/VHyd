import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from netCDF4 import Dataset
import numpy as np
import pandas as pd
import numpy.ma as ma

####### cargamos archivos SOI ##########

SOIh_ver = '/home/emi/Documents/vientohidro2/datos/SOIvsH_efm.nc'
SOIh_oto = '/home/emi/Documents/vientohidro2/datos/SOIvsH_amj.nc'
SOIh_inv = '/home/emi/Documents/vientohidro2/datos/SOIvsH_jas.nc'
SOIh_pri = '/home/emi/Documents/vientohidro2/datos/SOIvsH_ond.nc'

SOIolr_ver = '/home/emi/Documents/vientohidro2/datos/SOIvsOLR_efm.nc'
SOIolr_oto = '/home/emi/Documents/vientohidro2/datos/SOIvsOLR_amj.nc'
SOIolr_inv = '/home/emi/Documents/vientohidro2/datos/SOIvsOLR_jas.nc'
SOIolr_pri = '/home/emi/Documents/vientohidro2/datos/SOIvsOLR_ond.nc'

archivo1 = Dataset(SOIh_ver, mode='r')
archivo2 = Dataset(SOIh_oto, mode='r')
archivo3 = Dataset(SOIh_inv, mode='r')
archivo4 = Dataset(SOIh_pri, mode='r')

archivo5 = Dataset(SOIolr_ver, mode='r')
archivo6 = Dataset(SOIolr_oto, mode='r')
archivo7 = Dataset(SOIolr_inv, mode='r')
archivo8 = Dataset(SOIolr_pri, mode='r')

hgt1_ver= archivo1.variables['hgt'][:]
hgt1_oto= archivo2.variables['hgt'][:]
hgt1_inv= archivo3.variables['hgt'][:]
hgt1_pri= archivo4.variables['hgt'][:]

olr_s_ver= archivo5.variables['ulwrf'][:]
olr_s_oto= archivo6.variables['ulwrf'][:]
olr_s_inv= archivo7.variables['ulwrf'][:]
olr_s_pri= archivo8.variables['ulwrf'][:]


####### cargamos archivos BLOB ##########
BLOBh_ver = '/home/emi/Documents/vientohidro2/datos/BLOBvsH_efm.nc'
BLOBh_oto = '/home/emi/Documents/vientohidro2/datos/BLOBvsH_amj.nc'
BLOBh_inv = '/home/emi/Documents/vientohidro2/datos/BLOBvsH_jas.nc'
BLOBh_pri = '/home/emi/Documents/vientohidro2/datos/BLOBvsH_ond.nc'

BLOBolr_ver = '/home/emi/Documents/vientohidro2/datos/BLOBvsOLR_efm.nc'
BLOBolr_oto = '/home/emi/Documents/vientohidro2/datos/BLOBvsOLR_amj.nc'
BLOBolr_inv = '/home/emi/Documents/vientohidro2/datos/BLOBvsOLR_jas.nc'
BLOBolr_pri = '/home/emi/Documents/vientohidro2/datos/BLOBvsOLR_ond.nc'

archivo9 = Dataset(BLOBh_ver, mode='r')
archivo10 = Dataset(BLOBh_oto, mode='r')
archivo11 = Dataset(BLOBh_inv, mode='r')
archivo12 = Dataset(BLOBh_pri, mode='r')

archivo13 = Dataset(BLOBolr_ver, mode='r')
archivo14 = Dataset(BLOBolr_oto, mode='r')
archivo15 = Dataset(BLOBolr_inv, mode='r')
archivo16 = Dataset(BLOBolr_pri, mode='r')

hgt_b_ver= archivo9.variables['hgt'][:]
hgt_b_oto= archivo10.variables['hgt'][:]
hgt_b_inv= archivo11.variables['hgt'][:]
hgt_b_pri= archivo12.variables['hgt'][:]

olr_b_ver= archivo13.variables['ulwrf'][:]
olr_b_oto= archivo14.variables['ulwrf'][:]
olr_b_inv= archivo15.variables['ulwrf'][:]
olr_b_pri= archivo16.variables['ulwrf'][:]


####### cargamos archivos TSA ##########
TSAh_ver = '/home/emi/Documents/vientohidro2/datos/TSAvsH_efm.nc'
TSAh_oto = '/home/emi/Documents/vientohidro2/datos/TSAvsH_amj.nc'
TSAh_inv = '/home/emi/Documents/vientohidro2/datos/TSAvsH_jas.nc'
TSAh_pri = '/home/emi/Documents/vientohidro2/datos/TSAvsH_ond.nc'

TSAolr_ver = '/home/emi/Documents/vientohidro2/datos/TSAvsOLR_efm.nc'
TSAolr_oto = '/home/emi/Documents/vientohidro2/datos/TSAvsOLR_amj.nc'
TSAolr_inv = '/home/emi/Documents/vientohidro2/datos/TSAvsOLR_jas.nc'
TSAolr_pri = '/home/emi/Documents/vientohidro2/datos/TSAvsOLR_ond.nc'

archivo17 = Dataset(TSAh_ver, mode='r')
archivo18 = Dataset(TSAh_oto, mode='r')
archivo19 = Dataset(TSAh_inv, mode='r')
archivo20 = Dataset(TSAh_pri, mode='r')

archivo21 = Dataset(TSAolr_ver, mode='r')
archivo22 = Dataset(TSAolr_oto, mode='r')
archivo23 = Dataset(TSAolr_inv, mode='r')
archivo24 = Dataset(TSAolr_pri, mode='r')

hgt_t_ver= archivo17.variables['hgt'][:]
hgt_t_oto= archivo18.variables['hgt'][:]
hgt_t_inv= archivo19.variables['hgt'][:]
hgt_t_pri= archivo20.variables['hgt'][:]

olr_t_ver= archivo21.variables['ulwrf'][:]
olr_t_oto= archivo22.variables['ulwrf'][:]
olr_t_inv= archivo23.variables['ulwrf'][:]
olr_t_pri= archivo24.variables['ulwrf'][:]

####### cargamos archivos PDO ##########
PDOh_ver = '/home/emi/Documents/vientohidro2/datos/PDOvsH_efm.nc'
PDOh_oto = '/home/emi/Documents/vientohidro2/datos/PDOvsH_amj.nc'
PDOh_inv = '/home/emi/Documents/vientohidro2/datos/PDOvsH_jas.nc'
PDOh_pri = '/home/emi/Documents/vientohidro2/datos/PDOvsH_ond.nc'

PDOolr_ver = '/home/emi/Documents/vientohidro2/datos/PDOvsOLR_efm.nc'
PDOolr_oto = '/home/emi/Documents/vientohidro2/datos/PDOvsOLR_amj.nc'
PDOolr_inv = '/home/emi/Documents/vientohidro2/datos/PDOvsOLR_jas.nc'
PDOolr_pri = '/home/emi/Documents/vientohidro2/datos/PDOvsOLR_ond.nc'

archivo25 = Dataset(PDOh_ver, mode='r')
archivo26 = Dataset(PDOh_oto, mode='r')
archivo27 = Dataset(PDOh_inv, mode='r')
archivo28 = Dataset(PDOh_pri, mode='r')

archivo29 = Dataset(PDOolr_ver, mode='r')
archivo30 = Dataset(PDOolr_oto, mode='r')
archivo31 = Dataset(PDOolr_inv, mode='r')
archivo32 = Dataset(PDOolr_pri, mode='r')

hgt_p_ver= archivo25.variables['hgt'][:]
hgt_p_oto= archivo26.variables['hgt'][:]
hgt_p_inv= archivo27.variables['hgt'][:]
hgt_p_pri= archivo28.variables['hgt'][:]

olr_p_ver= archivo29.variables['ulwrf'][:]
olr_p_oto= archivo30.variables['ulwrf'][:]
olr_p_inv= archivo31.variables['ulwrf'][:]
olr_p_pri= archivo32.variables['ulwrf'][:]

####### cargo DEM ##########
elevat = '/home/emi/Documents/vientohidro2/datos/elev.0.5-deg.nc'
archivo33 = Dataset(elevat, mode ='r')


#########

lons_h = archivo1.variables['lon'][:]
lats_h = archivo1.variables['lat'][:]

lons_olr = archivo5.variables['lon'][:]
lats_olr = archivo5.variables['lat'][:]

lons_ele = archivo33.variables['lon'][:]
lats_ele = archivo33.variables['lat'][:]
lons_ele = lons_ele - 180
elev = archivo33.variables['data'][:]
elev = ma.masked_where(elev < 1500, elev)

df = pd.read_json("/home/emi/Dropbox/DTEC/Parques/python/solares.json").T

lats_s = []
lons_s = []
caps = []

for iparque in df.index:
    lats_s.append(df.loc[iparque]['Lat'][0])
    lons_s.append(df.loc[iparque]['Lat'][1])
    caps.append(df.loc[iparque]['Potencia'])

levels1 = [-35, -25, -15, -5]
levels2 = [1, 5,10, 15,20, 25,30,35]

# ~ levels2 = [0, 5, 10,15,20,25]
levels3 = [-16, -12, -8, -4, 0, 4, 8, 12, 16]

fig, ax = plt.subplots(nrows=4,ncols=4, subplot_kw={'projection': ccrs.PlateCarree(central_longitude=180)}, figsize=(8,7))

######### SOI olr hgt #######

######### mapa 1 ###########
ax[0,0].set_extent([-90, -40, -18,-60], crs=ccrs.PlateCarree())
ax[0,0].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[0,0].contour(lons_h,lats_h,np.squeeze(hgt1_ver), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[0,0].contour(lons_h,lats_h,np.squeeze(hgt1_ver), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs1=ax[0,0].contourf(lons_olr,lats_olr,np.squeeze(olr_s_ver),levels = [-5.5, -5,-4.5,-4,-3, -2, -1, 0, 1,2,3,4, 4.5, 5], transform = ccrs.PlateCarree(),cmap='binary_r')
ax[0,0].coastlines(resolution="10m",linewidth=1, color='black')
ax[0,0].gridlines(linewidth = 0)
ax[0,0].set_title('SOI vs hgt 925\n mb / OLR', fontsize = 14)
ax[0,0].clabel(line_c1)
ax[0,0].clabel(line_c2)
ax[0,0].plot(lons_s, lats_s, 'o', color='orange', ms="2", transform=ccrs.PlateCarree(), zorder=102)


######### mapa 2 ###########
ax[1,0].set_extent([-90, -40, -18,-60], crs=ccrs.PlateCarree())
ax[1,0].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[1,0].contour(lons_h,lats_h,np.squeeze(hgt1_oto), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[1,0].contour(lons_h,lats_h,np.squeeze(hgt1_oto), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs1=ax[1,0].contourf(lons_olr,lats_olr,np.squeeze(olr_s_oto),levels = [-5.5, -5,-4.5,-4,-3, -2, -1, 0, 1,2,3,4, 4.5, 5], transform = ccrs.PlateCarree(),cmap='binary_r')
ax[1,0].coastlines(resolution="10m",linewidth=1, color='black')
ax[1,0].gridlines(linewidth = 0)
ax[1,0].clabel(line_c1)
ax[1,0].clabel(line_c2)
ax[1,0].plot(lons_s, lats_s, 'o', color='orange', ms="2", transform=ccrs.PlateCarree(), zorder=102)


######### mapa 3 ###########
ax[2,0].set_extent([-90, -40, -18,-60], crs=ccrs.PlateCarree())
ax[2,0].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[2,0].contour(lons_h,lats_h,np.squeeze(hgt1_inv), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[2,0].contour(lons_h,lats_h,np.squeeze(hgt1_inv), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs1=ax[2,0].contourf(lons_olr,lats_olr,np.squeeze(olr_s_inv),levels = [-5.5, -5,-4.5,-4,-3, -2, -1, 0, 1,2,3,4, 4.5, 5], transform = ccrs.PlateCarree(),cmap='binary_r')
ax[2,0].coastlines(resolution="10m",linewidth=1, color='black')
ax[2,0].gridlines(linewidth = 0)
ax[2,0].clabel(line_c1)
ax[2,0].clabel(line_c2)
ax[2,0].plot(lons_s, lats_s, 'o', color='orange', ms="2", transform=ccrs.PlateCarree(), zorder=102)


######### mapa 4 ###########
ax[3,0].set_extent([-90, -40, -18,-60], crs=ccrs.PlateCarree())
ax[3,0].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[3,0].contour(lons_h,lats_h,np.squeeze(hgt1_pri), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[3,0].contour(lons_h,lats_h,np.squeeze(hgt1_pri), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs1=ax[3,0].contourf(lons_olr,lats_olr,np.squeeze(olr_s_pri),levels = [-5.5, -5,-4.5,-4,-3, -2, -1, 0, 1,2,3,4, 4.5, 5], transform = ccrs.PlateCarree(),cmap='binary_r')
ax[3,0].coastlines(resolution="10m",linewidth=1, color='black')
ax[3,0].gridlines(linewidth = 0)
ax[3,0].clabel(line_c1)
ax[3,0].clabel(line_c2)
ax[3,0].plot(lons_s, lats_s, 'o', color='orange', ms="2", transform=ccrs.PlateCarree(), zorder=102)

cbar = plt.colorbar(cs1,ax=[ax[0,0], ax[1,0], ax[2,0], ax[3,0]], location= 'bottom', pad= 0.1, anchor=(0.5,-0.5),ticks=[-4, 0, 4])
cbar.ax.tick_params(labelsize=14) 

######### blob olr hgt #######

######### mapa 9 ###########
ax[0,1].set_extent([-90, -40, -18,-60], crs=ccrs.PlateCarree())
ax[0,1].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[0,1].contour(lons_h,lats_h,np.squeeze(hgt_b_ver), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[0,1].contour(lons_h,lats_h,np.squeeze(hgt_b_ver), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs2=ax[0,1].contourf(lons_olr,lats_olr,np.squeeze(olr_b_ver),levels = levels3, transform = ccrs.PlateCarree(),cmap='binary_r')
ax[0,1].coastlines(resolution="10m",linewidth=1, color='black')
ax[0,1].gridlines(linewidth = 0)
ax[0,1].set_title('SB vs h.925\n mb / OLR', fontsize = 14)
ax[0,1].clabel(line_c1)
ax[0,1].clabel(line_c2)
ax[0,1].plot(lons_s, lats_s, 'o', color='orange', ms="2", transform=ccrs.PlateCarree(), zorder=102)

######### mapa 10 ###########
ax[1,1].set_extent([-90, -40, -18,-60], crs=ccrs.PlateCarree())
ax[1,1].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[1,1].contour(lons_h,lats_h,np.squeeze(hgt_b_oto), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[1,1].contour(lons_h,lats_h,np.squeeze(hgt_b_oto), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs2=ax[1,1].contourf(lons_olr,lats_olr,np.squeeze(olr_b_oto),levels = levels3, transform = ccrs.PlateCarree(),cmap='binary_r')
ax[1,1].coastlines(resolution="10m",linewidth=1, color='black')
ax[1,1].gridlines(linewidth = 0)
ax[1,1].clabel(line_c1)
ax[1,1].clabel(line_c2)
ax[1,1].plot(lons_s, lats_s, 'o', color='orange', ms="2", transform=ccrs.PlateCarree(), zorder=102)

######### mapa 11 ###########
ax[2,1].set_extent([-90, -40, -18,-60], crs=ccrs.PlateCarree())
ax[2,1].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[2,1].contour(lons_h,lats_h,np.squeeze(hgt_b_inv), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[2,1].contour(lons_h,lats_h,np.squeeze(hgt_b_inv), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs2=ax[2,1].contourf(lons_olr,lats_olr,np.squeeze(olr_b_inv),levels = levels3, transform = ccrs.PlateCarree(),cmap='binary_r')
ax[2,1].coastlines(resolution="10m",linewidth=1, color='black')
ax[2,1].gridlines(linewidth = 0)
ax[2,1].clabel(line_c1)
ax[2,1].clabel(line_c2)
ax[2,1].plot(lons_s, lats_s, 'o', color='orange', ms="2", transform=ccrs.PlateCarree(), zorder=102)

######### mapa 12 ###########
ax[3,1].set_extent([-90, -40, -18,-60], crs=ccrs.PlateCarree())
ax[3,1].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[3,1].contour(lons_h,lats_h,np.squeeze(hgt_b_pri), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[3,1].contour(lons_h,lats_h,np.squeeze(hgt_b_pri), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs2=ax[3,1].contourf(lons_olr,lats_olr,np.squeeze(olr_b_pri),levels = levels3, transform = ccrs.PlateCarree(),cmap='binary_r')
ax[3,1].coastlines(resolution="10m",linewidth=1, color='black')
ax[3,1].gridlines(linewidth = 0)
ax[3,1].clabel(line_c1)
ax[3,1].clabel(line_c2)
ax[3,1].plot(lons_s, lats_s, 'o', color='orange', ms="2", transform=ccrs.PlateCarree(), zorder=102)

cbar = plt.colorbar(cs2, ax=[ax[0,1], ax[1,1], ax[2,1], ax[3,1]], location= 'bottom', pad= 0.1, anchor=(0.5,-0.5),ticks=[-8, 0, 8])
# ~ cbar.set_label('OLR [W/m^2]', fontsize = 14)
cbar.ax.tick_params(labelsize=14) 

######## TSA olr hgt #######

######### mapa 17 ###########
ax[0,2].set_extent([-90, -40, -18,-60], crs=ccrs.PlateCarree())
ax[0,2].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[0,2].contour(lons_h,lats_h,np.squeeze(hgt_t_ver), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[0,2].contour(lons_h,lats_h,np.squeeze(hgt_t_ver), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs3=ax[0,2].contourf(lons_olr,lats_olr,np.squeeze(olr_t_ver),levels = levels3, transform = ccrs.PlateCarree(),cmap='binary_r')
ax[0,2].coastlines(resolution="10m",linewidth=1, color='black')
ax[0,2].gridlines(linewidth = 0)
ax[0,2].set_title('TSA vs h.925\n mb / OLR', fontsize = 14)
ax[0,2].clabel(line_c1)
ax[0,2].clabel(line_c2)
ax[0,2].plot(lons_s, lats_s, 'o', color='orange', ms="2", transform=ccrs.PlateCarree(), zorder=102)

######### mapa 18 ###########
ax[1,2].set_extent([-90, -40, -18,-60], crs=ccrs.PlateCarree())
ax[1,2].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[1,2].contour(lons_h,lats_h,np.squeeze(hgt_t_oto), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[1,2].contour(lons_h,lats_h,np.squeeze(hgt_t_oto), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs3=ax[1,2].contourf(lons_olr,lats_olr,np.squeeze(olr_t_oto),levels = levels3, transform = ccrs.PlateCarree(),cmap='binary_r')
ax[1,2].coastlines(resolution="10m",linewidth=1, color='black')
ax[1,2].gridlines(linewidth = 0)
ax[1,2].clabel(line_c1)
ax[1,2].clabel(line_c2)
ax[1,2].plot(lons_s, lats_s, 'o', color='orange', ms="2", transform=ccrs.PlateCarree(), zorder=102)

######### mapa 19 ###########
ax[2,2].set_extent([-90, -40, -18,-60], crs=ccrs.PlateCarree())
ax[2,2].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[2,2].contour(lons_h,lats_h,np.squeeze(hgt_t_inv), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[2,2].contour(lons_h,lats_h,np.squeeze(hgt_t_inv), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs3=ax[2,2].contourf(lons_olr,lats_olr,np.squeeze(olr_t_inv),levels = levels3, transform = ccrs.PlateCarree(),cmap='binary_r')
ax[2,2].coastlines(resolution="10m",linewidth=1, color='black')
ax[2,2].gridlines(linewidth = 0)
ax[2,2].clabel(line_c1)
ax[2,2].clabel(line_c2)
ax[2,2].plot(lons_s, lats_s, 'o', color='orange', ms="2", transform=ccrs.PlateCarree(), zorder=102)

######### mapa 20 ###########
ax[3,2].set_extent([-90, -40, -18,-60], crs=ccrs.PlateCarree())
ax[3,2].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[3,2].contour(lons_h,lats_h,np.squeeze(hgt_t_pri), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[3,2].contour(lons_h,lats_h,np.squeeze(hgt_t_pri), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs3=ax[3,2].contourf(lons_olr,lats_olr,np.squeeze(olr_t_pri),levels = levels3, transform = ccrs.PlateCarree(),cmap='binary_r')
ax[3,2].coastlines(resolution="10m",linewidth=1, color='black')
ax[3,2].gridlines(linewidth = 0)
ax[3,2].clabel(line_c1)
ax[3,2].clabel(line_c2)
ax[3,2].plot(lons_s, lats_s, 'o', color='orange', ms="2", transform=ccrs.PlateCarree(), zorder=102)

cbar = plt.colorbar(cs3,ax=[ax[0,2], ax[1,2], ax[2,2], ax[3,2]], location= 'bottom', pad= 0.1, anchor=(0.5,-0.5),ticks=[-8, 0, 8])
cbar.ax.tick_params(labelsize=14) 

######## PDO olr hgt #######

######### mapa 17 ###########
ax[0,3].set_extent([-90, -40, -18,-60], crs=ccrs.PlateCarree())
ax[0,3].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[0,3].contour(lons_h,lats_h,np.squeeze(hgt_p_ver), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[0,3].contour(lons_h,lats_h,np.squeeze(hgt_p_ver), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs3=ax[0,3].contourf(lons_olr,lats_olr,np.squeeze(olr_p_ver),levels = [-5.5, -5,-4.5,-4,-3, -2, -1, 0, 1,2,3,4, 4.5, 5], transform = ccrs.PlateCarree(),cmap='binary_r')
ax[0,3].coastlines(resolution="10m",linewidth=1, color='black')
ax[0,3].gridlines(linewidth = 0)
ax[0,3].set_title('PDO vs h.925\n mb / OLR', fontsize = 14)
ax[0,3].clabel(line_c1)
ax[0,3].clabel(line_c2)
ax[0,3].plot(lons_s, lats_s, 'o', color='orange', ms="2", transform=ccrs.PlateCarree(), zorder=102)

######### mapa 18 ###########
ax[1,3].set_extent([-90, -40, -18,-60], crs=ccrs.PlateCarree())
ax[1,3].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[1,3].contour(lons_h,lats_h,np.squeeze(hgt_p_oto), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[1,3].contour(lons_h,lats_h,np.squeeze(hgt_p_oto), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs3=ax[1,3].contourf(lons_olr,lats_olr,np.squeeze(olr_p_oto),levels = [-5.5, -5,-4.5,-4,-3, -2, -1, 0, 1,2,3,4, 4.5, 5], transform = ccrs.PlateCarree(),cmap='binary_r')
ax[1,3].coastlines(resolution="10m",linewidth=1, color='black')
ax[1,3].gridlines(linewidth = 0)
ax[1,3].clabel(line_c1)
ax[1,3].clabel(line_c2)
ax[1,3].plot(lons_s, lats_s, 'o', color='orange', ms="2", transform=ccrs.PlateCarree(), zorder=102)

######### mapa 19 ###########
ax[2,3].set_extent([-90, -40, -18,-60], crs=ccrs.PlateCarree())
ax[2,3].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[2,3].contour(lons_h,lats_h,np.squeeze(hgt_p_inv), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[2,3].contour(lons_h,lats_h,np.squeeze(hgt_p_inv), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs3=ax[2,3].contourf(lons_olr,lats_olr,np.squeeze(olr_p_inv),levels = [-5.5, -5,-4.5,-4,-3, -2, -1, 0, 1,2,3,4, 4.5, 5], transform = ccrs.PlateCarree(),cmap='binary_r')
ax[2,3].coastlines(resolution="10m",linewidth=1, color='black')
ax[2,3].gridlines(linewidth = 0)
ax[2,3].clabel(line_c1)
ax[2,3].clabel(line_c2)
ax[2,3].plot(lons_s, lats_s, 'o', color='orange', ms="2", transform=ccrs.PlateCarree(), zorder=102)

######### mapa 20 ###########
ax[3,3].set_extent([-90, -40, -18,-60], crs=ccrs.PlateCarree())
ax[3,3].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[3,3].contour(lons_h,lats_h,np.squeeze(hgt_p_pri), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[3,3].contour(lons_h,lats_h,np.squeeze(hgt_p_pri), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs3=ax[3,3].contourf(lons_olr,lats_olr,np.squeeze(olr_p_pri),levels = [-5.5, -5,-4.5,-4,-3, -2, -1, 0, 1,2,3,4, 4.5, 5], transform = ccrs.PlateCarree(),cmap='binary_r')
ax[3,3].coastlines(resolution="10m",linewidth=1, color='black')
ax[3,3].gridlines(linewidth = 0)
ax[3,3].clabel(line_c1)
ax[3,3].clabel(line_c2)
ax[3,3].plot(lons_s, lats_s, 'o', color='orange', ms="2", transform=ccrs.PlateCarree(), zorder=102)

cbar = plt.colorbar(cs3,ax=[ax[0,3], ax[1,3], ax[2,3], ax[3,3]], location= 'bottom', pad= 0.1, anchor=(0.5,-0.5),ticks=[-4, 0, 4])
cbar.ax.tick_params(labelsize=14) 


fig.text(0.09, 0.75, 'summer', fontsize = 14, rotation = 'vertical')
fig.text(0.09, 0.56, 'fall', fontsize = 14, rotation = 'vertical')
fig.text(0.09, 0.35, 'winter', fontsize = 14, rotation = 'vertical')
fig.text(0.09, 0.15, 'spring', fontsize = 14, rotation = 'vertical')
fig.text(0.45, -0.004, 'OLR [W/m^2]', fontsize = 14, rotation = 'horizontal')

plt.subplots_adjust(wspace=0.03)
plt.subplots_adjust(hspace=0.03)

plt.savefig('reg_ind_olr.png',dpi = 600 ,bbox_inches="tight")
# ~ plt.show()


