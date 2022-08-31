from tensorflow.keras.models import load_model
import time
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
#from cvzone.HandTrackingModule import HandDetector
#detector = HandDetector(maxHands=1)
from gtts import gTTS
import os
from textblob import TextBlob

model=load_model(r"predictor.h5")

d={0:'A'}
for i in range(66,91):
    d[i-65]=chr(i)
    
d[26]='space'
d[27]='del'
d[28]='nothing

img=cv2.imread(r"C_test.jpg")
img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
img_file = skimage.transform.resize(img, (64, 64, 3))
img_arr = np.asarray(img_file).reshape((-1, 64, 64, 3))
prediction=model.predict(img_arr).argmax(axis=-1)
prediction[0]


cap = cv2.VideoCapture(0)
count=0
res=""

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1))
    rectangle=cv2.rectangle(img,(50,50),(400,400),(255,0,0),2)
    imgCrop=img[50:400,50:400]
    img_file = skimage.transform.resize(imgCrop, (64, 64, 3))
    img_arr = np.asarray(img_file).reshape((-1, 64, 64, 3))
    cv2.imshow('crop_img',imgCrop)
    pred=model.predict(img_arr).argmax(axis=-1)[0]
    if count==100:
     if pred=='space':
        res+=' '
        continue
     if pred=='del':
        res=res[:-1]
        continue
     if pred=='nothing':
        continue
      res+=d[pred]
      count=0
      print(res)
    cv2.imshow('webcam',img)    
    count+=1
    if cv2.waitKey(1) == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
