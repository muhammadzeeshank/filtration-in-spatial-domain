import numpy as np
import cv2
from tqdm import tqdm  # for progress bar

# Taking size and value of mask from user
# Enforcing the user to enter size of mask only in odd number
while(True):
    size = int(input("Enter mask size(only odd number): "))
    if (size % 2) != 0:
        break
    else:
        print("[-] ERROR. Please Enter odd number!")
value = input("Enter maske value(fraction/float/int): ")
if '/' in value:
    num, den = value.split('/')
    value = float(num)/float(den)
else:
    value = float(value)

# filling mask of (size, size) with value
mask = np.full([size, size], value)

# Reading image from drive
img1 = cv2.imread('images/img1b.tif', 0)

# Padding image
padsize = int(size/2)
img = np.lib.pad(img1, ((padsize, padsize), (padsize, padsize)), mode='constant',
                 constant_values=(0, 0))
rows, cols = img1.shape

# convolving mask with image
for y in tqdm(range(rows)):
    for x in range(cols):
        val = 0
        for i in range(size):
            for j in range(size):
                val += img[i + y][j + x] * mask[i][j]
        img1[y][x] = val

cv2.imwrite('img1b.jpg', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
