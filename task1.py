import numpy as np
import cv2
from tqdm import tqdm  # for progress bar


def constructMask():
    """
    : return: mask, size of mask
    """
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
    return mask, size


def padImage(img1, size):
    """
    : param img1: original image
    : param size: size of mask
    : return: padded image
    """
    # Padding image
    padsize = int(size/2)
    img = np.lib.pad(img1, ((padsize, padsize), (padsize, padsize)), mode='constant',
                     constant_values=(0, 0))
    return img


def applyFilter(img, img1, mask):
    """
    : param img: the padded image
    : param img1: the original image
    : return: convovled image with mask
    """
    # convolving mask with image
    rows, cols = img1.shape
    size = mask.shape[0]
    for y in tqdm(range(rows)):
        for x in range(cols):
            val = 0
            for i in range(size):
                for j in range(size):
                    val += img[i + y][j + x] * mask[i][j]
            img1[y][x] = val
    return img1


# **** main ***
# Reading image from drive
orig_img = cv2.imread('images/img1b.tif', 0)
mask, mask_size = constructMask()
pad_img = padImage(orig_img, mask_size)
final_img = applyFilter(pad_img, orig_img, mask)
cv2.imwrite('img1b.jpg', final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
