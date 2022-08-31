import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import joblib
import cv2
from PIL import Image
from matplotlib.pyplot import imshow
import warnings
import pandas as pd
from tensorflow.keras.models import load_model
import time
import matplotlib.pyplot as plt
import matplotlib.image as img
from gtts import gTTS
import os
import skimage.transform
from textblob import TextBlob

warnings.filterwarnings(action='ignore')
#model=load_model('/content/drive/MyDrive/asl_alphabet_test/predictor.h5')
st.write(model.summary())

with st.sidebar:
  selected=option_menu(
      menu_title='Main_Menu',
      options=['Home','Upload']
  )


if selected=='Home':
  st.title('SIGN TO TEXT AND VOICE CONVERTER')
  st.subheader("This is an application which coverts hand signs to text or voice")
  #st.image(r"/content/drive/MyDrive/ML/homepage.jpg",width=800)

res=""
d={0:'A'}
for i in range(66,91):
    d[i-65]=chr(i)
    
d[26]='space'
d[27]='del'
d[28]='nothing'
count=0
if selected=='Upload':
  st.title("YOU CAN UPLOAD THE IMAGE HERE")
  #st.image(r"/content/drive/MyDrive/ML/upload1.webp")
  image_file = st.file_uploader("Upload Images", type=["jpg"])
  try:
    img = Image.open(image_file)
    st.image(img)
    img_file = skimage.transform.resize(img, (64, 64, 3))
    img_arr = np.asarray(img_file).reshape((-1, 64, 64, 3))
    prediction=model.predict(img_arr).argmax(axis=-1)[0]
    print(prediction)
    if count==100:
      if pred=='space':
        res+=' '
        continue
      if pred=='del':
        res=res[:-1]
        continue
      if pred=='nothing':
        continue
      res+=d[prediction]
      obj=TextBlob(res)
      obj.correct()
      st.write(obj.correct())
      mytext = res
      language = 'en'

      myobj = gTTS(text=mytext, lang=language, slow=False)
      myobj.save("res.mp3")
      video1=open(os.system("res.mp3"),"rb")
      st.video(video1)
  except:
    print("error")
      
