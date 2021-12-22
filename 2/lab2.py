import rasterio
import numpy
import matplotlib.pyplot as plt

with rasterio.open('BAND3.tif') as src:
    band_red = src.read(1)

with rasterio.open('BAND4.tif') as src:
    band_nir = src.read(1)

numpy.seterr(divide='ignore', invalid='ignore')

ndvi = (band_nir.astype(float) - band_red.astype(float)) / (band_nir + band_red)

kwargs = src.meta
kwargs.update(
    dtype=rasterio.float32,
    count=1)

with rasterio.open('ndvi.tif', 'w', **kwargs) as dst:
    dst.write_band(1, ndvi.astype(rasterio.float32))

plt.imsave("ndvi_cmap.png", ndvi, cmap=plt.cm.twilight)