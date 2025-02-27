import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from netCDF4 import Dataset
import numpy as np
import pandas as pd
import numpy.ma as ma

####### cargamos archivos AAO ##########
AAOh_ver = '/home/emi/Documents/vientohidro2/datos/AAOvsH_efm.nc'
AAOh_oto = '/home/emi/Documents/vientohidro2/datos/AAOvsH_amj.nc'
AAOh_inv = '/home/emi/Documents/vientohidro2/datos/AAOvsH_jas.nc'
AAOh_pri = '/home/emi/Documents/vientohidro2/datos/AAOvsH_ond.nc'

AAOpp_ver = '/home/emi/Documents/vientohidro2/datos/AAOvsPP_efm.nc'
AAOpp_oto = '/home/emi/Documents/vientohidro2/datos/AAOvsPP_amj.nc'
AAOpp_inv = '/home/emi/Documents/vientohidro2/datos/AAOvsPP_jas.nc'
AAOpp_pri = '/home/emi/Documents/vientohidro2/datos/AAOvsPP_ond.nc'

AAOt_ver = '/home/emi/Documents/vientohidro2/datos/AAOvsT_efm.nc'
AAOt_oto = '/home/emi/Documents/vientohidro2/datos/AAOvsT_amj.nc'
AAOt_inv = '/home/emi/Documents/vientohidro2/datos/AAOvsT_jas.nc'
AAOt_pri = '/home/emi/Documents/vientohidro2/datos/AAOvsT_ond.nc'

archivo1 = Dataset(AAOh_ver, mode='r')
archivo2 = Dataset(AAOh_oto, mode='r')
archivo3 = Dataset(AAOh_inv, mode='r')
archivo4 = Dataset(AAOh_pri, mode='r')

archivo5 = Dataset(AAOpp_ver, mode='r')
archivo6 = Dataset(AAOpp_oto, mode='r')
archivo7 = Dataset(AAOpp_inv, mode='r')
archivo8 = Dataset(AAOpp_pri, mode='r')

archivo9 = Dataset(AAOt_ver, mode='r')
archivo10 = Dataset(AAOt_oto, mode='r')
archivo11 = Dataset(AAOt_inv, mode='r')
archivo12 = Dataset(AAOt_pri, mode='r')

hgt_a_ver= archivo1.variables['hgt'][:]
hgt_a_oto= archivo2.variables['hgt'][:]
hgt_a_inv= archivo3.variables['hgt'][:]
hgt_a_pri= archivo4.variables['hgt'][:]

pp_a_ver= archivo5.variables['precip'][:]
pp_a_oto= archivo6.variables['precip'][:]
pp_a_inv= archivo7.variables['precip'][:]
pp_a_pri= archivo8.variables['precip'][:]

t_a_ver= archivo9.variables['air'][:]
t_a_oto= archivo10.variables['air'][:]
t_a_inv= archivo11.variables['air'][:]
t_a_pri= archivo12.variables['air'][:]

####### cargamos archivos SOI ##########

SOIh_ver = '/home/emi/Documents/vientohidro2/datos/SOIvsH_efm.nc'
SOIh_oto = '/home/emi/Documents/vientohidro2/datos/SOIvsH_amj.nc'
SOIh_inv = '/home/emi/Documents/vientohidro2/datos/SOIvsH_jas.nc'
SOIh_pri = '/home/emi/Documents/vientohidro2/datos/SOIvsH_ond.nc'

SOIpp_ver = '/home/emi/Documents/vientohidro2/datos/SOIvsPP_efm.nc'
SOIpp_oto = '/home/emi/Documents/vientohidro2/datos/SOIvsPP_amj.nc'
SOIpp_inv = '/home/emi/Documents/vientohidro2/datos/SOIvsPP_jas.nc'
SOIpp_pri = '/home/emi/Documents/vientohidro2/datos/SOIvsPP_ond.nc'

SOIt_ver = '/home/emi/Documents/vientohidro2/datos/SOIvsTefm.nc'
SOIt_oto = '/home/emi/Documents/vientohidro2/datos/SOIvsTamj.nc'
SOIt_inv = '/home/emi/Documents/vientohidro2/datos/SOIvsTjas.nc'
SOIt_pri = '/home/emi/Documents/vientohidro2/datos/SOIvsTond.nc'

archivo13 = Dataset(SOIh_ver, mode='r')
archivo14 = Dataset(SOIh_oto, mode='r')
archivo15 = Dataset(SOIh_inv, mode='r')
archivo16 = Dataset(SOIh_pri, mode='r')

archivo17 = Dataset(SOIpp_ver, mode='r')
archivo18 = Dataset(SOIpp_oto, mode='r')
archivo19 = Dataset(SOIpp_inv, mode='r')
archivo20 = Dataset(SOIpp_pri, mode='r')

archivo21 = Dataset(SOIt_ver, mode='r')
archivo22 = Dataset(SOIt_oto, mode='r')
archivo23 = Dataset(SOIt_inv, mode='r')
archivo24 = Dataset(SOIt_pri, mode='r')

hgt1_ver= archivo13.variables['hgt'][:]
hgt1_oto= archivo14.variables['hgt'][:]
hgt1_inv= archivo15.variables['hgt'][:]
hgt1_pri= archivo16.variables['hgt'][:]

pp1_ver= archivo17.variables['precip'][:]
pp1_oto= archivo18.variables['precip'][:]
pp1_inv= archivo19.variables['precip'][:]
pp1_pri= archivo20.variables['precip'][:]

olr_ver= archivo21.variables['air'][:]
olr_oto= archivo22.variables['air'][:]
olr_inv= archivo23.variables['air'][:]
olr_pri= archivo24.variables['air'][:]

####### cargamos archivos BLOB ##########
BLOBh_ver = '/home/emi/Documents/vientohidro2/datos/BLOBvsH_efm.nc'
BLOBh_oto = '/home/emi/Documents/vientohidro2/datos/BLOBvsH_amj.nc'
BLOBh_inv = '/home/emi/Documents/vientohidro2/datos/BLOBvsH_jas.nc'
BLOBh_pri = '/home/emi/Documents/vientohidro2/datos/BLOBvsH_ond.nc'

BLOBpp_ver = '/home/emi/Documents/vientohidro2/datos/BLOBvsPP_efm.nc'
BLOBpp_oto = '/home/emi/Documents/vientohidro2/datos/BLOBvsPP_amj.nc'
BLOBpp_inv = '/home/emi/Documents/vientohidro2/datos/BLOBvsPP_jas.nc'
BLOBpp_pri = '/home/emi/Documents/vientohidro2/datos/BLOBvsPP_ond.nc'

BLOBt_ver = '/home/emi/Documents/vientohidro2/datos/BLOBvsT_efm.nc'
BLOBt_oto = '/home/emi/Documents/vientohidro2/datos/BLOBvsT_amj.nc'
BLOBt_inv = '/home/emi/Documents/vientohidro2/datos/BLOBvsT_jas.nc'
BLOBt_pri = '/home/emi/Documents/vientohidro2/datos/BLOBvsT_ond.nc'

archivo25 = Dataset(BLOBh_ver, mode='r')
archivo26 = Dataset(BLOBh_oto, mode='r')
archivo27 = Dataset(BLOBh_inv, mode='r')
archivo28 = Dataset(BLOBh_pri, mode='r')

archivo29 = Dataset(BLOBpp_ver, mode='r')
archivo30 = Dataset(BLOBpp_oto, mode='r')
archivo31 = Dataset(BLOBpp_inv, mode='r')
archivo32 = Dataset(BLOBpp_pri, mode='r')

archivo33 = Dataset(BLOBt_ver, mode='r')
archivo34 = Dataset(BLOBt_oto, mode='r')
archivo35 = Dataset(BLOBt_inv, mode='r')
archivo36 = Dataset(BLOBt_pri, mode='r')

hgt_b_ver= archivo25.variables['hgt'][:]
hgt_b_oto= archivo26.variables['hgt'][:]
hgt_b_inv= archivo27.variables['hgt'][:]
hgt_b_pri= archivo28.variables['hgt'][:]

pp_b_ver= archivo29.variables['precip'][:]
pp_b_oto= archivo30.variables['precip'][:]
pp_b_inv= archivo31.variables['precip'][:]
pp_b_pri= archivo32.variables['precip'][:]

t_b_ver= archivo33.variables['air'][:]
t_b_oto= archivo34.variables['air'][:]
t_b_inv= archivo35.variables['air'][:]
t_b_pri= archivo36.variables['air'][:]

####### cargamos archivos PDO ##########
PDOh_ver = '/home/emi/Documents/vientohidro2/datos/PDOvsH_efm.nc'
PDOh_oto = '/home/emi/Documents/vientohidro2/datos/PDOvsH_amj.nc'
PDOh_inv = '/home/emi/Documents/vientohidro2/datos/PDOvsH_jas.nc'
PDOh_pri = '/home/emi/Documents/vientohidro2/datos/PDOvsH_ond.nc'

PDOpp_ver = '/home/emi/Documents/vientohidro2/datos/PDOvsPP_efm.nc'
PDOpp_oto = '/home/emi/Documents/vientohidro2/datos/PDOvsPP_amj.nc'
PDOpp_inv = '/home/emi/Documents/vientohidro2/datos/PDOvsPP_jas.nc'
PDOpp_pri = '/home/emi/Documents/vientohidro2/datos/PDOvsPP_ond.nc'

PDOt_ver = '/home/emi/Documents/vientohidro2/datos/PDOvsT_efm.nc'
PDOt_oto = '/home/emi/Documents/vientohidro2/datos/PDOvsT_amj.nc'
PDOt_inv = '/home/emi/Documents/vientohidro2/datos/PDOvsT_jas.nc'
PDOt_pri = '/home/emi/Documents/vientohidro2/datos/PDOvsT_ond.nc'

archivo37 = Dataset(PDOh_ver, mode='r')
archivo38 = Dataset(PDOh_oto, mode='r')
archivo39 = Dataset(PDOh_inv, mode='r')
archivo40 = Dataset(PDOh_pri, mode='r')

archivo41 = Dataset(PDOpp_ver, mode='r')
archivo42 = Dataset(PDOpp_oto, mode='r')
archivo43 = Dataset(PDOpp_inv, mode='r')
archivo44 = Dataset(PDOpp_pri, mode='r')

archivo45 = Dataset(PDOt_ver, mode='r')
archivo46 = Dataset(PDOt_oto, mode='r')
archivo47 = Dataset(PDOt_inv, mode='r')
archivo48 = Dataset(PDOt_pri, mode='r')

hgt_p_ver= archivo37.variables['hgt'][:]
hgt_p_oto= archivo38.variables['hgt'][:]
hgt_p_inv= archivo39.variables['hgt'][:]
hgt_p_pri= archivo40.variables['hgt'][:]

pp_p_ver= archivo41.variables['precip'][:]
pp_p_oto= archivo42.variables['precip'][:]
pp_p_inv= archivo43.variables['precip'][:]
pp_p_pri= archivo44.variables['precip'][:]

t_p_ver= archivo45.variables['air'][:]
t_p_oto= archivo46.variables['air'][:]
t_p_inv= archivo47.variables['air'][:]
t_p_pri= archivo48.variables['air'][:]

####### cargo DEM ##########
elevat = '/home/emi/Documents/vientohidro2/datos/elev.0.5-deg.nc'
archivo49 = Dataset(elevat, mode ='r')

#########

lons_h = archivo1.variables['lon'][:]
lats_h = archivo1.variables['lat'][:]

lons_pp = archivo5.variables['lon'][:]
lats_pp = archivo5.variables['lat'][:]

lons_t = archivo9.variables['lon'][:]
lats_t = archivo9.variables['lat'][:]

lons_olr = archivo21.variables['lon'][:]
lats_olr = archivo21.variables['lat'][:]

lons_ele = archivo49.variables['lon'][:]
lats_ele = archivo49.variables['lat'][:]
lons_ele = lons_ele - 180
elev = archivo49.variables['data'][:]
elev = ma.masked_where(elev < 1500, elev)

lats_hidro = [-38.53, -40.51, -50.25]
lons_hidro = [-69.4, -70.45, -71.88]

levels1 = [-35, -25, -15, -5]
# ~ levels2 = [0, 5, 10,15,20,25]
levels2 = [1, 5,10, 15,20, 25,30,35]

df = pd.read_json("/home/emi/Dropbox/DTEC/Parques/python/eolicos.json").T
lats_w = []
lons_w = []
cap = []
for iparque in df.index:
    lats_w.append(df.loc[iparque]['Lat'][0])
    lons_w.append(df.loc[iparque]['Lat'][1])
    cap.append(df.loc[iparque]['Potencia'])

fig, ax = plt.subplots(nrows=4,ncols=8, subplot_kw={'projection': ccrs.PlateCarree(central_longitude=180)}, figsize=(16,7))

######### AAO pp hgt #######

######### mapa 1 ###########
ax[0,0].set_extent([-90, -40, -10,-60], crs=ccrs.PlateCarree())
ax[0,0].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[0,0].contour(lons_h,lats_h,np.squeeze(hgt_a_ver), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[0,0].contour(lons_h,lats_h,np.squeeze(hgt_a_ver), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs1=ax[0,0].contourf(lons_pp,lats_pp,np.squeeze(pp_a_ver),levels =[-1.8,-1.5,-1.2,-0.9,-0.6,-0.3,0, 0.3, 0.6, 0.9, 1.2, 1.4], transform = ccrs.PlateCarree(),cmap='PuOr')
ax[0,0].coastlines(resolution="10m",linewidth=1, color='black')
ax[0,0].gridlines(linewidth = 0)
ax[0,0].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[0,0].set_title('AAO vs h.925\n mb / rainfall', fontsize = 14)
ax[0,0].clabel(line_c1)
ax[0,0].clabel(line_c2)
ax[0,0].plot(lons_w, lats_w, 'o', color='blue', ms="2", transform=ccrs.PlateCarree())

######### mapa 2 ###########
ax[1,0].set_extent([-90, -40, -10,-60], crs=ccrs.PlateCarree())
ax[1,0].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[1,0].contour(lons_h,lats_h,np.squeeze(hgt_a_oto), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[1,0].contour(lons_h,lats_h,np.squeeze(hgt_a_oto), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs1=ax[1,0].contourf(lons_pp,lats_pp,np.squeeze(pp_a_oto),levels =[-1.8,-1.5,-1.2,-0.9,-0.6,-0.3,0, 0.3, 0.6, 0.9, 1.2, 1.4], transform = ccrs.PlateCarree(),cmap='PuOr')
ax[1,0].coastlines(resolution="10m",linewidth=1, color='black')
ax[1,0].gridlines(linewidth = 0)
ax[1,0].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[1,0].clabel(line_c1)
ax[1,0].clabel(line_c2)
ax[1,0].plot(lons_w, lats_w, 'o', color='blue', ms="2", transform=ccrs.PlateCarree())

######### mapa 3 ###########
ax[2,0].set_extent([-90, -40, -10,-60], crs=ccrs.PlateCarree())
ax[2,0].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[2,0].contour(lons_h,lats_h,np.squeeze(hgt_a_inv), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[2,0].contour(lons_h,lats_h,np.squeeze(hgt_a_inv), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs1=ax[2,0].contourf(lons_pp,lats_pp,np.squeeze(pp_a_inv),levels = [-1.8,-1.5,-1.2,-0.9,-0.6,-0.3,0, 0.3, 0.6, 0.9, 1.2, 1.4], transform = ccrs.PlateCarree(),cmap='PuOr')
ax[2,0].coastlines(resolution="10m",linewidth=1, color='black')
ax[2,0].gridlines(linewidth = 0)
ax[2,0].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[2,0].clabel(line_c1)
ax[2,0].clabel(line_c2)
ax[2,0].plot(lons_w, lats_w, 'o', color='blue', ms="2", transform=ccrs.PlateCarree())

######### mapa 4 ###########
ax[3,0].set_extent([-90, -40, -10,-60], crs=ccrs.PlateCarree())
ax[3,0].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[3,0].contour(lons_h,lats_h,np.squeeze(hgt_a_pri), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[3,0].contour(lons_h,lats_h,np.squeeze(hgt_a_pri), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs1=ax[3,0].contourf(lons_pp,lats_pp,np.squeeze(pp_a_pri),levels =[-1.8,-1.5,-1.2,-0.9,-0.6,-0.3,0, 0.3, 0.6, 0.9, 1.2, 1.4], transform = ccrs.PlateCarree(),cmap='PuOr')
ax[3,0].coastlines(resolution="10m",linewidth=1, color='black')
ax[3,0].gridlines(linewidth = 0)
ax[3,0].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[3,0].clabel(line_c1)
ax[3,0].clabel(line_c2)
ax[3,0].plot(lons_w, lats_w, 'o', color='blue', ms="2", transform=ccrs.PlateCarree())

######### SOI pp hgt #######

######### mapa 9 ###########
ax[0,1].set_extent([-90, -40, -10,-60], crs=ccrs.PlateCarree())
ax[0,1].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[0,1].contour(lons_h,lats_h,np.squeeze(hgt1_ver), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[0,1].contour(lons_h,lats_h,np.squeeze(hgt1_ver), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs2=ax[0,1].contourf(lons_pp,lats_pp,np.squeeze(pp1_ver),levels =[-1.8,-1.5,-1.2,-0.9,-0.6,-0.3,0, 0.3, 0.6, 0.9, 1.2, 1.4], transform = ccrs.PlateCarree(),cmap='PuOr')
ax[0,1].coastlines(resolution="10m",linewidth=1, color='black')
ax[0,1].gridlines(linewidth = 0)
ax[0,1].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[0,1].set_title('SOI vs h.925\n mb / rainfall', fontsize = 14)
ax[0,1].clabel(line_c1)
ax[0,1].clabel(line_c2)
ax[0,1].plot(lons_w, lats_w, 'o', color='blue', ms="2", transform=ccrs.PlateCarree())

######### mapa 10 ###########
ax[1,1].set_extent([-90, -40, -10,-60], crs=ccrs.PlateCarree())
ax[1,1].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[1,1].contour(lons_h,lats_h,np.squeeze(hgt1_oto), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[1,1].contour(lons_h,lats_h,np.squeeze(hgt1_oto), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs2=ax[1,1].contourf(lons_pp,lats_pp,np.squeeze(pp1_oto),levels =[-1.8,-1.5,-1.2,-0.9,-0.6,-0.3,0, 0.3, 0.6, 0.9, 1.2, 1.4], transform = ccrs.PlateCarree(),cmap='PuOr')
ax[1,1].coastlines(resolution="10m",linewidth=1, color='black')
ax[1,1].gridlines(linewidth = 0)
ax[1,1].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[1,1].clabel(line_c1)
ax[1,1].clabel(line_c2)
ax[1,1].plot(lons_w, lats_w, 'o', color='blue', ms="2", transform=ccrs.PlateCarree())

######### mapa 11 ###########
ax[2,1].set_extent([-90, -40, -10,-60], crs=ccrs.PlateCarree())
ax[2,1].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[2,1].contour(lons_h,lats_h,np.squeeze(hgt1_inv), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[2,1].contour(lons_h,lats_h,np.squeeze(hgt1_inv), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs2=ax[2,1].contourf(lons_pp,lats_pp,np.squeeze(pp1_inv),levels =[-1.8,-1.5,-1.2,-0.9,-0.6,-0.3,0, 0.3, 0.6, 0.9, 1.2, 1.4], transform = ccrs.PlateCarree(),cmap='PuOr')
ax[2,1].coastlines(resolution="10m",linewidth=1, color='black')
ax[2,1].gridlines(linewidth = 0)
ax[2,1].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[2,1].clabel(line_c1)
ax[2,1].clabel(line_c2)
ax[2,1].plot(lons_w, lats_w, 'o', color='blue', ms="2", transform=ccrs.PlateCarree())

######### mapa 12 ###########
ax[3,1].set_extent([-90, -40, -10,-60], crs=ccrs.PlateCarree())
ax[3,1].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[3,1].contour(lons_h,lats_h,np.squeeze(hgt1_pri), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[3,1].contour(lons_h,lats_h,np.squeeze(hgt1_pri), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs2=ax[3,1].contourf(lons_pp,lats_pp,np.squeeze(pp1_pri),levels =[-1.8,-1.5,-1.2,-0.9,-0.6,-0.3,0, 0.3, 0.6, 0.9, 1.2, 1.4], transform = ccrs.PlateCarree(),cmap='PuOr')
ax[3,1].coastlines(resolution="10m",linewidth=1, color='black')
ax[3,1].gridlines(linewidth = 0)
ax[3,1].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[3,1].clabel(line_c1)
ax[3,1].clabel(line_c2)
ax[3,1].plot(lons_w, lats_w, 'o', color='blue', ms="2", transform=ccrs.PlateCarree())

######## BLOB pp hgt #######

######### mapa 17 ###########
ax[0,2].set_extent([-90, -40, -10,-60], crs=ccrs.PlateCarree())
ax[0,2].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[0,2].contour(lons_h,lats_h,np.squeeze(hgt_b_ver), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[0,2].contour(lons_h,lats_h,np.squeeze(hgt_b_ver), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs3=ax[0,2].contourf(lons_pp,lats_pp,np.squeeze(pp_b_ver),levels =[-3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5], transform = ccrs.PlateCarree(),cmap='PuOr')
ax[0,2].coastlines(resolution="10m",linewidth=1, color='black')
ax[0,2].gridlines(linewidth = 0)
ax[0,2].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[0,2].set_title('SB vs h.925\n mb / rainfall', fontsize = 14)
ax[0,2].clabel(line_c1)
ax[0,2].clabel(line_c2)
ax[0,2].plot(lons_w, lats_w, 'o', color='blue', ms="2", transform=ccrs.PlateCarree())

######### mapa 18 ###########
ax[1,2].set_extent([-90, -40, -10,-60], crs=ccrs.PlateCarree())
ax[1,2].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[1,2].contour(lons_h,lats_h,np.squeeze(hgt_b_oto), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[1,2].contour(lons_h,lats_h,np.squeeze(hgt_b_oto), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs3=ax[1,2].contourf(lons_pp,lats_pp,np.squeeze(pp_b_oto),levels =[-3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5], transform = ccrs.PlateCarree(),cmap='PuOr')
ax[1,2].coastlines(resolution="10m",linewidth=1, color='black')
ax[1,2].gridlines(linewidth = 0)
ax[1,2].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[1,2].clabel(line_c1)
ax[1,2].clabel(line_c2)
ax[1,2].plot(lons_w, lats_w, 'o', color='blue', ms="2", transform=ccrs.PlateCarree())

######### mapa 19 ###########
ax[2,2].set_extent([-90, -40, -10,-60], crs=ccrs.PlateCarree())
ax[2,2].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[2,2].contour(lons_h,lats_h,np.squeeze(hgt_b_inv), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[2,2].contour(lons_h,lats_h,np.squeeze(hgt_b_inv), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs3=ax[2,2].contourf(lons_pp,lats_pp,np.squeeze(pp_b_inv),levels =[-3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5], transform = ccrs.PlateCarree(),cmap='PuOr')
ax[2,2].coastlines(resolution="10m",linewidth=1, color='black')
ax[2,2].gridlines(linewidth = 0)
ax[2,2].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[2,2].clabel(line_c1)
ax[2,2].clabel(line_c2)
ax[2,2].plot(lons_w, lats_w, 'o', color='blue', ms="2", transform=ccrs.PlateCarree())

######### mapa 20 ###########
ax[3,2].set_extent([-90, -40, -10,-60], crs=ccrs.PlateCarree())
ax[3,2].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[3,2].contour(lons_h,lats_h,np.squeeze(hgt_b_pri), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[3,2].contour(lons_h,lats_h,np.squeeze(hgt_b_pri), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs3=ax[3,2].contourf(lons_pp,lats_pp,np.squeeze(pp_b_pri),levels =[-3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5], transform = ccrs.PlateCarree(),cmap='PuOr')
ax[3,2].coastlines(resolution="10m",linewidth=1, color='black')
ax[3,2].gridlines(linewidth = 0)
ax[3,2].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[3,2].clabel(line_c1)
ax[3,2].clabel(line_c2)
ax[3,2].plot(lons_w, lats_w, 'o', color='blue', ms="2", transform=ccrs.PlateCarree())

######## PDO pp hgt #######

######### mapa 17 ###########
ax[0,3].set_extent([-90, -40, -10,-60], crs=ccrs.PlateCarree())
ax[0,3].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[0,3].contour(lons_h,lats_h,np.squeeze(hgt_p_ver), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[0,3].contour(lons_h,lats_h,np.squeeze(hgt_p_ver), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs4=ax[0,3].contourf(lons_pp,lats_pp,np.squeeze(pp_p_ver),levels =[-1.8,-1.5,-1.2,-0.9,-0.6,-0.3,0, 0.3, 0.6, 0.9, 1.2, 1.4], transform = ccrs.PlateCarree(),cmap='PuOr')
ax[0,3].coastlines(resolution="10m",linewidth=1, color='black')
ax[0,3].gridlines(linewidth = 0)
ax[0,3].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[0,3].set_title('PDO vs h.925\n mb / rainfall', fontsize = 14)
ax[0,3].clabel(line_c1)
ax[0,3].clabel(line_c2)
ax[0,3].plot(lons_w, lats_w, 'o', color='blue', ms="2", transform=ccrs.PlateCarree())

######### mapa 18 ###########
ax[1,3].set_extent([-90, -40, -10,-60], crs=ccrs.PlateCarree())
ax[1,3].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[1,3].contour(lons_h,lats_h,np.squeeze(hgt_p_oto), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[1,3].contour(lons_h,lats_h,np.squeeze(hgt_p_oto), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs4=ax[1,3].contourf(lons_pp,lats_pp,np.squeeze(pp_p_oto),levels =[-1.8,-1.5,-1.2,-0.9,-0.6,-0.3,0, 0.3, 0.6, 0.9, 1.2, 1.4], transform = ccrs.PlateCarree(),cmap='PuOr')
ax[1,3].coastlines(resolution="10m",linewidth=1, color='black')
ax[1,3].gridlines(linewidth = 0)
ax[1,3].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[1,3].clabel(line_c1)
ax[1,3].clabel(line_c2)
ax[1,3].plot(lons_w, lats_w, 'o', color='blue', ms="2", transform=ccrs.PlateCarree())

######### mapa 19 ###########
ax[2,3].set_extent([-90, -40, -10,-60], crs=ccrs.PlateCarree())
ax[2,3].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[2,3].contour(lons_h,lats_h,np.squeeze(hgt_p_inv), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[2,3].contour(lons_h,lats_h,np.squeeze(hgt_p_inv), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs4=ax[2,3].contourf(lons_pp,lats_pp,np.squeeze(pp_p_inv),levels =[-1.8,-1.5,-1.2,-0.9,-0.6,-0.3,0, 0.3, 0.6, 0.9, 1.2, 1.4], transform = ccrs.PlateCarree(),cmap='PuOr')
ax[2,3].coastlines(resolution="10m",linewidth=1, color='black')
ax[2,3].gridlines(linewidth = 0)
ax[2,3].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[2,3].clabel(line_c1)
ax[2,3].clabel(line_c2)
ax[2,3].plot(lons_w, lats_w, 'o', color='blue', ms="2", transform=ccrs.PlateCarree())

######### mapa 20 ###########
ax[3,3].set_extent([-90, -40, -10,-60], crs=ccrs.PlateCarree())
ax[3,3].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[3,3].contour(lons_h,lats_h,np.squeeze(hgt_p_pri), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[3,3].contour(lons_h,lats_h,np.squeeze(hgt_p_pri), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs4=ax[3,3].contourf(lons_pp,lats_pp,np.squeeze(pp_p_pri),levels =[-1.8,-1.5,-1.2,-0.9,-0.6,-0.3,0, 0.3, 0.6, 0.9, 1.2, 1.4], transform = ccrs.PlateCarree(),cmap='PuOr')
ax[3,3].coastlines(resolution="10m",linewidth=1, color='black')
ax[3,3].gridlines(linewidth = 0)
ax[3,3].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[3,3].clabel(line_c1)
ax[3,3].clabel(line_c2)
ax[3,3].plot(lons_w, lats_w, 'o', color='blue', ms="2", transform=ccrs.PlateCarree())

# ~ cbar = plt.colorbar(cs1,ax=[ax[0,0], ax[1,0], ax[2,0], ax[3,0], ax[0,1], ax[1,1], ax[2,1], ax[3,1], ax[0,2], ax[1,2], ax[2,2], ax[3,2]], location= 'bottom', pad= 0.3, anchor=(0.5,-0.5))
cbar = plt.colorbar(cs1,ax=[ax[0,0], ax[1,0], ax[2,0], ax[3,0]], location= 'bottom', pad= 0.3, anchor=(0.5,-0.5), ticks=[-1, 0, 1])
cbar.ax.tick_params(labelsize=14) 
cbar = plt.colorbar(cs2,ax=[ax[0,1], ax[1,1], ax[2,1], ax[3,1]], location= 'bottom', pad= 0.3, anchor=(0.5,-0.5), ticks=[-1, 0, 1])
# ~ cbar.set_label('rainfall [mm]', fontsize = 14)
cbar.ax.tick_params(labelsize=14) 
cbar = plt.colorbar(cs3,ax=[ax[0,2], ax[1,2], ax[2,2], ax[3,2]], location= 'bottom', pad= 0.3, anchor=(0.5,-0.5), ticks=[-2, 0, 2])
cbar.ax.tick_params(labelsize=14) 
cbar = plt.colorbar(cs4,ax=[ax[0,3], ax[1,3], ax[2,3], ax[3,3]], location= 'bottom', pad= 0.3, anchor=(0.5,-0.5), ticks=[-1, 0, 1])
cbar.ax.tick_params(labelsize=14) 

######### AAO t hgt #######

######### mapa 5 ###########
ax[0,4].set_extent([-90, -40, -10,-60], crs=ccrs.PlateCarree())
ax[0,4].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[0,4].contour(lons_h,lats_h,np.squeeze(hgt_a_ver), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[0,4].contour(lons_h,lats_h,np.squeeze(hgt_a_ver), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs5=ax[0,4].contourf(lons_t,lats_t,np.squeeze(t_a_ver),levels =[-1.2,-1, -0.8, -0.6, -0.4, -0.2,0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4], transform = ccrs.PlateCarree(),cmap='RdYlBu_r')
ax[0,4].coastlines(resolution="10m",linewidth=1, color='black')
ax[0,4].gridlines(linewidth = 0)
ax[0,4].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[0,4].set_title('AAO vs h.925\n mb / TEMP', fontsize = 14)
ax[0,4].clabel(line_c1)
ax[0,4].clabel(line_c2)
ax[0,4].plot(lons_w, lats_w, 'o', color='blue', ms="2", transform=ccrs.PlateCarree())

######### mapa 6 ###########
ax[1,4].set_extent([-90, -40, -10,-60], crs=ccrs.PlateCarree())
ax[1,4].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[1,4].contour(lons_h,lats_h,np.squeeze(hgt_a_oto), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[1,4].contour(lons_h,lats_h,np.squeeze(hgt_a_oto), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs5=ax[1,4].contourf(lons_t,lats_t,np.squeeze(t_a_oto),levels =[-1.2,-1, -0.8, -0.6, -0.4, -0.2,0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4], transform = ccrs.PlateCarree(),cmap='RdYlBu_r')
ax[1,4].coastlines(resolution="10m",linewidth=1, color='black')
ax[1,4].gridlines(linewidth = 0)
ax[1,4].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[1,4].clabel(line_c1)
ax[1,4].clabel(line_c2)
ax[1,4].plot(lons_w, lats_w, 'o', color='blue', ms="2", transform=ccrs.PlateCarree())

######### mapa 7 ###########
ax[2,4].set_extent([-90, -40, -10,-60], crs=ccrs.PlateCarree())
ax[2,4].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[2,4].contour(lons_h,lats_h,np.squeeze(hgt_a_inv), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[2,4].contour(lons_h,lats_h,np.squeeze(hgt_a_inv), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs5=ax[2,4].contourf(lons_t,lats_t,np.squeeze(t_a_inv),levels =[-1.2,-1, -0.8, -0.6, -0.4, -0.2,0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4], transform = ccrs.PlateCarree(),cmap='RdYlBu_r')
ax[2,4].coastlines(resolution="10m",linewidth=1, color='black')
ax[2,4].gridlines(linewidth = 0)
ax[2,4].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[2,4].clabel(line_c1)
ax[2,4].clabel(line_c2)
ax[2,4].plot(lons_w, lats_w, 'o', color='blue', ms="2", transform=ccrs.PlateCarree())

######### mapa 8 ###########
ax[3,4].set_extent([-90, -40, -10,-60], crs=ccrs.PlateCarree())
ax[3,4].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[3,4].contour(lons_h,lats_h,np.squeeze(hgt_a_pri), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[3,4].contour(lons_h,lats_h,np.squeeze(hgt_a_pri), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs5=ax[3,4].contourf(lons_t,lats_t,np.squeeze(t_a_pri),levels =[-1.2,-1, -0.8, -0.6, -0.4, -0.2,0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4], transform = ccrs.PlateCarree(),cmap='RdYlBu_r')
ax[3,4].coastlines(resolution="10m",linewidth=1, color='black')
ax[3,4].gridlines(linewidth = 0)
ax[3,4].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[3,4].clabel(line_c1)
ax[3,4].clabel(line_c2)
ax[3,4].plot(lons_w, lats_w, 'o', color='blue', ms="2", transform=ccrs.PlateCarree())

######### SOI t hgt #######

######### mapa 13 ###########
ax[0,5].set_extent([-90, -40, -10,-60], crs=ccrs.PlateCarree())
ax[0,5].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[0,5].contour(lons_h,lats_h,np.squeeze(hgt1_ver), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[0,5].contour(lons_h,lats_h,np.squeeze(hgt1_ver), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs6=ax[0,5].contourf(lons_olr,lats_olr,np.squeeze(olr_ver),levels = [-1.2,-1, -0.8, -0.6, -0.4, -0.2,0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4], transform = ccrs.PlateCarree(),cmap='RdYlBu_r')
ax[0,5].coastlines(resolution="10m",linewidth=1, color='black')
ax[0,5].gridlines(linewidth = 0)
ax[0,5].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[0,5].set_title('SOI vs h.925\n mb / TEMP', fontsize = 14)
ax[0,5].clabel(line_c1)
ax[0,5].clabel(line_c2)
ax[0,5].plot(lons_w, lats_w, 'o', color='blue', ms="2", transform=ccrs.PlateCarree())

######### mapa 14 ###########
ax[1,5].set_extent([-90, -40, -10,-60], crs=ccrs.PlateCarree())
ax[1,5].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[1,5].contour(lons_h,lats_h,np.squeeze(hgt1_oto), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[1,5].contour(lons_h,lats_h,np.squeeze(hgt1_oto), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs6=ax[1,5].contourf(lons_olr,lats_olr,np.squeeze(olr_oto),levels = [-1.2,-1, -0.8, -0.6, -0.4, -0.2,0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4], transform = ccrs.PlateCarree(),cmap='RdYlBu_r')
ax[1,5].coastlines(resolution="10m",linewidth=1, color='black')
ax[1,5].gridlines(linewidth = 0)
ax[1,5].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[1,5].clabel(line_c1)
ax[1,5].clabel(line_c2)
ax[1,5].plot(lons_w, lats_w, 'o', color='blue', ms="2", transform=ccrs.PlateCarree())

######### mapa 15 ###########
ax[2,5].set_extent([-90, -40, -10,-60], crs=ccrs.PlateCarree())
ax[2,5].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[2,5].contour(lons_h,lats_h,np.squeeze(hgt1_inv), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[2,5].contour(lons_h,lats_h,np.squeeze(hgt1_inv), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs6=ax[2,5].contourf(lons_olr,lats_olr,np.squeeze(olr_inv),levels = [-1.2,-1, -0.8, -0.6, -0.4, -0.2,0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4], transform = ccrs.PlateCarree(),cmap='RdYlBu_r')
ax[2,5].coastlines(resolution="10m",linewidth=1, color='black')
ax[2,5].gridlines(linewidth = 0)
ax[2,5].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[2,5].clabel(line_c1)
ax[2,5].clabel(line_c2)
ax[2,5].plot(lons_w, lats_w, 'o', color='blue', ms="2", transform=ccrs.PlateCarree())

######### mapa 16 ###########
ax[3,5].set_extent([-90, -40, -10,-60], crs=ccrs.PlateCarree())
ax[3,5].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[3,5].contour(lons_h,lats_h,np.squeeze(hgt1_pri), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[3,5].contour(lons_h,lats_h,np.squeeze(hgt1_pri), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs6=ax[3,5].contourf(lons_olr,lats_olr,np.squeeze(olr_pri),levels = [-1.2,-1, -0.8, -0.6, -0.4, -0.2,0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4], transform = ccrs.PlateCarree(),cmap='RdYlBu_r')
ax[3,5].coastlines(resolution="10m",linewidth=1, color='black')
ax[3,5].gridlines(linewidth = 0)
ax[3,5].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[3,5].clabel(line_c1)
ax[3,5].clabel(line_c2)
ax[3,5].plot(lons_w, lats_w, 'o', color='blue', ms="2", transform=ccrs.PlateCarree())

######### BLOB t hgt #######

######### mapa 21 ###########
ax[0,6].set_extent([-90, -40, -10,-60], crs=ccrs.PlateCarree())
ax[0,6].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[0,6].contour(lons_h,lats_h,np.squeeze(hgt_b_ver), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[0,6].contour(lons_h,lats_h,np.squeeze(hgt_b_ver), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs7=ax[0,6].contourf(lons_t,lats_t,np.squeeze(t_b_ver),levels =[-3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3], transform = ccrs.PlateCarree(),cmap='RdYlBu_r')
ax[0,6].coastlines(resolution="10m",linewidth=1, color='black')
ax[0,6].gridlines(linewidth = 0)
ax[0,6].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[0,6].set_title('SB vs h.925\n mb / TEMP', fontsize = 14)
ax[0,6].clabel(line_c1)
ax[0,6].clabel(line_c2)
ax[0,6].plot(lons_w, lats_w, 'o', color='blue', ms="2", transform=ccrs.PlateCarree())

######### mapa 22 ###########
ax[1,6].set_extent([-90, -40, -10,-60], crs=ccrs.PlateCarree())
ax[1,6].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[1,6].contour(lons_h,lats_h,np.squeeze(hgt_b_oto), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[1,6].contour(lons_h,lats_h,np.squeeze(hgt_b_oto), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs7=ax[1,6].contourf(lons_t,lats_t,np.squeeze(t_b_oto),levels =[-3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3], transform = ccrs.PlateCarree(),cmap='RdYlBu_r')
ax[1,6].coastlines(resolution="10m",linewidth=1, color='black')
ax[1,6].gridlines(linewidth = 0)
ax[1,6].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[1,6].clabel(line_c1)
ax[1,6].clabel(line_c2)
ax[1,6].plot(lons_w, lats_w, 'o', color='blue', ms="2", transform=ccrs.PlateCarree())

######### mapa 23 ###########
ax[2,6].set_extent([-90, -40, -10,-60], crs=ccrs.PlateCarree())
ax[2,6].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[2,6].contour(lons_h,lats_h,np.squeeze(hgt_b_inv), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[2,6].contour(lons_h,lats_h,np.squeeze(hgt_b_inv), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs7=ax[2,6].contourf(lons_t,lats_t,np.squeeze(t_b_inv),levels =[-3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3], transform = ccrs.PlateCarree(),cmap='RdYlBu_r')
ax[2,6].coastlines(resolution="10m",linewidth=1, color='black')
ax[2,6].gridlines(linewidth = 0)
ax[2,6].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[2,6].clabel(line_c1)
ax[2,6].clabel(line_c2)
ax[2,6].plot(lons_w, lats_w, 'o', color='blue', ms="2", transform=ccrs.PlateCarree())

######### mapa 24 ###########
ax[3,6].set_extent([-90, -40, -10,-60], crs=ccrs.PlateCarree())
ax[3,6].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[3,6].contour(lons_h,lats_h,np.squeeze(hgt_b_pri), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[3,6].contour(lons_h,lats_h,np.squeeze(hgt_b_pri), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs7=ax[3,6].contourf(lons_t,lats_t,np.squeeze(t_b_pri),levels =[-3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3], transform = ccrs.PlateCarree(),cmap='RdYlBu_r')
ax[3,6].coastlines(resolution="10m",linewidth=1, color='black')
ax[3,6].gridlines(linewidth = 0)
ax[3,6].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[3,6].clabel(line_c1)
ax[3,6].clabel(line_c2)
ax[3,6].plot(lons_w, lats_w, 'o', color='blue', ms="2", transform=ccrs.PlateCarree())

######### PDO t hgt #######

######### mapa 21 ###########
ax[0,7].set_extent([-90, -40, -10,-60], crs=ccrs.PlateCarree())
ax[0,7].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[0,7].contour(lons_h,lats_h,np.squeeze(hgt_p_ver), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[0,7].contour(lons_h,lats_h,np.squeeze(hgt_p_ver), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs8=ax[0,7].contourf(lons_t,lats_t,np.squeeze(t_p_ver),levels =[-1.2,-1, -0.8, -0.6, -0.4, -0.2,0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4], transform = ccrs.PlateCarree(),cmap='RdYlBu_r')
ax[0,7].coastlines(resolution="10m",linewidth=1, color='black')
ax[0,7].gridlines(linewidth = 0)
ax[0,7].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[0,7].set_title('PDO vs h.925\n mb / TEMP', fontsize = 14)
ax[0,7].clabel(line_c1)
ax[0,7].clabel(line_c2)
ax[0,7].plot(lons_w, lats_w, 'o', color='blue', ms="2", transform=ccrs.PlateCarree())

######### mapa 22 ###########
ax[1,7].set_extent([-90, -40, -10,-60], crs=ccrs.PlateCarree())
ax[1,7].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[1,7].contour(lons_h,lats_h,np.squeeze(hgt_p_oto), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[1,7].contour(lons_h,lats_h,np.squeeze(hgt_p_oto), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs8=ax[1,7].contourf(lons_t,lats_t,np.squeeze(t_p_oto),levels =[-1.2,-1, -0.8, -0.6, -0.4, -0.2,0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4], transform = ccrs.PlateCarree(),cmap='RdYlBu_r')
ax[1,7].coastlines(resolution="10m",linewidth=1, color='black')
ax[1,7].gridlines(linewidth = 0)
ax[1,7].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[1,7].clabel(line_c1)
ax[1,7].clabel(line_c2)
ax[1,7].plot(lons_w, lats_w, 'o', color='blue', ms="2", transform=ccrs.PlateCarree())

######### mapa 23 ###########
ax[2,7].set_extent([-90, -40, -10,-60], crs=ccrs.PlateCarree())
ax[2,7].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[2,7].contour(lons_h,lats_h,np.squeeze(hgt_p_inv), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[2,7].contour(lons_h,lats_h,np.squeeze(hgt_p_inv), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs8=ax[2,7].contourf(lons_t,lats_t,np.squeeze(t_p_inv),levels =[-1.2,-1, -0.8, -0.6, -0.4, -0.2,0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4], transform = ccrs.PlateCarree(),cmap='RdYlBu_r')
ax[2,7].coastlines(resolution="10m",linewidth=1, color='black')
ax[2,7].gridlines(linewidth = 0)
ax[2,7].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[2,7].clabel(line_c1)
ax[2,7].clabel(line_c2)
ax[2,7].plot(lons_w, lats_w, 'o', color='blue', ms="2", transform=ccrs.PlateCarree())

######### mapa 24 ###########
ax[3,7].set_extent([-90, -40, -10,-60], crs=ccrs.PlateCarree())
ax[3,7].pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=101)
line_c1 = ax[3,7].contour(lons_h,lats_h,np.squeeze(hgt_p_pri), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax[3,7].contour(lons_h,lats_h,np.squeeze(hgt_p_pri), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs8=ax[3,7].contourf(lons_t,lats_t,np.squeeze(t_p_pri),levels =[-1.2,-1, -0.8, -0.6, -0.4, -0.2,0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4], transform = ccrs.PlateCarree(),cmap='RdYlBu_r')
ax[3,7].coastlines(resolution="10m",linewidth=1, color='black')
ax[3,7].gridlines(linewidth = 0)
ax[3,7].plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree())
ax[3,7].clabel(line_c1)
ax[3,7].clabel(line_c2)
ax[3,7].plot(lons_w, lats_w, 'o', color='blue', ms="2", transform=ccrs.PlateCarree())

# ~ cbar = plt.colorbar(cs2,ax=[ax[0,3], ax[1,3], ax[2,3], ax[3,3], ax[0,4], ax[1,4], ax[2,4], ax[3,4], ax[0,5], ax[1,5], ax[2,5], ax[3,5]], location= 'bottom', anchor=(0.5,-0.5))
cbar = plt.colorbar(cs5,ax=[ax[0,4], ax[1,4], ax[2,4], ax[3,4]], location= 'bottom', anchor=(0.5,-0.5), ticks=[-1, 0, 1])
cbar.ax.tick_params(labelsize=14) 
cbar = plt.colorbar(cs6,ax=[ax[0,5], ax[1,5], ax[2,5], ax[3,5]], location= 'bottom', anchor=(0.5,-0.5), ticks=[-1, 0, 1])
# ~ cbar.set_label('Temperature [°c]', fontsize = 14)
cbar.ax.tick_params(labelsize=14) 
cbar = plt.colorbar(cs7,ax=[ax[0,6], ax[1,6], ax[2,6], ax[3,6]], location= 'bottom', anchor=(0.5,-0.5), ticks=[-2, 0, 2])
cbar.ax.tick_params(labelsize=14) 
cbar = plt.colorbar(cs8,ax=[ax[0,7], ax[1,7], ax[2,7], ax[3,7]], location= 'bottom', anchor=(0.5,-0.5), ticks=[-1, 0, 1])
cbar.ax.tick_params(labelsize=14) 

fig.text(0.11, 0.75, 'summer', fontsize = 14, rotation = 'vertical')
fig.text(0.11, 0.56, 'fall', fontsize = 14, rotation = 'vertical')
fig.text(0.11, 0.35, 'winter', fontsize = 14, rotation = 'vertical')
fig.text(0.11, 0.15, 'spring', fontsize = 14, rotation = 'vertical')
fig.text(0.28, -0.004, 'Rainfall [mm]', fontsize = 14, rotation = 'horizontal')
fig.text(0.67, -0.004, 'Temperature [°c]', fontsize = 14, rotation = 'horizontal')


plt.subplots_adjust(wspace=0.04)
plt.subplots_adjust(hspace=0.03)
plt.savefig('reg_ind_q.png',dpi = 600 ,bbox_inches="tight")
# ~ plt.show()
