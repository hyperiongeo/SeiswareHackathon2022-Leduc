import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

import geoplot as gplt
import geoplot.crs as gcrs

import lithium_data

# infile = r"data/Lithium_Content_Groundwater_Formation-Water_Alberta.txt"


df_woodbend = lithium_data.get_lith_horizon('Woodbend Group')
gdf = gpd.GeoDataFrame(df_woodbend, geometry=gpd.points_from_xy(df_woodbend.Long_NAD83, df_woodbend.Lat_NAD83))
# data = gpd.read_file(infile)

# gdf.plot()


# gplt.pointplot(gdf)
# plt.show()

import mapclassify as mc
scheme = mc.Quantiles(gdf['Li_mg_L'], k=5)

# ax = gplt.webmap(gdf, projection=gcrs.WebMercator())
# gplt.pointplot(
#     gdf,
#     hue='Li_mg_L',
#     scheme=scheme,
#         legend=True, legend_var='hue',
#     ax=ax
# )
# # ax.legend()
# plt.show()
