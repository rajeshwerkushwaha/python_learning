import cv2 as cv
import numpy as np

algo = 'MOG2' # you can chose any algo between MOG2 or KNN
if algo == 'MOG2':
    backSub = cv.createBackgroundSubtractorMOG2(history = 50,
                                                varThreshold = 16,
                                                detectShadows = True)
elif algo == 'KNN':
    backSub = cv.createBackgroundSubtractorKNN()

cap = cv.VideoCapture(0)  # capture webcam object

if not cap.isOpened:
    print('Unable to open: ' + args.input)
    exit(0)
while True:
    ret, frame = cap.read()       # start getting feed from webcam


    if frame is None:
        break
    
    fgMask = backSub.apply(frame) # apply above provided Background Subtraction algo to each frame
    
    fgMask_new = fgMask[:,:,np.newaxis]
    fgMask_new = np.where(fgMask_new==1, [1,1,1], [0,0,0])

    #print(frame.shape, fgMask_new.shape)
    sub = cv.subtract(frame, fgMask_new)

    cv.imshow('Frame', frame)
    cv.imshow('FG Mask', fgMask)
    cv.imshow('Subtract', sub)
    
    
    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break



# a = np.array([[1, 2, 3],
# ...           [2, 2, 4],
# ...           [3, 1, 5]])

# b = np.array([[0, 0, 0],
# ...           [0, 1, 1],
# ...           [0, 0, 0]])

# c = np.array([[1, 1, 1],
# ...           [0, 1, 1],
# ...           [0, 0, 0]])





