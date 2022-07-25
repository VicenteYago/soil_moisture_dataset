import pickle
from optram import *

with open('./inSitu_dfs_global_masked.pkl', 'rb') as f:
    inSitu_dfs_global = pickle.load(f)
    
cols = ['ndvi', 'W', 'SM5', 'sensor_name', 'utm_x', 'utm_y']
bands = ['R', 'G', 'B', 'NIR', 'SWIR']
data = []

for index_dt , row_n in zip(inSitu_dfs_global.index, range(len(inSitu_dfs_global))) : 
    row = dict.fromkeys(bands)
    for band in bands : 
        fp = S2_getIndex(BASE_DIR = './' + band +'/', date = index_dt.date())
        raster = rioxarray.open_rasterio(fp)
        val = raster.loc[dict(x=586115, y=3510185)].values
        row[band] = val[0]
    data.append(row)

for band in bands : 
    inSitu_dfs_global[band] = [row[band] for row in data]

validation = inSitu_dfs_global[bands+["ndvi", "W", "SM5"]]

with open('validation.pkl', 'wb') as handle:
    pickle.dump(validation, handle, protocol=pickle.HIGHEST_PROTOCOL)