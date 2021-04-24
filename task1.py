import numpy as np
import cv2

# Taking size and value of mask from user
# Enforcing the user to enter size of mask only in odd number
while(True):
    size = int(input("Enter mask size: "))
    if (size % 2) != 0:
        break
    else:
        print("[-] ERROR. Please Enter odd number!")
value = float(input("Enter maske value: "))
mask = np.full([size, size], value)
# Reading image from drive
# img1 = cv2.imread('images/img_face.tif', 0)
img1 = np.full([size, size], value)
# Padding image
padsize = int(size/2)
img = np.lib.pad(img1, ((padsize, padsize), (padsize, padsize)), mode='constant',
                 constant_values=(0, 0))
rows, cols = img1.shape
for y in range(rows):
    for x in range(cols):
        val = 0
        for i in range(size):
            for j in range(size):
                val += img[i + y][j + x] * mask[i][j]
        img1[y][x] = val

print(mask)
print(img)
print(img1)
# cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
