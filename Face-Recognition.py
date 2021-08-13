
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
role = input('Role = ')

cam = cv2.VideoCapture(0)
cv2.namedWindow("window",cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

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
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(img, 1.25, 5, minSize = (100,100))
        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            cface_gray = gray[y:y+h, x:x+w]
            cface_resize = cv2.resize(cface_gray, (270,270), interpolation=cv2.INTER_AREA)
            norm_img = np.zeros((cface_resize.shape[0], cface_resize.shape[1]))
            cface_norm = cv2.normalize(cface_resize, norm_img, 0, 255, cv2.NORM_MINMAX)
            id, confidence = recognizer.predict(cface_norm)

            if (confidence < 55):
                cv2.rectangle(img, (10,400), (260,220), (0,0,0), -1)
                cv2.putText(img, str(get_name()[id]), (20,300), font, 1, (255,255,255), 2)
                cv2.putText(img, str(role), (20,340), font, 1, (255,255,255), 2)
                #confidence = round(100 - confidence)
                #cv2.putText(img, str('Conf={}%'.format(confidence)), (20,260), font, 1, (255,255,0), 1)
                cv2.putText(img, 'Suhu = {}'.format(round(sensor.get_object_1()+2.7,2)), (20, 260), font, 1, (0,0,255), 2)
                GPIO.output (GPIO_BUZZER, True)
                time.sleep(2)
            else:
                cv2.rectangle(img, (20,400), (240,250), (0,0,0), -1)
                cv2.putText(img, str('Unknown'), (30,320), font, 1, (255,255,255), 2)
                #confidence = "  {0}%".format(round(100 - confidence))
                #cv2.putText(img, str('Conf={}'.format(confidence)), (30,380), font, 1, (255,255,0), 2)

    cv2.imshow('Opencv',img)
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break

print("\n Exit Program")
cam.release()
cv2.destroyAllWindows()

