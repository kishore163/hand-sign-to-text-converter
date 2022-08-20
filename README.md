# hand-sign-to-text-converter
This is an application built on top of keras which converts hand signs to text.This was built mainly built to help the deaf and dumb to help them to communicate easily.

### About the data
The data consists of nearly 80000 images for training and around 10000 images for testing.
The images are divided into 29 classes where 26 classes are the alphabets of english letter and 3 other classes represent to delete,nothing and space.

### Preprocessing

The images have been resized,scaled and one hot encoding is applied.
Some EDA is also performed to understand the images we are working with


### Model

CNN model with variety of layers were tried and the best suited one was a stacked 5 layered One but the problem with this one was it did not perform very well on Testing data and hence vgg16 was implemented in the final part.

### Performance
##### Stacked CNN with 5 layers- 92% accurate for train dataset and 72% for testing
#####vgg16 - 98% accurate for trainset and 93% accurate for testset


