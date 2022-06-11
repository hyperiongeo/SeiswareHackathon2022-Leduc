import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

import geoplot as gplt
import geoplot.crs as gcrs
import mapclassify as mc

import lithium_data


# for grp in ['Woodbend Group', 'Winterburn Group', 'Mannville Group', 'Swan Hills Formation']:
for grp in ['Woodbend Group']:

    df = lithium_data.get_lith_horizon(grp)
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Long_NAD83, df.Lat_NAD83))

    scheme = mc.Quantiles(gdf['Li_mg_L'], k=5)
    scheme = mc.UserDefined(gdf['Li_mg_L'], bins=[50, 100, 150])

    ax = gplt.webmap(gdf, projection=gcrs.WebMercator())
    gplt.pointplot(
        gdf,
        hue='Li_mg_L',
        scheme=scheme,
        legend=True, legend_var='hue', cmap='rainbow',
        ax=ax
    )
    plt.title(grp)
    plt.show()
