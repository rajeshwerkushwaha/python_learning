import cv2 as cv
import numpy as np


pt1 = []
width,height = 250,350

img = cv.imread('cards.jpg')
clone = img.copy()


def mouse_click(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        pt1.append([x,y])
        if len(pt1)>1:
            cv.line(img, tuple(pt1[-2]), tuple(pt1[-1]), (0,255,0), 2)
            cv.imshow('Cards', img)

def crop_img(pt1):
    # pt1 = np.float32([[564,63], [721,52], [788,242], [614,254]])
    pt1 = np.float32(pt1[:-1])

    # pt2 = np.float32([[0,0], [0,height], [width,height], [width,0]])
    pt2 = np.float32([[0,0], [width,0], [width,height], [0,height]])
    matrix = cv.getPerspectiveTransform(pt1, pt2)
    imgOut = cv.warpPerspective(img, matrix, (width,height))
    cv.imshow('Crop Card', imgOut)
    pt1 = []
    return pt1


cv.imshow('Cards', img)
cv.setMouseCallback('Cards', mouse_click);


print("##### Program to get the crop image #####")
print("Press 'r' to reset image")
print("Press 'c' to crop the selected image")



# keep looping until the 'q' key is pressed
while True:
    # display the image and wait for a keypress
    key = cv.waitKey(1) & 0xFF
    # if the 'r' key is pressed, reset the cropping region
    if key == ord("r"):
        img = clone.copy()
        pt1 = []
        cv.imshow('Cards', img)
    # if the 'c' key is pressed, break from the loop
    elif key == ord("c"):
        crop_img(pt1)
        pt1 = []
    elif key == ord("q"):
        break;


cv.destroyAllWindows()

