import cv2 as cv
import numpy as np

img = np.zeros((400, 600, 1), dtype=np.uint8)
cv.imshow('image', img)
sub_img = np.zeros([100,150,1],dtype=np.uint8)
sub_img.fill(255)
cv.imshow('sub image', sub_img)

copy_img = img.copy()
copy_img[100:100+sub_img.shape[0], 100:100+sub_img.shape[1]] = sub_img
cv.imshow('merge image', copy_img)


k = cv.waitKey(0) & 0xFF
if k == ord('q'):
    cv.destroyAllWindows()