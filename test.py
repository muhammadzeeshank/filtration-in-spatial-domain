import numpy as np
import cv2 as cv

# Part A


def Input_Mask():
    row = int(input("Enter the Number of rows: "))
    col = int(input("Enter the Number of Columns: "))
    mask = np.zeros((row, col))

    for i in range(row):
        for j in range(col):
            mask[i][j] = float(
                input("Enter the value of Mask at loc ( " + str(i) + ' , ' + str(j) + ' )'))
    return mask

# Part B


def padding(img, pad_size):
    pad_img = np.pad(img, ((pad_size, pad_size),
                     (pad_size, pad_size), (0, 0)), 'constant')
    return pad_img

# Part C


def filter(pad_img, img, mask):
    row = np.shape(img)[0]
    col = np.shape(img)[1]
    size = mask.shape[0]
    for y in range(row):
        for x in range(col):
            val = 0
            for i in range(size):
                for j in range(size):
                    val += pad_img[i + y][j + x] * mask[i][j]
            img[y][x] = val[0]
            # print(val[0])
    return img


def normalization(img):
    dims = np.shape(img)
    rows = dims[0]
    cols = dims[1]
    norm_img = np.zeros((rows, cols))
    norm_img = cv.normalize(img, norm_img, 0, 255, cv.NORM_MINMAX)
    return norm_img


mask = Input_Mask()
img = cv.imread("images/img1b.tif")
dims = np.shape(mask)
rows = dims[0]
padding_size = int(rows/2)
padded_img = padding(img, padding_size)
filtered_img = filter(padded_img, img, mask)
normalized_img = normalization(img)
print("Mask\n", mask)
print("Padding size : ", padding_size)
print("Original Image \n", img)
print("Padded Image \n", padded_img)
# Displaying masked and normalized images
cv.imshow('After applying filter', filtered_img)
cv.imshow('After applying normalization', normalized_img)
cv.waitKey(0)
