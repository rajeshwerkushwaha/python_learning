import numpy as np
import cv2 as cv


path = '/Users/rkumar/.virtualenvs/cv/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_alt2.xml'
faceCascade = cv.CascadeClassifier(path)

cap = cv.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height

while True:
    ret, img = cap.read()
    # img = cv.flip(img, -1)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,     
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )

    for (x,y,w,h) in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]  

    cv.imshow('video',img)

    k = cv.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

cap.release()
cv.destroyAllWindows()



# ❯ ls
# __init__.py                                haarcascade_fullbody.xml
# __pycache__                                haarcascade_lefteye_2splits.xml
# haarcascade_eye.xml                        haarcascade_licence_plate_rus_16stages.xml
# haarcascade_eye_tree_eyeglasses.xml        haarcascade_lowerbody.xml
# haarcascade_frontalcatface.xml             haarcascade_profileface.xml
# haarcascade_frontalcatface_extended.xml    haarcascade_righteye_2splits.xml
# haarcascade_frontalface_alt.xml            haarcascade_russian_plate_number.xml
# haarcascade_frontalface_alt2.xml           haarcascade_smile.xml
# haarcascade_frontalface_alt_tree.xml       haarcascade_upperbody.xml
# haarcascade_frontalface_default.xml
# ❯ pwd
# /Users/rkumar/.virtualenvs/cv/lib/python3.7/site-packages/cv2/data