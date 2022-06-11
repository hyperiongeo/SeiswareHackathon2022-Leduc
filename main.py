"""


main

"""

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

uwi_param = {}

uwi_param['uwis'] = list(gdf['UWI'])
print('uwi_param', uwi_param)

ninja_prod = PetroNinja("wells", "production_summaries")
prod_well_data = ninja_prod.get_wells(uwi_param)
prod_data_df = pd.DataFrame.from_dict(prod_well_data)
prod_data_df = prod_data_df.rename(columns={"wellbore_uwi": "UWI"})
# gdf_prod = gpd.GeoDataFrame(prod_data_df, geometry=gpd.points_from_xy(prod_data_df.Long_NAD83, prod_data_df.Lat_NAD83))
# print(prod_data_df.head())
print("prod_data_df", prod_data_df.columns)
# for well in prod_well_data:
#     print(well)

print("# OF WELLS:", len(uwi_param['uwis']))
print("# OF WELLS:", len(prod_well_data))

# print(prod_well_data[-1].keys())
# prod_well_data.to_csv("data/leduc_prod.csv")



tmp = pd.concat([df_woodbend, prod_data_df], axis=0, ignore_index=True)
gdf_merge = gpd.GeoDataFrame(tmp, geometry=gpd.points_from_xy(tmp.Long_NAD83, tmp.Lat_NAD83))
gdf_merge['cumulative_water'] = gdf_merge['cumulative_water'].fillna(0)
gdf_merge['cumulative_water'] = gdf_merge['cumulative_water'].astype(float)
print(gdf_merge['cumulative_water'])

new_data = gdf_merge[gdf_merge['cumulative_water'] > 0]
gdf_merge = gpd.GeoDataFrame(new_data, geometry=gpd.points_from_xy(new_data.Long_NAD83, new_data.Lat_NAD83))
print(gdf_merge.head())
scheme = mc.EqualInterval(gdf_merge, k=6)

ax = gplt.webmap(gdf_merge, projection=gcrs.WebMercator())
gplt.pointplot(
    gdf_merge,
    hue='cumulative_water',
    scheme=scheme,
    legend=True, legend_var='hue',
    ax=ax
)
plt.show()
