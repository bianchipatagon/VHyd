import cartopy.crs as ccrs
from netCDF4 import Dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy.ma as ma

############# archivos verano

Hver = '/home/emi/Documents/vientohidro2/WIND ENERGY/VH2/data/VIENTOvsH_VER.nc'
OLRver = '/home/emi/Documents/vientohidro2/WIND ENERGY/VH2/data/VIENTOvsOLR_VER.nc'
Tver = '/home/emi/Documents/vientohidro2/WIND ENERGY/VH2/data/VvsT_ver.nc'
PPver = '/home/emi/Documents/vientohidro2/WIND ENERGY/VH2/data/VvsPP_ver.nc'
elevat = '/home/emi/Documents/vientohidro2/WIND ENERGY/VH2/data/elev.0.5-deg.nc'

archivo1 = Dataset(Hver, mode='r')
archivo2 = Dataset(Tver, mode ='r')
archivo3 = Dataset(PPver, mode ='r')
archivo4 = Dataset(OLRver, mode='r')
archivo5 = Dataset(elevat, mode ='r')

hgt_ver = archivo1.variables['hgt'][:]
sat_ver =  archivo2.variables['air'][:]
pp_ver = archivo3.variables['precip'][:]
olr_ver = archivo4.variables['ulwrf'][:]

elev = archivo5.variables['data'][:]
elev = ma.masked_where(elev < 1500, elev)

############# archivos invierno

Hinv = '/home/emi/Documents/vientohidro2/WIND ENERGY/VH2/data/VIENTOvsH_INV.nc'
OLRinv = '/home/emi/Documents/vientohidro2/WIND ENERGY/VH2/data/VIENTOvsOLR_INV.nc'
Tinv = '/home/emi/Documents/vientohidro2/WIND ENERGY/VH2/data/VIENTOvsT_INV.nc'
PPinv = '/home/emi/Documents/vientohidro2/WIND ENERGY/VH2/data/VvsPP_inv.nc'

archivo6 = Dataset(Hinv, mode='r')
archivo7 = Dataset(Tinv, mode ='r')
archivo8 = Dataset(PPinv, mode ='r')
archivo9 = Dataset(OLRinv, mode='r')

hgt_inv = archivo6.variables['hgt'][:]
sat_inv =  archivo7.variables['air'][:]
pp_inv = archivo8.variables['precip'][:]
olr_inv = archivo9.variables['ulwrf'][:]

lons_h = archivo1.variables['lon'][:]
lats_h = archivo1.variables['lat'][:]

lons_o = archivo4.variables['lon'][:]
lats_o = archivo4.variables['lat'][:]

lons_pp = archivo3.variables['lon'][:]
lats_pp = archivo3.variables['lat'][:]

lons_t = archivo2.variables['lon'][:]
lats_t = archivo2.variables['lat'][:]

lons_ele = archivo5.variables['lon'][:]
lats_ele = archivo5.variables['lat'][:]
lons_ele = lons_ele - 180

# ~ print(elev)

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

levels1 = [-50, -40, -30, -20, -10, -1]
levels2 = [5, 10]
fig, ((ax1, ax2, ax3),(ax4, ax5, ax6)) = plt.subplots(nrows=2,ncols=3, subplot_kw={'projection': ccrs.PlateCarree(central_longitude=180)}, figsize=(11,5.5))

######### mapa 1 ###########
ax1.set_extent([-90, -40, -10,-65], crs=ccrs.PlateCarree())
ax1.pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=100)
line_c1 = ax1.contour(lons_h,lats_h,np.squeeze(hgt_ver), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax1.contour(lons_h,lats_h,np.squeeze(hgt_ver), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs2=ax1.contourf(lons_t,lats_t,np.squeeze(sat_ver),levels = [-2.5,-2.25, -2,-1.75, -1.5, -1.25,-1,-0.75, -0.5,-0.25, 0,0.25, 0.5,0.75, 1,1.25, 1.5] ,transform = ccrs.PlateCarree(),cmap='RdYlBu_r')
ax1.coastlines(resolution="10m",linewidth=1, color='black')
ax1.gridlines(linewidth = 0)
ax1.set_title('w speed vs 925 mb \n geop. h. /TEMP')
ax1.clabel(line_c1,   colors=['black'], manual=False, inline=True, fmt=' {:.0f} '.format)
ax1.clabel(line_c2,   colors=['black'], manual=False, inline=True, fmt=' {:.0f} '.format)
ax1.plot(-71.88, -50.25, '^', color='black', ms="6", transform=ccrs.PlateCarree()) 
cbar2 = fig.colorbar(cs2, ax=ax1,fraction = 0.05)
cbar2.set_label('Temperature [°c]', fontsize = 14)
cbar2.ax.tick_params(labelsize=12) 

######### mapa 2 ###########
ax2.set_extent([-90, -40, -10,-65], crs=ccrs.PlateCarree())
ax2.pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=100)
line_c1 = ax2.contour(lons_h,lats_h,np.squeeze(hgt_ver), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax2.contour(lons_h,lats_h,np.squeeze(hgt_ver), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs2=ax2.contourf(lons_pp,lats_pp,np.squeeze(pp_ver),levels = [-2.5,-2.25, -2,-1.75, -1.5, -1.25,-1,-0.75, -0.5,-0.25, 0,0.25, 0.5,0.75, 1,1.25, 1.5, 1.75, 2, 2.25] ,transform = ccrs.PlateCarree(),cmap='PuOr')
ax2.coastlines(resolution="10m",linewidth=1, color='black')
ax2.gridlines(linewidth = 0)
ax2.set_title('w speed vs 925 mb \n geop. h. /Rainfall')
ax2.clabel(line_c1,   colors=['black'], manual=False, inline=True, fmt=' {:.0f} '.format)
ax2.clabel(line_c2,   colors=['black'], manual=False, inline=True, fmt=' {:.0f} '.format)
ax2.plot(-71.88, -50.25, '^', color='black', ms="6", transform=ccrs.PlateCarree()) 
cbar2 = fig.colorbar(cs2, ax=ax2,fraction = 0.05)
cbar2.set_label('rainfall [mm]', fontsize = 14)
cbar2.ax.tick_params(labelsize=12) 

######### mapa 3 ###########
ax3.set_extent([-90, -40, -10,-65], crs=ccrs.PlateCarree())
ax3.pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=100)
line_c1 = ax3.contour(lons_h,lats_h,np.squeeze(hgt_ver), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax3.contour(lons_h,lats_h,np.squeeze(hgt_ver), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs=ax3.contourf(lons_o,lats_o,np.squeeze(olr_ver),levels=[-15, -13, -11, -9, -7, -5, -3,-1, 1,3,5,7,9,11 ], transform = ccrs.PlateCarree(),cmap='binary_r')
ax3.coastlines(resolution="10m",linewidth=1, color='white')
ax3.gridlines(linewidth = 0)
ax3.plot(lons_s, lats_s, 'o', color='orange', ms="4", transform=ccrs.PlateCarree(), zorder=101)
ax3.plot(lons_w, lats_w, 'o', color='blue', ms="4", transform=ccrs.PlateCarree(), zorder=101)
ax3.set_title('w speed vs 925 mb \n geop. h. /OLR')
ax3.clabel(line_c1,   colors=['black'], manual=False, inline=True, fmt=' {:.0f} '.format)
ax3.clabel(line_c2,   colors=['black'], manual=False, inline=True, fmt=' {:.0f} '.format)
cbar2 = fig.colorbar(cs, ax=ax3,fraction = 0.05)
cbar2.set_label('OLR [W/$m^{2}$]', fontsize = 14)
cbar2.ax.tick_params(labelsize=12)

######### mapa 4 ###########
ax4.set_extent([-90, -40, -10,-65], crs=ccrs.PlateCarree())
ax4.pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=100)
line_c1 = ax4.contour(lons_h,lats_h,np.squeeze(hgt_inv), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax4.contour(lons_h,lats_h,np.squeeze(hgt_inv), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs2=ax4.contourf(lons_t,lats_t,np.squeeze(sat_inv),levels = [-2.5,-2.25, -2,-1.75, -1.5, -1.25,-1,-0.75, -0.5,-0.25, 0,0.25, 0.5,0.75, 1,1.25, 1.5, 1.75, 2, 2.25] ,transform = ccrs.PlateCarree(),cmap='RdYlBu_r')
ax4.coastlines(resolution="10m",linewidth=1, color='black')
ax4.gridlines(linewidth = 0)
#ax4.set_title('w. speed vs geop. h. 925 mb \n TEMP')
ax4.clabel(line_c1,   colors=['black'], manual=False, inline=True, fmt=' {:.0f} '.format)
ax4.clabel(line_c2,   colors=['black'], manual=False, inline=True, fmt=' {:.0f} '.format)
ax4.plot(-71.88, -50.25, '^', color='black', ms="6", transform=ccrs.PlateCarree()) 
cbar2 = fig.colorbar(cs2, ax=ax4,fraction = 0.05)
cbar2.set_label('Temperature [°c]', fontsize = 14)
cbar2.ax.tick_params(labelsize=12) 

######### mapa 5 ###########
ax5.set_extent([-90, -40, -10,-65], crs=ccrs.PlateCarree())
ax5.pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=100)
line_c1 = ax5.contour(lons_h,lats_h,np.squeeze(hgt_inv), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax5.contour(lons_h,lats_h,np.squeeze(hgt_inv), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs2=ax5.contourf(lons_pp,lats_pp,np.squeeze(pp_inv),levels = [-2.5,-2.25, -2,-1.75, -1.5, -1.25,-1,-0.75, -0.5,-0.25, 0,0.25, 0.5,0.75, 1,1.25, 1.5] ,transform = ccrs.PlateCarree(),cmap='PuOr')
ax5.coastlines(resolution="10m",linewidth=1, color='black')
ax5.gridlines(linewidth = 0)
#ax5.set_title('w. speed vs geop. h. 925 mb \n Rainfall')
ax5.clabel(line_c1,   colors=['black'], manual=False, inline=True, fmt=' {:.0f} '.format)
ax5.clabel(line_c2,   colors=['black'], manual=False, inline=True, fmt=' {:.0f} '.format)
ax5.plot(-71.88, -50.25, '^', color='black', ms="6", transform=ccrs.PlateCarree()) 
cbar2 = fig.colorbar(cs2, ax=ax5,fraction = 0.05)
cbar2.set_label('rainfall [mm]', fontsize = 14)
cbar2.ax.tick_params(labelsize=12)

######### mapa 6 ###########
ax6.set_extent([-90, -40, -10,-65], crs=ccrs.PlateCarree())
ax6.pcolormesh(lons_ele, lats_ele, np.squeeze(elev), vmin=1500, vmax=50000, cmap='Greys_r', alpha=0.8, zorder=100)
line_c1 = ax6.contour(lons_h,lats_h,np.squeeze(hgt_inv), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1)
line_c2 = ax6.contour(lons_h,lats_h,np.squeeze(hgt_inv), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2)
cs1=ax6.contourf(lons_o,lats_o,np.squeeze(olr_inv), levels = [-10,-9, -8,-7, -6,-5, -4,-3,-2,-1, 0,1, 2,3,4,5, 6,7,8], transform = ccrs.PlateCarree(),cmap='binary_r')
ax6.coastlines(resolution="10m",linewidth=1, color='white')
ax6.gridlines(linewidth = 0)
ax6.plot(lons_s, lats_s, 'o', color='orange', ms="4", transform=ccrs.PlateCarree(), zorder=101)
ax6.plot(lons_w, lats_w, 'o', color='blue', ms="4", transform=ccrs.PlateCarree(), zorder=101)
#ax6.set_title('w. speed vs geop. h. 925 mb \n OLR')
ax6.clabel(line_c1,   colors=['black'], manual=False, inline=True, fmt=' {:.0f} '.format)
ax6.clabel(line_c2,   colors=['black'], manual=False, inline=True, fmt=' {:.0f} '.format)
cbar1 = fig.colorbar(cs1, ax=ax6, fraction = 0.05)
cbar1.set_label('OLR [W/$m^{2}$]', fontsize = 14)
cbar1.ax.tick_params(labelsize=12) 

plt.figtext( 0.14, 0.25, 'winter', rotation = 'vertical', fontsize = 14)
plt.figtext( 0.14, 0.67, 'summer', rotation = 'vertical', fontsize = 14)
fig.subplots_adjust(hspace=0.1)

plt.savefig('reg_inv_ver2.png',dpi = 600 ,bbox_inches="tight")

plt.show()

