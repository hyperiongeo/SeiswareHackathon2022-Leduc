
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

import geoplot as gplt
import geoplot.crs as gcrs

import cartopy.crs as ccrs
import numpy as np
import pyproj

import verde as vd

def clean_isopach():
    tmp = pd.read_csv("data/winterburn_structure.txt", delim_whitespace=True,
                       names=["longitude", "latitude", "elevation", "val1", 'val2'])
    # print(tmp.head())
    tmp = tmp.drop(['val1', 'val2'], axis=1)
    tmp['longitude'] = tmp['longitude']*-1
    print(tmp.describe())

    gdf = gpd.GeoDataFrame(tmp, geometry=gpd.points_from_xy(tmp.longitude, tmp.latitude))

    return gdf

def grid_isopach(gdf):

    # gdf = gdf[gdf['elevation'] > 0]
    # print(gdf.head())

    projection = pyproj.Proj(proj="merc", lat_ts=gdf.latitude.mean())
    # pyproj doesn't play well with Pandas so we need to convert to numpy arrays
    proj_coords = projection(gdf.longitude.values, gdf.latitude.values)
    print(proj_coords)

    # plt.figure(figsize=(7, 6))
    # plt.title("isopach")
    # # Plot the bathymetry data locations as black dots
    # plt.plot(proj_coords[0], proj_coords[1], ".k", markersize=0.5)
    # plt.xlabel("Easting (m)")
    # plt.ylabel("Northing (m)")
    # plt.gca().set_aspect("equal")
    # plt.tight_layout()
    # plt.show()

    # Now we can set up a gridder for the decimated data
    grd = vd.ScipyGridder(method="cubic").fit(proj_coords, gdf.elevation.values)
    print("Gridder used:", grd)

    spacing = 5 / 60

    # Get the grid region in geographic coordinates
    region = vd.get_region((gdf.longitude, gdf.latitude))
    print("Data region:", region)

    # The 'grid' method can still make a geographic grid if we pass in a projection
    # function that converts lon, lat into the easting, northing coordinates that
    # we used in 'fit'. This can be any function that takes lon, lat and returns x,
    # y. In our case, it'll be the 'projection' variable that we created above.
    # We'll also set the names of the grid dimensions and the name the data
    # variable in our grid (the default would be 'scalars', which isn't very
    # informative).
    grid = grd.grid(
        region=region,
        spacing=spacing,
        projection=projection,
        dims=["latitude", "longitude"],
        data_names="elevation",
    )
    print("Generated geographic grid:", grid)

    return proj_coords, grid

def plot_isopach(proj_coords, grid):
    # Cartopy requires setting the coordinate reference system (CRS) of the
    # original data through the transform argument. Their docs say to use
    # PlateCarree to represent geographic data.
    crs = ccrs.PlateCarree()

    plt.figure(figsize=(7, 6))
    # Make a Mercator map of our gridded bathymetry
    ax = plt.axes(projection=ccrs.Mercator())
    ax.set_title("Gridded elevation Using Scipy")
    # Plot the gridded bathymetry
    pc = grid.elevation.plot.pcolormesh(
        ax=ax, transform=crs, zorder=-1, add_colorbar=False,
        vmin=-3500, vmax=250,
        cmap='rainbow',
    )
    plt.colorbar(pc).set_label("meters ASL")
    # Plot the locations of the decimated data
    ax.plot(proj_coords[0], proj_coords[1], ".k", markersize=0.5, transform=crs)
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")

    plt.show()


    # if ax is None:
    #     ax = gplt.webmap(gdf, projection=gcrs.WebMercator())

    # gplt.pointplot(
    #     gdf,
    #     hue='elevation',
    #     # scheme=scheme,
    #     legend=True, legend_var='hue', cmap='rainbow',
    #     ax=ax
    # )
    # if plot:
    #     plt.show()


# df = clean_isopach()
# proj_coords, grid = grid_isopach(df)
# plot_isopach(proj_coords, grid)
