import cv2
import numpy as np
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

def get_name():
    path = '../images/dataset'
    imagePaths = [os.path.join(path,i) for i in os.listdir(path)]
    names = []
    for path in imagePaths:
        name = os.path.split(path)[1].split('.')[1]
        names.append(name)

    names = np.unique(names)      
    return names


conf_arr = []
for i in range(len(faceSamples)):
    id, confidence = recognizer.predict(faceSamples[i])	

    if (confidence < 50):
        name = str(get_name()[id])
        print(name)
        conf_arr.append(name)
        # role dari database
    else:
        conf_arr.append("None")

distinct = len(set(conf_arr))
if distinct == 1:
    #kirim
    print(name)
else:
    print("Test lagi")








#if (confidence < 50):
#   cv2.rectangle(img, (20,275), (240,145), (0,0,0), -1)
#   cv2.putText(img, str(get_name()[id]), (30,220), font, 1, (255,255,255), 2)
#   cv2.putText(img, str(role), (30,260), font, 1, (255,255,255), 2) 
#   confidence = "  {0}%".format(round(100 - confidence))
#   cv2.putText(img, str('Conf={}'.format(confidence)), (30,280), font, 1, (255,255,0), 1) 
#else:
#   cv2.rectangle(img, (20,400), (240,300), (0,0,0), -1)
#   cv2.putText(img, str('Unknown'), (30,320), font, 1, (255,255,255), 2)
#   confidence = "  {0}%".format(round(100 - confidence))
#   cv2.putText(img, str('Conf={}'.format(confidence)), (30,380), font, 1, (255,255,0), 1)

print("\n Exit Program")
