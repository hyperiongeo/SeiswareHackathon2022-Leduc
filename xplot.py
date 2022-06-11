import os
import geopandas as gpd
import pandas as pd
import geoplot as gplt
import geoplot.crs as gcrs
import mapclassify as mc
import geoplot.crs as gcrs
import matplotlib.pyplot as plt

from petro_ninja import PetroNinja

import lithium_data

df_woodbend = lithium_data.get_lith_horizon('Woodbend Group')
gdf = gpd.GeoDataFrame(df_woodbend, geometry=gpd.points_from_xy(df_woodbend.Long_NAD83, df_woodbend.Lat_NAD83))




##################
# xplot


# fig, ax = plt.subplots()
# ax.scatter(gdf_merge['Li_mg_L'], gdf_merge['cumulative_water'], alpha=0.5)

# ax.set_xlabel('Lithium Concen', fontsize=15)
# ax.set_ylabel('Cum Water', fontsize=15)
# ax.set_title('Leduc')

# ax.grid(True)
# fig.tight_layout()

# plt.show()

#######
df_lith = lithium_data.get_lith()
df_lith = df_lith[df_lith['Li_mg_L'] > 0.1]
gdf = gpd.GeoDataFrame(df_lith, geometry=gpd.points_from_xy(df_lith.Long_NAD83, df_lith.Lat_NAD83))


fig, ax = plt.subplots()
ax.scatter(df_lith['Li_mg_L'], df_lith['Cat_An_Bal'], alpha=0.5)

ax.set_xlabel('Lithium Concen', fontsize=15)
ax.set_ylabel('Cat_An_Bal', fontsize=15)
ax.set_title('All')

ax.grid(True)
fig.tight_layout()

plt.show()
