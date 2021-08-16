import cv2
import numpy as np
import json
import os
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
font = cv2.FONT_HERSHEY_SIMPLEX

path = 'scan/'
def Split_Image_Name(path):
    imagePaths = [os.path.join(path,i) for i in os.listdir(path)]
    faceSamples=[]
    names = []
    for path in imagePaths:
        PIL_img = Image.open(path).convert('L')
        img_array = np.array(PIL_img,'uint8')
        name = os.path.split(path)[1].split('.')[1]
        faceSamples.append(img_array)
        names.append(name)
    return faceSamples, names

faceSamples, names = Split_Image_Name(path)

#def get_name():
#    path = '../images/dataset'
#    imagePaths = [os.path.join(path,i) for i in os.listdir(path)]
#    names = []
#    for path in imagePaths:
#        name = os.path.split(path)[1].split('.')[1]
#        names.append(name)
#
#    names = np.unique(names)      
#    return names
f = open("trainer/dict.json")

label_dict = json.load(f)

def get_name(id, label_dict):
    for name, label in label_dict.items():
        if label == id:
            return name

conf_arr = []
id, confidence = recognizer.predict(faceSamples[0])	
#print(ids.inverse_transform())
#name = get_name(id, label_dict)
#name = str(get_name())
print(get_name(id, label_dict))

#if confidence > 60: 
#    print(id)
#else:
#    print("Unknown")
