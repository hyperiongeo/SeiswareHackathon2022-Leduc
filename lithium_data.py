import geopandas as gpd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import geoplot as gplt
import geoplot.crs as gcrs

infile = r"data/Lithium_Content_Groundwater_Formation-Water_Alberta.txt"

df = pd.read_csv(infile, sep='\t', lineterminator='\r')
df = df.drop(['Site_ID', 'Reference', 'Pub_by', 'Report_No'], axis=1)
# df = df[len(df['UWI']) < 5]

df = df.replace("\n", "")
df = df.replace("<0.1", "0.")
df = df.replace("<0.01", "0.")
df = df.replace("<0.02", "0.")

df['Li_mg_L'] = df['Li_mg_L'].astype(float)
df['UWI'] = df['UWI'].astype(str)

new_row = []
for idx, rows in df.iterrows():
    val = rows['UWI']
    # print(val, len(val))
    # print(rows['UWI'], len(rows['UWI']))
    if len(val) == 20:
        val = val+"0"
    if len(val) == 14:
        val = "100/"+val+"/00"
    val = val.replace("/", "").replace("-", "")
    # print(val)
    new_row.append(val)

df['UWI'] = new_row

# print(df['Li_mg_L'].describe())

def get_lith_horizon(horizon_name='Woodbend Group'):
    df_out = df[df.Geo_Unit == horizon_name]
    # print(df_out.shape)
    return df_out
