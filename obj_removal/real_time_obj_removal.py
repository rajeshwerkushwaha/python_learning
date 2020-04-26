import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (width, height)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, size)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()



# import cv2 as cv
# import numpy as np

# algo = 'MOG2' # you can chose any algo between MOG2 or KNN
# if algo == 'MOG2':
#     backSub = cv.createBackgroundSubtractorMOG2(history = 50,
#                                                 varThreshold = 16,
#                                                 detectShadows = True)
# elif algo == 'KNN':
#     backSub = cv.createBackgroundSubtractorKNN()

# cap = cv.VideoCapture(0)  # capture webcam object
# print(dir(cap.get.__getattribute__))

# if not cap.isOpened:
#     print('Unable to open: ' + args.input)
#     exit(0)
# while True:
#     ret, frame = cap.read()       # start getting feed from webcam


#     if frame is None:
#         break
    
#     fgMask = backSub.apply(frame) # apply above provided Background Subtraction algo to each frame
    
#     fgMask_new = fgMask[:,:,np.newaxis]
#     fgMask_new = np.where(fgMask_new==1, [1,1,1], [0,0,0])

# #     print(frame.shape, fgMask_new.shape)
# #     sub = cv.subtract(frame, fgMask_new)

#     cv.imshow('Frame', frame)
#     cv.imshow('FG Mask', fgMask)
# #     cv.imshow('Subtract', sub)
    
    
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break
        
# cv.destroyAllWindows()



# # a = np.array([[1, 2, 3],
# # ...           [2, 2, 4],
# # ...           [3, 1, 5]])

# # b = np.array([[0, 0, 0],
# # ...           [0, 1, 1],
# # ...           [0, 0, 0]])

# # c = np.array([[1, 1, 1],
# # ...           [0, 1, 1],
# # ...           [0, 0, 0]])





