import cv2
import json
import numpy as np
from PIL import Image
import os

class LabelEncoder:
    def __init__(self, dataset):
        self.dataset = dataset
        self.dict = dict()
        self.labeled = []

    def createDict(self):
        temp = []
        
        for i in range(len(self.dataset)):
            if self.dataset[i] not in temp:
                temp.append(self.dataset[i])

        temp_dict = dict()
        for i in range(len(temp)):
            temp_dict[temp[i]] = i

        self.dict = temp_dict

    def fit(self):
        self.createDict()
        labeled = []

        for i in range(len(self.dataset)):
            val = self.dict[self.dataset[i]]
            labeled.append(val)

        self.labeled = labeled
        return labeled
    
    def return_key(self, dict, x):
        for key, value in dict.items():
            if x == value:
                return key

        return "None"


    def inverse_transform(self, labeled):
        inversed = []
        temp_dict = self.dict
        
        for i in range(len(labeled)):
            temp = self.return_key(temp_dict, labeled[i])
            inversed.append(temp)

        return inversed

# set path
path = '../images/dataset/'
recognizer = cv2.face.LBPHFaceRecognizer_create()

def Split_Image_Name(path):
    imagePaths = [os.path.join(path,i) for i in os.listdir(path)]
    faceSamples=[]
    names = []
    for path in imagePaths:
        PIL_img = Image.open(path).convert('L') 
        img_array = np.array(PIL_img,'uint8')
        name = os.path.split(path)[1].split('.')[1]
        #face = detector.detectMultiScale(img_array)
        #for (x,y,w,h) in face:
        faceSamples.append(img_array)
        names.append(name)
    return faceSamples,names

print ("\n Training...")
face,name = Split_Image_Name(path)
new = LabelEncoder(name)
ids = np.array(new.fit())
label_dict = new.dict

with open("trainer/dict.json", "w") as outfile:
    json.dump(label_dict, outfile)

print(ids, name)
recognizer.train(face, ids)
recognizer.write('trainer/trainer.yml')
print("\n {0} faces already trained. Exiting Program".format(len(np.unique(ids))))
