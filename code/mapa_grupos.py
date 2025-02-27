import matplotlib.pyplot as plt
import cartopy.crs as crs
from cartopy.feature import ShapelyFeature
import cartopy.feature as cfeature
import numpy as np
from cartopy.io.shapereader import Reader
from cartopy.mpl.ticker import (LongitudeFormatter, LatitudeFormatter,
                                LatitudeLocator, LongitudeLocator)

                                      
a = np.load('../notebooks/resumen_merra_eolicos_2022.npy', allow_pickle = True).item()
print(a)
lat = a['lat']
lon = a['lon']
grupos = a['grupos']
print(grupos)
print(lat)
print(lon)

def main():

    fig = plt.figure(figsize=(5,5))
    ax = fig.add_subplot(1, 1, 1, projection=crs.PlateCarree())
    ax.set_extent([-75, -52, -20,-57], crs=crs.PlateCarree())
    ax.coastlines(resolution="10m",linewidth=0.7, color='black')
    ax.add_feature(cfeature.BORDERS)
    ax.add_feature(cfeature.OCEAN)
    ax.tick_params(labelsize=9)

    ax.set_yticks([-25, -35, -45, -55], crs=crs.PlateCarree())
    ax.set_xticks([-72, -65, -58], crs=crs.PlateCarree())
    scatter = ax.scatter(lon, lat, c=grupos,transform=crs.PlateCarree(),cmap = 'tab10')
    ax.plot(-62.659, -40.04, 'o', color='brown', ms="6", transform=crs.PlateCarree(), alpha=0.8)
    # ~ scatter = ax.scatter(lon, lat, c=grupos,transform=crs.PlateCarree(),cmap = 'hsv')

    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    legend = ax.legend(*scatter.legend_elements(num=8),bbox_to_anchor=(0.75, 0.45), loc=2,labelcolor = 'white', borderaxespad=0., fontsize=9, frameon=False,title="Groups")
    plt.setp(legend.get_title(), color='white')
    plt.savefig('mapa_grupos.jpg', dpi=300, bbox_inches="tight")
    # ~ plt.show()


if __name__ == '__main__':
    main()
    
plt.savefig('mapa_grupos.jpg',dpi=300, bbox_inches="tight")


