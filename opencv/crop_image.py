import cv2 as cv
import numpy as np
 


def mouse_click(event,x,y,flags,param):
    """
    This is method to capture the mouse click event on the image
    and store the point coordinates into pt1 variable
    """
    if event == cv.EVENT_LBUTTONDOWN:
        pt1.append([x,y])
        if len(pt1)>1:
            cv.line(img, tuple(pt1[-2]), tuple(pt1[-1]), (0,255,0), 2)
            cv.imshow('Cards', img)


def crop_img(pt1):
    """
    This is method to crop the selected area (points given in the param pt1) 
    from the image and display it into new window
    """
    # remove the last point from pt1 list as we just need 4 points
    pt1 = np.float32(pt1[:-1])  
    # transformed coordinates for the new image
    pt2 = np.float32([[0,0], [width,0], [width,height], [0,height]])
    # generate matrix for transformation
    matrix = cv.getPerspectiveTransform(pt1, pt2)
    # get cropped image from the original image using the matrix
    imgOut = cv.warpPerspective(img, matrix, (width,height))
    # show cropped image in new window
    cv.imshow('Crop Card', imgOut)


def write_text(img):
    """
    This method is to write text on the given image
    """
    font = cv.FONT_HERSHEY_SIMPLEX
    scale = 0.5
    color = (0,0,0)
    font_size = 1
    img = cv.putText(img, "1. Click on selected area", (20,15), font, scale, color, font_size, cv.LINE_AA)
    img = cv.putText(img, "2. Press 'c' to crop the selected image", (20, 35), font, scale, color, font_size, cv.LINE_AA)
    img = cv.putText(img, "3. Press 'r' to reset image", (20,55), font, scale, color, font_size, cv.LINE_AA)
    return img


pt1 = []    # pt1 list to hol
width,height = 250,350  # width & heigh of the cropped image
img = cv.imread('cards.jpg')    # read cards image
clone = img.copy()  # get clone of image for future
img = write_text(img)
cv.imshow('Cards', img)
cv.setMouseCallback('Cards', mouse_click);


# keep looping until the 'q' key is pressed
while True:
    # display the image and wait for an action
    key = cv.waitKey(1) & 0xFF
    # if the 'r' key is pressed, reset the cropping region
    if key == ord("r"):
        pt1 = []
        img = clone.copy()
        img = write_text(img)
        cv.imshow('Cards', img)
    # if the 'c' key is pressed, crop the selected image
    elif key == ord("c"):
        crop_img(pt1)
        pt1 = []
    elif key == ord("q"):
        break;


cv.destroyAllWindows()

