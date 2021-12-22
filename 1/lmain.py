from PIL import Image
import numpy as np

mtl_text = open("LE07_L2SP_199026_20020729_20200916_02_T1_MTL.txt", "r")

corners = ['CORNER_UL_LAT_PRODUCT', 'CORNER_UL_LON_PRODUCT', 'CORNER_UR_LAT_PRODUCT', 'CORNER_UR_LON_PRODUCT',
           'CORNER_LL_LAT_PRODUCT', 'CORNER_LL_LON_PRODUCT', 'CORNER_LR_LAT_PRODUCT', 'CORNER_LR_LON_PRODUCT']

coordinates = []
lines = mtl_text.readlines()
#
for line in lines:
    line = line.strip()
    if line[0:21] in corners:
        coordinates.append(float(line[24:]))
print(coordinates)
array_coord = np.array([coordinates[0::2], coordinates[1::2]])
print(array_coord)
coord1 = coordinates[0:2]
coord2 = coordinates[2:4]
coord3 = coordinates[4:6]
coord4 = coordinates[6:8]

print(coord1)
print(coord2)
print(coord3)
print(coord4)

delta_x = coord2[0] - coord4[0]
delta_y = coord4[1] - coord3[1]
print(delta_x, delta_y)




x, y = 48.85341, 2.3488


pixel_x = 8101
pixel_y = 7431
density_x = delta_x/pixel_x
density_y = delta_y/pixel_y


print(density_x, density_y)

centr_x = (coord4[0]-x) / density_x
centr_y = (coord4[1]-y) / density_y

print(centr_x)
print(centr_y)


image = Image.open('LE07_L2SP_199026_20020729_20200916_02_T1_SR_B3.TIF')
box = (3417, 2992, 5145, 4464)
image2 = image.crop(box)
print(image2)
image2.save('paris.TIF')