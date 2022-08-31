# hand-sign-to-text-converter
This is an application built using python and on top of keras which converts hand signs to text and voice. <br /> This was mainly built to help the deaf and dumb to help them to communicate easily with the outer world.

### About the data
The data consists of nearly 80000 images for training and around 10000 images for testing. <br />
The images are divided into 29 classes where 26 classes are the alphabets of english letter and 3 other classes represent to delete,nothing and space.

### Preprocessing

The images have been resized,scaled and one hot encoding is applied <br />
Some EDA is also performed to understand the images we are working with


### Model

CNN model with variety of layers were tried and the best suited one was a stacked 5 layered One but the problem with this one was it did not perform very well on Testing data and hence vgg16 was implemented in the final part.

### Performance
#### Stacked CNN with 5 layers- 92% accurate for train dataset and 72% for testing
#### vgg16 - 98% accurate for trainset and 93% accurate for testset

## Features in the application
-> can convert real time video to text and audio <br />
-> auto-correction of misspelled texts <br />
-> can upload images also which are converted to text <br />

## CHALLENGES FACED
The main challenges were the errors which I came across while training the model and during the developing phase. 
Thanks to stackoverflow,google,youtube and some documentations which helped me understand and rectify the errors. Rectifying Some small errors such as passing the image without resizing to the model which resulted in wrong output although seems silly now were TimeConsuming.Adding features to the application were also a bit challenging and I had to play with some of the variables to get things at the right place.

## Learnings

-> IN depth knowledge of working with images <br />
-> best way to deal with errors <br />
-> new concepts of machine learning and computer vision <br />
-> integrating the model to the application <br />
