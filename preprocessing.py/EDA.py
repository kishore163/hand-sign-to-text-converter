import os
import numpy as np
import mattplotlib.pyplot as plt

Xtrain=[]
Ytrain=[]
for i in range(len(X_train)):
  if i%2==0:
    Xtrain.append(X_train[i])
    Ytrain.append(Y_train[i])
X_train=np.array(Xtrain)
Y_train=np.array(Ytrain)
len(X_train)

a=np.unique(Y_train)
b=sorted(os.listdir(train_set))
hash=dict(zip(a,b))


unique_images=[]                                 
for i in range(len(hash)):
  for ind,img_label in enumerate(Y_train):
    if i==img_label:
      unique_images.append(X_train[ind])
      break
      
cols = 8
rows = 4
fig = plt.figure(figsize = (24, 12))

for i in range(len(hash)):
        ax = plt.subplot(rows, cols, i + 1)
        plt.imshow(unique_images[i])
        plt.title(hash[i])
        ax.title.set_fontsize(20)
        ax.axis('off')
plt.show()
