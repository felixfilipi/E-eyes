import cv2
import numpy as np
import os
import time
import RPi.GPIO as GPIO
import mlx90614
from smbus2 import SMBus

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO_BUZZER = 17
GPIO_TRIGGER = 23
GPIO_ECHO = 24
GPIO.setup(GPIO_BUZZER, GPIO.OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

GPIO.output(GPIO_TRIGGER, GPIO.LOW)
GPIO.output(GPIO_BUZZER, GPIO.LOW)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml');
font = cv2.FONT_HERSHEY_SIMPLEX

cam = cv2.VideoCapture(-1,2)
cv2.namedWindow("window",cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

def get_range():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.001)

    GPIO.output(GPIO_TRIGGER, False)
    timeout_counter = int(time.time())
    start = time.time()

    while GPIO.input(GPIO_ECHO)==0 and (int(time.time())-timeout_counter) < 3:
        start = time.time()

    timeout_counter = int(time.time())
    stop = time.time()
    while GPIO.input(GPIO_ECHO)==1 and (int(time.time()) - timeout_counter) < 3:
        stop = time.time()
    elapsed = stop-start
    distance = elapsed * 34320
    distance = distance / 2
    return distance

def get_name():
    path = 'dataset'
    imagePaths = [os.path.join(path,i) for i in os.listdir(path)]
    names = []
    for path in imagePaths:
        name = os.path.split(path)[1].split('.')[1]
        names.append(name)

    names = np.unique(names)
    return names

bus = SMBus(1)
sensor = mlx90614.MLX90614(bus, address = 0x5A)

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    range = get_range()
    if range < 30:
        cv2.rectangle(img, (195,20), (455,60), (0,0,0), -1)
        cv2.putText(img, 'Tolong menjauh', (200,50), font, 1, (255,255,255), 2)
        GPIO.output(GPIO_BUZZER, False)
    elif range > 50:
        cv2.rectangle(img, (195,20), (470,60), (0,0,0), -1) #top,left,right,btm
        cv2.putText(img, 'Tolong Mendekat', (200,50), font, 1, (255,255,255), 2)
        GPIO.output(GPIO_BUZZER, False)
    else:
        cv2.rectangle(img, (195,20), (470,60), (0,0,0), -1)
        cv2.putText(img, 'Tahan Sebentar', (200,50), font, 1, (255,255,255),2)
        #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.25, 5, minSize = (100,100))
        count = 0
        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            cface_gray = gray[y:y+h, x:x+w]
            cface_resize = cv2.resize(cface_gray, (270,270), interpolation=cv2.INTER_AREA)
            norm_img = np.zeros((cface_resize.shape[0], cface_resize.shape[1]))
            cface_norm = cv2.normalize(cface_resize, norm_img, 0, 255, cv2.NORM_MINMAX)
            if count == 20:
                cv2.imwrite("scan/aksfb.jpg", cface_norm)

            count += 1

    cv2.imshow('Opencv',img)
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break

print("\n Exit Program")
cam.release()
cv2.destroyAllWindows()

