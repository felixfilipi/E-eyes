import cv2
import glob
import shutil
import base64
import paho.mqtt.client as mqtt
import time
import os
import json
import numpy as np

broker = "mqtt.antares.id"
port = 1883
client = mqtt.Client("train_send")

cam = cv2.VideoCapture(0)
cam.set(3, 640) #Height
cam.set(4, 480) #Weight
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#name = input('\n Enter your name = ')
name = input()
print("\n Look at the camera and wait")

def send_image(name):
    client.connect(broker, port)
    access_key = "c9ab16824dc3b3d4:c76af9ff466e3c4d"
    to = "/antares-cse/antares-id/e-eyes/send_file"
    topic = "/oneM2M/req/c9ab16824dc3b3d4:c76af9ff466e3c4d/antares-cse/json"

    shutil.make_archive("archive", "zip", "temp/")

    with open("archive.zip", "rb") as file:
        data = base64.b64encode(file.read())

    data_str = data.decode("utf-8")

    n = 50000
    chunks = [data_str[i:i+n] for i in range(0, len(data_str), n)]

    done_signal = "DONE"
    chunks.append(done_signal)

    for i in range(len(chunks)):
         content = {
                  "m2m:rqp": {
                          "fr": access_key,
                          "to": to,
                          "op": 1,
                          "rqi": "train_face",
                          "pc": {
                              "m2m:cin": {
                                  "cnf": name,
                                  "con": chunks[i]
                                  }
                              },
                      "ty": 4
                      }
                  }

         json_obj = json.dumps(content, indent = 1)
         client.publish(topic, json_obj)
         time.sleep(0.5)

def delete_files():
    files = glob.glob("temp/*")
    for f in files:
        os.remove(f)

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
        cv2.imwrite("temp/User." + str(name) +'.' + str(id_count) + ".jpg", cface_norm)
            
    cv2.imshow('image', img)
    k = cv2.waitKey(100) & 0xff 
    
    if k == 27:
        break
    if id_count >= 30:
         break

send_image(name)
delete_files()
cam.release()
cv2.destroyAllWindows()
