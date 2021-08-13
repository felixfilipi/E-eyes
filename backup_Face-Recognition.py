import cv2
import numpy as np
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml');
font = cv2.FONT_HERSHEY_SIMPLEX
role = input('Role = ')

cam = cv2.VideoCapture(0)
cv2.namedWindow("window",cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

def get_name():
    path = 'dataset'
    imagePaths = [os.path.join(path,i) for i in os.listdir(path)]
    names = []
    for path in imagePaths:
        name = os.path.split(path)[1].split('.')[1]
        names.append(name)

    names = np.unique(names)      
    return names

while True:
    ret, img =cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.25, 6, minSize = (100,100))    
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        cface_gray = gray[y:y+h, x:x+w]
        cface_resize = cv2.resize(cface_gray, (270,270), interpolation=cv2.INTER_AREA)
        norm_img = np.zeros((cface_resize.shape[0], cface_resize.shape[1]))
        cface_norm = cv2.normalize(cface_resize, norm_img, 0, 255, cv2.NORM_MINMAX)
        id, confidence = recognizer.predict(cface_norm)	
        if (confidence < 50):
            cv2.rectangle(img, (20,275), (240,145), (0,0,0), -1)
            cv2.putText(img, str(get_name()[id]), (30,220), font, 1, (255,255,255), 2)
            cv2.putText(img, str(role), (30,260), font, 1, (255,255,255), 2) 
            confidence = "  {0}%".format(round(100 - confidence))
            cv2.putText(img, str('Conf={}'.format(confidence)), (30,280), font, 1, (255,255,0), 1) 
        else:
            cv2.rectangle(img, (20,400), (240,300), (0,0,0), -1)
            cv2.putText(img, str('Unknown'), (30,320), font, 1, (255,255,255), 2)
            confidence = "  {0}%".format(round(100 - confidence))
            cv2.putText(img, str('Conf={}'.format(confidence)), (30,380), font, 1, (255,255,0), 1)
    cv2.imshow('Opencv',img) 
    k = cv2.waitKey(10) & 0xff 
    if k == 27:
        break

print("\n Exit Program")
cam.release()
cv2.destroyAllWindows()
