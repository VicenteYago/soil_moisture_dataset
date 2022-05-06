# soil_moisture_dataset
Based on OPTRAM model for [Walnut Gulch Watershed area](https://github.com/VicenteYago/OPTRAM).

Highlights: 
- 1 year of sentinel2 imagery (2019)
- 8 bands: 
 - optical: R,G,B
 - IR: NIR, SWIR
 - mask: SCL
 - humidity normalized: W
 - humidty estimated: THETA  

W and THETA bands are estimated based on the Optical Trapezoidal Model (OPTRAM) as described by [sadegui et al 2017](https://www.sciencedirect.com/science/article/abs/pii/S0034425717302493).

```{bash}
858M	./dataset_v0/G/masked
1,3G	./dataset_v0/G
858M	./dataset_v0/NDVI/masked
1,2G	./dataset_v0/NDVI
858M	./dataset_v0/SWIR/masked
1,3G	./dataset_v0/SWIR
858M	./dataset_v0/W/masked
1,7G	./dataset_v0/W
8,0K	./dataset_v0/.ipynb_checkpoints
858M	./dataset_v0/B/masked
1,3G	./dataset_v0/B
1,7G	./dataset_v0/THETA/masked
3,4G	./dataset_v0/THETA
858M	./dataset_v0/R/masked
1,3G	./dataset_v0/R
858M	./dataset_v0/NIR/masked
1,3G	./dataset_v0/NIR
858M	./dataset_v0/SCL
14G	./dataset_v0/
```
