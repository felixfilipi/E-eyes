import cv2
import numpy as np
from PIL import Image
import os
from sklearn.preprocessing import LabelEncoder

path = 'dataset'
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml");

def Split_Image_Name(path):
    imagePaths = [os.path.join(path,i) for i in os.listdir(path)]
    faceSamples=[]
    names = []
    for path in imagePaths:
        PIL_img = Image.open(path).convert('L') 
        img_array = np.array(PIL_img,'uint8')
        name = os.path.split(path)[1].split('.')[1]
        face = detector.detectMultiScale(img_array)
        for (x,y,w,h) in face:
            faceSamples.append(img_array[y:y+h,x:x+w])
            names.append(name)
    return faceSamples,names

print ("\n Training...")
face,name = Split_Image_Name(path)
ids = LabelEncoder().fit_transform(name)
recognizer.train(face, ids)
recognizer.write('trainer/trainer.yml') 
print("\n {0} faces already trained. Exiting Program".format(len(np.unique(ids))))