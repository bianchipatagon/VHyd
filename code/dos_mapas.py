import cartopy.crs as ccrs
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import matplotlib.pyplot as plt
import cartopy.feature as cfeature
from cartopy.feature import ShapelyFeature
from cartopy.io.shapereader import Reader
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from shapely.geometry.polygon import LinearRing
from matplotlib.patches import Rectangle
import pandas as pd
import geopandas as gpd

img = plt.imread('/home/emi/Documents/vientohidro2/imagenes/waves.png')
Argentina = gpd.read_file('/home/emi/Documents/vientohidro2/shapes/ARG_adm0.shp')
Chile = gpd.read_file('/home/emi/Documents/vientohidro2/shapes/CHL_adm0.shp')
Lagos = gpd.read_file('/home/emi/Documents/vientohidro2/shp/areas_de_aguas_continentales_perenne/areas_de_aguas_continentales_perenne.shp')
Lagosch = gpd.read_file('/home/emi/Documents/vientohidro2/shp/Masas_Lacustres/masas_lacustres.shp')
# ~ negro = gpd.read_file('/home/emi/Documents/vientohidro2/shapes/Cuenca_Negro_Rios_UTF8.shp')
negro = r'/home/emi/Documents/vientohidro2/shapes/Cuenca_Negro_Rios_UTF8.shp'
cruz = r'/home/emi/Documents/vientohidro2/shapes/Cuenca Santa Cruz Rios UTF8.shp'
# ~ cruz = gpd.read_file('/home/emi/Documents/vientohidro2/shapes/Cuenca Santa Cruz Rios UTF8.shp')
cuencas = gpd.read_file('/home/emi/Documents/vientohidro2/shapes/Cuencas.shp')

df = pd.read_json("/home/emi/Dropbox/DTEC/Parques/python/eolicos.json").T
lat = []
lon = []
cap = []
for iparque in df.index:
    lat.append(df.loc[iparque]['Lat'][0])
    lon.append(df.loc[iparque]['Lat'][1])
    cap.append(df.loc[iparque]['Potencia'])

df = pd.read_json("/home/emi/Dropbox/DTEC/Parques/python/solares.json").T


lats = []
lons = []
caps = []
for iparque in df.index:
    lats.append(df.loc[iparque]['Lat'][0])
    lons.append(df.loc[iparque]['Lat'][1])
    caps.append(df.loc[iparque]['Potencia'])

# ~ shp_arg = ShapelyFeature(Reader(Argentina).geometries(),
                                # ~ ccrs.PlateCarree(), facecolor='white')
# ~ shp_ch = ShapelyFeature(Reader(Chile).geometries(),
                                # ~ ccrs.PlateCarree(), facecolor='white')                                
# ~ shp_lag_arg = ShapelyFeature(Reader(Lagos).geometries(),
                                # ~ ccrs.PlateCarree(), facecolor='cornflowerblue')                       
# ~ shp_lag_ch = ShapelyFeature(Reader(Lagosch).geometries(),
                                # ~ ccrs.PlateCarree(), facecolor='cornflowerblue')
# ~ cuencas = ShapelyFeature(Reader(cuencas).geometries(),
                                # ~ ccrs.PlateCarree(), facecolor='goldenrod')
negro = ShapelyFeature(Reader(negro).geometries(),
                                ccrs.PlateCarree(), facecolor='none')
cruz = ShapelyFeature(Reader(cruz).geometries(),
                                ccrs.PlateCarree(), facecolor='none')
                                
lats_h = [-41.58, -41.35, -42,-41.5,-41.58]
lons_h = [-71.66,-71.51,-71.51, -71.53,-71.51]

lons_area = [-72.1, -72.1, -67.5, -67.5]
lats_area = [-41.75, -35.75, -35.75, -41.75]

lats_hidro = [-38.53, -40.51, -50.25]
lons_hidro = [-69.4, -70.45, -71.88]

ring = LinearRing(list(zip(lons_area, lats_area)))

def main():
    fig = plt.figure(figsize=(11.8, 8))

#### mapa 1 ####

    ax1 = fig.add_subplot(2, 2, 1,
                          projection=ccrs.PlateCarree())
    ax1.set_extent([-75, -52, -20,-57], crs=ccrs.PlateCarree())
    ax1.coastlines(resolution="10m",linewidth=0.7, color='black')
    ax1.add_feature(cfeature.BORDERS)
    ax1.add_feature(cfeature.OCEAN)
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax1.xaxis.set_major_formatter(lon_formatter)
    ax1.yaxis.set_major_formatter(lat_formatter)
    # ~ cuencas.loc[[0]].plot(ax=ax1, facecolor = 'goldenrod', alpha=0.6)
    # ~ cuencas.loc[[1],'geometry'].plot(ax=ax1, facecolor = 'goldenrod', alpha=0.6)
    # ~ cuencas.loc[[2],'geometry'].plot(ax=ax1, facecolor = 'goldenrod', alpha=0.6)
    # ~ cuencas.loc[[3],'geometry'].plot(ax=ax1, facecolor = 'goldenrod', alpha=0.6)
    # ~ cuencas.loc[[4],'geometry'].plot(ax=ax1, facecolor = 'goldenrod', alpha=0.6)
    # ~ cuencas.loc[[5],'geometry'].plot(ax=ax1, facecolor = 'goldenrod', alpha=0.6)
    # ~ cuencas.loc[[6],'geometry'].plot(ax=ax1, facecolor = 'goldenrod', alpha=0.6)
    ax1.add_feature(cruz,linewidth=0.2,edgecolor='cornflowerblue')
    # ~ cruz.plot(ax=ax1,linewidth=0.2,edgecolor='cornflowerblue')
    ax1.add_feature(negro,linewidth=0.2,edgecolor='cornflowerblue')
    # ~ negro.plot(ax=ax1,linewidth=0.2,edgecolor='cornflowerblue')
    ax1.set_yticks([-25, -35, -45, -55], crs=ccrs.PlateCarree())
    ax1.set_xticks([-72, -65, -58], crs=ccrs.PlateCarree())
    ax1.plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree(), label = 'flow')
    ax1.add_geometries([ring], ccrs.PlateCarree(), facecolor='none', edgecolor='black')
    ax1.tick_params(axis='both', labelsize=9)
    ax1.text(-69, -50, 'Santa \n Cruz', ha='right',fontsize=5)
    ax1.scatter(lon, lat, s= cap,
             alpha=0.5,  transform=ccrs.PlateCarree(), label = 'wind')
    ax1.scatter(lons, lats, s= caps,
             alpha=0.5,  transform=ccrs.PlateCarree(), label = 'solar')
    ax1.legend(bbox_to_anchor=(0.55, 0.92), loc=2, borderaxespad=0., fontsize=8, framealpha=1).get_frame().set_edgecolor("white")
    
#### mapa 2 ####
 
    ax2 = fig.add_subplot(2, 1, 1, projection=ccrs.PlateCarree())
    ax2.set_extent([-72.1, -67.5, -35.75,-41.75], crs=ccrs.PlateCarree())
    ax2.xaxis.set_major_formatter(lon_formatter)
    ax2.yaxis.set_major_formatter(lat_formatter)
    ax2.coastlines(resolution="10m",linewidth=0.7, color='black')
    ax2.add_feature(cfeature.OCEAN)
    # ~ ax2.add_feature(shp_arg,linewidth=0.7, edgecolor='black')
    Argentina.plot(ax=ax2,linewidth=0.7, edgecolor='black', facecolor='white')
    Chile.plot(ax=ax2,linewidth=0.7, edgecolor='black', facecolor='white')
    # ~ ax2.add_feature(shp_ch,linewidth=0.7, edgecolor='black')
    # ~ ax2.add_feature(cuencas,linewidth=0, edgecolor='white', facecolor = 'goldenrod', alpha=0.6)
    cuencas.plot(ax=ax2,linewidth=0, edgecolor='white', facecolor = 'goldenrod', alpha=0.6)
    # ~ ax2.add_feature(shp_lag_arg,linewidth=0)
    Lagos.plot(ax=ax2,linewidth=0, facecolor= 'cornflowerblue')
    # ~ ax2.add_feature(shp_lag_ch,linewidth=0)
    Lagosch.plot(ax=ax2,linewidth=0, facecolor= 'cornflowerblue')
    ax2.add_feature(negro,linewidth=0.2,edgecolor='cornflowerblue')
    # ~ negro.plot(ax=ax2,linewidth=0.2,edgecolor='cornflowerblue')
    ax2.plot(lons_hidro, lats_hidro, '^', color='black', ms="4", transform=ccrs.PlateCarree(), zorder=4)
    ax2.stock_img()
    imagebox = OffsetImage(img, zoom=.03)
    imagebox.image.axes = ax2
    ab1 = AnnotationBbox(imagebox, [-68.46, -38.55], pad=0, frameon=False)
    ab2 = AnnotationBbox(imagebox, [-68.58, -39.1], pad=0, frameon=False)
    ab3 = AnnotationBbox(imagebox, [-68.75, -39.26], pad=0, frameon=False)
    ab4 = AnnotationBbox(imagebox, [-69.98, -40], pad=0, frameon=False)
    ab5 = AnnotationBbox(imagebox, [-70, -40.18], pad=0, frameon=False)
    ab6 = AnnotationBbox(imagebox, [-70.75, -40.58], pad=0, frameon=False)
    ax2.add_artist(ab1)
    ax2.add_artist(ab2)
    ax2.add_artist(ab3)
    ax2.add_artist(ab4)
    ax2.add_artist(ab5)
    ax2.add_artist(ab6)
    ax2.text(-68.11, -38.35, '479 MW', ha='right',fontsize=6)
    ax2.text(-67.7, -39.1, '127 MW', ha='right',fontsize=6)
    ax2.text(-67.80, -39.36, '1200 MW', ha='right',fontsize=6)
    ax2.text(-69.13, -40, '261 MW', ha='right',fontsize=6)
    ax2.text(-69.05, -40.28, '1400 MW', ha='right',fontsize=6)
    ax2.text(-70.30, -40.38, '1050 MW', ha='right',fontsize=6)
    ax2.text(-69, -38.2, 'Neuquén', ha='right',fontsize=7.5)
    ax2.text(-70.2, -41, 'Limay', ha='right',fontsize=7.5)
    ax2.set_yticks([-36.5, -38.5,-40.5], crs=ccrs.PlateCarree())
    ax2.set_xticks([-71.5,-70, -68.5], crs=ccrs.PlateCarree())
    ax2.tick_params(axis='both', labelsize=9)
    
    l1 = plt.scatter([],[], s=25, edgecolors='black',facecolor='none')
    l2 = plt.scatter([],[], s=50, edgecolors='black',facecolor='none')
    l3 = plt.scatter([],[], s=100, edgecolors='black',facecolor='none')
    l4 = plt.scatter([],[], s=300, edgecolors='black',facecolor='none')
    labels = ["25 MW", "50 MW", "100 MW", "300 MW"]
    leg = plt.legend([l1, l2, l3, l4], labels, scatterpoints=1,  frameon=False, labelspacing=1, bbox_to_anchor=(-0.25, 0.5), fontsize=7)
    
    plt.savefig('dos_mapas.png', dpi=600, bbox_inches="tight")

    # ~ plt.show()

if __name__ == '__main__':
    main()


