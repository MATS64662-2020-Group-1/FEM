# Import necessary libraries #
import numpy as np
import matplotlib.pyplot as plt
import skimage
import scipy
# tell me when done #
print('done')

img = plt.imread('Ti64_binary_V6.0.png')
print('microstrure is', img)

y = -1
for row in img:
    y = y + 1
    
    x = -1
    for coloumn in row:
        x = x + 1
        if img[y, x] == 1:
            img[y,x]=2
            
        elif img[y,x]== 0:
            img[y,x]=1 
            
print('new img array is:')
print(img)

# write out geom files
f = open('image.geom', 'w')
f.write("\
5 header\n\
grid a %d b %d c %d\n\
size x %d.0 y %d.0 z %d.0\n\
origin x 0.0 y 0.0 z 0.0\n\
homogenization 1\n\
microstructures %d\n"\
%( x, y, 1.0, x, y, 1.0, 2)
       )
# %(resolution,resolution,resolution, resolution,resolution,resolution,n_packets)

np.savetxt(f, img, fmt='%d')

f.close()