import cv2
import numpy as np
import os
import json
import base64
import paho.mqtt.client as mqtt
import time
import sys
import threading
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

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml');
font = cv2.FONT_HERSHEY_SIMPLEX

cam = cv2.VideoCapture(0)
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

bus = SMBus(1)
sensor = mlx90614.MLX90614(bus, address = 0x5A)

broker = "mqtt.antares.id"
port = 1883
client = mqtt.Client("scan_send")

def send_photo(temperature):
    client.connect(broker, port)
    access_key = "c9ab16824dc3b3d4:c76af9ff466e3c4d"
    to = "/antares-cse/antares-id/e-eyes/send_face"
    topic = "/oneM2M/req/c9ab16824dc3b3d4:c76af9ff466e3c4d/antares-cse/json"

    with open("scan/photo_scan.jpg", "rb") as file:
        data = base64.b64encode(file.read())

    data_str = data.decode("utf-8")
    
    content = {
            "m2m:rqp": {
                "fr": access_key,
                "to": to,
                "op": 1,
                "rqi": "face_detect",
                "pc": {
                    "m2m:cin": {
                        "cnf": data_str,
                        "con": str(temperature)
                        }
                    },
                "ty": 4
                }
            }

    json_obj = json.dumps(content, indent = 1)
    client.publish(topic, json_obj)

prediction = " "

def thread1():
    global prediction
    lock = threading.Lock()
    with lock:
        while True:
            prediction = input()
            time.sleep(2)
            prediction = ""

threading.Thread(target = thread1).start()

count = 0
while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    range = get_range()
    if range < 30:
        cv2.rectangle(img, (195,20), (455,60), (0,0,0), -1)
        cv2.putText(img, 'Tolong menjauh', (200,50), font, 1, (255,255,255), 2)
        GPIO.output(GPIO_BUZZER, False)
    #elif range > 50:
    #    cv2.rectangle(img, (195,20), (470,60), (0,0,0), -1) #top,left,right,btm
    #    cv2.putText(img, 'Tolong Mendekat', (200,50), font, 1, (255,255,255), 2)
    #    GPIO.output(GPIO_BUZZER, False)
    else:
        cv2.rectangle(img, (195,20), (470,60), (0,0,0), -1)
        cv2.putText(img, 'Tahan Sebentar', (200,50), font, 1, (255,255,255),2)
        #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.25, 5, minSize = (100,100))
        for(x,y,w,h) in faces:
            temperature = round(sensor.get_object_1() + 2.7, 2)
            cv2.rectangle(img, (20,275), (240,145), (0,0,0), -1)
            cv2.putText(img, prediction, (30,220), font, 1, (255,255,255), 2)
            #cv2.putText(img, str(role), (30,260), font, 1, (255,255,255), 2)
            #confidence = "  {0}%".format(round(100 - confidence))
            cv2.putText(img, str('Temp={}C'.format(temperature)), (30,280), font, 1,(255,255,0), 1)
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            cface_gray = gray[y:y+h, x:x+w]
            cface_resize = cv2.resize(cface_gray, (270,270), interpolation=cv2.INTER_AREA)
            norm_img = np.zeros((cface_resize.shape[0], cface_resize.shape[1]))
            cface_norm = cv2.normalize(cface_resize, norm_img, 0, 255, cv2.NORM_MINMAX)
            if count == 60:
                cv2.imwrite("scan/photo_scan.jpg", cface_norm)
                send_photo(temperature)
                count = 0

            count += 1

    cv2.imshow('Opencv',img)
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break

print("\n Exit Program")
cam.release()
cv2.destroyAllWindows()

