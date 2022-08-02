classes = 29
batch = 128
epochs = 3
learning_rate = 0.0001

def results(model):
    adam = Adam(lr=learning_rate)

    model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['accuracy'])

    start = time()
    history = model.fit(X_train, Y_train, batch_size=batch, epochs=epochs, validation_split=0.1, shuffle = True, verbose=1)
    train_time = time() - start

    model.summary()

    plt.figure(figsize=(12, 12))
    plt.subplot(3, 2, 1)
    plt.plot(history.history['accuracy'], label = 'train_accuracy')
    plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
    plt.xlabel('epoch')
    plt.ylabel('accuracy')
    plt.legend()
    plt.subplot(3, 2, 2)
    plt.plot(history.history['loss'], label = 'train_loss')
    plt.plot(history.history['val_loss'], label = 'val_loss')
    plt.ylabel('accuracy')
    plt.legend()
    plt.show()

    start = time()
    test_loss, test_acc = model.evaluate(X_test, Y_test)
    test_time = time() - start
    print('\nTrain time: ', train_time)
    print('Test accuracy:', test_acc)
    print('Test loss:', test_loss)
    print('Test time: ', test_time)
   
from time import time
from keras import utils
from keras.optimizers import Adam
from keras.applications import VGG16
model = Sequential()

model.add(VGG16(weights='imagenet', include_top=False, input_shape=(64,64,3)))

model.add(Flatten())

model.add(Dense(512, activation='sigmoid'))

model.add(Dense(29, activation='softmax'))

results(model)
