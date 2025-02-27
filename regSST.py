import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy as cart
from netCDF4 import Dataset
import numpy as np
import pandas as pd
import matplotlib.gridspec as gridspec
from shapely.geometry.polygon import LinearRing

SST = '/home/emi/Documents/vientohidro2/datos/corrRADvsSST_jas.nc'
H = '/home/emi/Documents/vientohidro2/datos/regRADvsH250_jas.nc'

archivo1 = Dataset(SST, mode='r')
sst= archivo1.variables['skt'][:]
lons_s = archivo1.variables['lon'][:]
lats_s = archivo1.variables['lat'][:]

archivo2 = Dataset(H, mode='r')
h = archivo2.variables['hgt'][:]
lons_h = archivo2.variables['lon'][:]
lats_h = archivo2.variables['lat'][:]

levels1 = [-3, -2,-1]
levels2 = [1, 2,3]

df = pd.read_json("/home/emi/Dropbox/DTEC/Parques/python/solares.json").T


lats_sol = []
lons_sol = []
caps = []
for iparque in df.index:
    lats_sol.append(df.loc[iparque]['Lat'][0])
    lons_sol.append(df.loc[iparque]['Lat'][1])
    caps.append(df.loc[iparque]['Potencia'])
    
# ~ lons_TSA = [-30, -30, 10, 10]
# ~ lats_TSA = [-20, 0, 0, -20]
# ~ ringTSA = LinearRing(list(zip(lons_TSA, lats_TSA)))

# ~ lons_TNA = [-57.5, -57.5, -15,-15]
# ~ lats_TNA = [5.5, 23, 23, 5.5]
# ~ ringTNA = LinearRing(list(zip(lons_TNA, lats_TNA)))

# ~ lons_12 = [-90, -90, -80, -80]
# ~ lats_12 = [-10, 0, 0, -10]
# ~ ring12 = LinearRing(list(zip(lons_12, lats_12)))

# ~ lons_34 = [-170, -170, -120, -120]
# ~ lats_34 = [-5, 5, 5, -5]
# ~ ring34 = LinearRing(list(zip(lons_34, lats_34)))

# ~ lons_blob = [-170, -170, -130, -130]
# ~ lats_blob = [-40, -30, -30, -40]
# ~ ringblob = LinearRing(list(zip(lons_blob, lats_blob)))


fig, ax = plt.subplots(nrows=1,ncols=1, subplot_kw={'projection': ccrs.PlateCarree(central_longitude=180)}, figsize=(8,8))

line_c1 = ax.contour(lons_h,lats_h,np.squeeze(h), transform = ccrs.PlateCarree(), colors='mediumblue', alpha = 0.5, linewidth = 0.6, levels=levels1, zorder=101)
line_c2 = ax.contour(lons_h,lats_h,np.squeeze(h), transform = ccrs.PlateCarree(), colors='red', alpha = 0.5, linewidth = 0.6, levels=levels2, zorder=101)
ax.set_extent([-180, 180, -90,20], crs=ccrs.PlateCarree())
ax.clabel(line_c1, inline=True, fontsize=10)
ax.clabel(line_c2, inline=True, fontsize=10)
cs1=ax.contourf(lons_s,lats_s,np.squeeze(sst), levels = [-1, -0.75, -0.5,-0.25, 0,0.25 ,0.5,0.75,1], transform = ccrs.PlateCarree(),cmap='RdYlBu_r')
ax.coastlines(resolution="10m",linewidth=1, color='black')
ax.add_feature(cart.feature.LAND, zorder=100, edgecolor='k')
ax.gridlines(linewidth = 0)
ax.plot(lons_sol, lats_sol, 'o', color='orange', ms="2", transform=ccrs.PlateCarree(), zorder=102)
# ~ ax.plot(-68.66, -31.38, 'o', color='orange', ms="2", transform=ccrs.PlateCarree(), zorder=102)
# ~ ax.add_geometries([ringTSA], ccrs.PlateCarree(), facecolor='none', edgecolor='black', linewidth=2)
# ~ ax.add_geometries([ringTNA], ccrs.PlateCarree(), facecolor='none', edgecolor='black', linewidth=2)
# ~ ax.add_geometries([ring12], ccrs.PlateCarree(), facecolor='none', edgecolor='black', linewidth=2)
# ~ ax.add_geometries([ring34], ccrs.PlateCarree(), facecolor='none', edgecolor='black', linewidth=2)
# ~ ax.add_geometries([ringblob], ccrs.PlateCarree(), facecolor='none', edgecolor='black', linewidth=2)

# ~ ax.text(-20+180, -10, 'TSA')
# ~ ax.text(-40+180, 12, 'TNA')
# ~ ax.text(-120+180, -18, 'Niño 1+2')
# ~ ax.text(-160+180, -15, 'Niño 3.4')
# ~ ax.text(-160+180, -50, 'Blob')



cbar = plt.colorbar(cs1,ax=ax, fraction=0.014, pad=0.04)
cbar.set_label('corr. coef. []', fontsize = 12)
cbar.ax.tick_params(labelsize=12) 

plt.savefig('SST.png',dpi = 600 ,bbox_inches="tight")
plt.show()
