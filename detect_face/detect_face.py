import cv2 as cv

face_cascade = cv.CascadeClassifier('/anaconda3/pkgs/libopencv-3.4.2-h7c891bd_1/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
#face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')

img = cv.imread('groupphoto.jpg')

print(img)

# cv.imshow("FacesImg", img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# faces = face_cascade.detectMultiScale(gray, scaleFactor=2, minNeighbors=5)

# for (x,y,w,h) in faces:
#     img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

# #resized = cv2.resize(img, (int(img.shape[1]/7), int(img.shape[0]/7)))
# cv2.imshow("FacesImg", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()