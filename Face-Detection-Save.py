import cv2
import os
import numpy as np

cam = cv2.VideoCapture(0)
cam.set(3, 640) #Height
cam.set(4, 480) #Weight
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
name = input('\n Enter your name = ')
print("\n Look at the camera and wait")

id_count = 0
while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = face_detector.detectMultiScale(gray, 1.25, 6, minSize = (100,100))
    
    for (x,y,w,h) in face:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0, 0, 255), 2)   
        cface_gray = gray[y:y+h, x:x+w]
        cface_resize = cv2.resize(cface_gray, (270,270), interpolation=cv2.INTER_AREA)
        norm_img = np.zeros((cface_resize.shape[0], cface_resize.shape[1]))
        cface_norm = cv2.normalize(cface_resize, norm_img, 0, 255, cv2.NORM_MINMAX)
        id_count += 1
        cv2.imwrite("dataset/User." + str(name) +'.' + str(id_count) + ".jpg", cface_resize)
            
    cv2.imshow('image', img)
    k = cv2.waitKey(100) & 0xff 
    
    if k == 27:
        break
    if id_count >= 30:
         break

print("\n Exiting Program")
cam.release()
cv2.destroyAllWindows()