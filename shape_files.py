import cartopy.io.shapereader as shpreader
import cartopy.crs as ccrs
import cartopy.feature as cf
from cartopy.feature import ShapelyFeature
from matplotlib import pyplot as plt
import geopandas as gpd
import pandas as pd

import geoplot as gplt
import geoplot.crs as gcrs
import lithium_data

df = lithium_data.get_lith_horizon('Woodbend Group')
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Long_NAD83, df.Lat_NAD83))

ax = gplt.webmap(gdf, projection=gcrs.WebMercator())
# gplt.pointplot(
#     gdf,
#     hue='Li_mg_L',
#     # scheme=scheme,
#     legend=True, legend_var='hue', cmap='rainbow',
#     ax=ax
# )


# # Read shape file
reader = shpreader.Reader("data/WCSBAtlasShp/fg1205_ln_ll.shp")

shape_feature = ShapelyFeature(reader.geometries(),
                                ccrs.LambertConformal(), facecolor='none')

ax.add_feature(shape_feature)

plt.show()


# plt.savefig("Africa-Highlight-Kenya.svg")
