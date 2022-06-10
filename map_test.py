import geopandas as gpd
import pandas as pd



infile = r"data/Lithium_Content_Groundwater_Formation-Water_Alberta.txt"

tmp = pd.read_csv(infile, sep='\t', lineterminator='\r')
tmp = tmp.drop(['Site_ID'])
print(tmp.head())

# data = gpd.read_file(infile)
