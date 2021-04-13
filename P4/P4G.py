# P4 - .py Version (Generator)
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
import random
import sklearn
import math
import csv
import cv2

samples = []
with open('./data/driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        samples.append(line)

samples.pop(0)

train_samples, valid_samples = train_test_split(samples, test_size=0.2)

def Generator(samples, batch_size=32):
    num_samples = len(samples)
    
    while 1:
        random.shuffle(samples)
        
        for offset in range(0, num_samples, batch_size):
            batch_samples = samples[offset:offset+batch_size]
            images = []
            measurements = []
            
            for batch_sample in batch_samples:
                
                steering_center = float(batch_sample[3])
                correction = 0.1
                steering_left = steering_center + correction
                steering_right = steering_center - correction
    
                path = './data/IMG/'
                img_center = cv2.imread(path + batch_sample[0].split('/')[-1])
                img_left = cv2.imread(path + batch_sample[1].split('/')[-1])
                img_right = cv2.imread(path + batch_sample[2].split('/')[-1])
    
                images.append(img_center)
                measurements.append(steering_center)
            
                images.append(cv2.flip(img_center, 1))
                measurements.append(steering_center*-1.0)

                images.append(img_left)
                measurements.append(steering_left)
                
                images.append(cv2.flip(img_left, 1))
                measurements.append(steering_left*-1.0)

                images.append(img_right)
                measurements.append(steering_right)
                
                images.append(cv2.flip(img_right, 1))
                measurements.append(steering_right*-1.0)
            
            X_train = np.array(images)
            y_train = np.array(measurements)
            
            yield sklearn.utils.shuffle(X_train, y_train)

batch_size = 32
train_generator = Generator(train_samples, batch_size=batch_size)
valid_generator = Generator(valid_samples, batch_size=batch_size)
            
            
from keras.models import Sequential
from keras.layers import Flatten, Dense, Lambda, Cropping2D, Dropout, BatchNormalization
from keras.layers.convolutional import Convolution2D as Conv2D
from keras.layers.pooling import MaxPooling2D

model = Sequential()

model.add(Lambda(lambda x: x / 255.0 - 0.5, input_shape=(160, 320, 3)))
model.add(Cropping2D(cropping=((70, 25), (0, 0))))

model.add(Conv2D(24, (5, 5), strides=2, activation='elu', padding='same'))
model.add(BatchNormalization())
model.add(MaxPooling2D(strides=(2, 2), padding='same'))

model.add(Conv2D(36, (5, 5), strides=2, activation='elu', padding='same'))
model.add(BatchNormalization())
model.add(MaxPooling2D(strides=(2, 2), padding='same'))

model.add(Conv2D(48, (5, 5), strides=2, activation='elu', padding='same'))
model.add(BatchNormalization())
model.add(MaxPooling2D(strides=(2, 2), padding='same'))

model.add(Conv2D(64, (3, 3), activation='elu', padding='same'))
model.add(BatchNormalization())
model.add(MaxPooling2D(strides=(2, 2), padding='same'))

model.add(Conv2D(64, (3, 3), activation='elu', padding='same'))
model.add(BatchNormalization())
model.add(MaxPooling2D(strides=(2, 2), padding='same'))

model.add(Flatten())
model.add(Dense(100))
model.add(BatchNormalization())

model.add(Dropout(rate=0.1))
model.add(Dense(50))
model.add(BatchNormalization())

model.add(Dropout(rate=0.1))
model.add(Dense(10)) 
model.add(BatchNormalization())

model.add(Dropout(rate=0.1))
model.add(Dense(1)) 

model.compile(loss='mse', optimizer='adam')

history_object = model.fit_generator(train_generator, \
            steps_per_epoch=math.ceil(len(train_samples) / batch_size), \
            validation_data=valid_generator, \
            validation_steps=math.ceil(len(valid_samples) / batch_size), \
            epochs=25, verbose=1)

model.save('Gmodel.h5')

print('GModel Saved!')

print(history_object.history.keys())
plt.plot(history_object.history['loss'])
plt.plot(history_object.history['val_loss'])
plt.title('model mean squared error loss')
plt.ylabel('mean squared error loss')
plt.xlabel('epoch')
plt.legend(['training set', 'validation set'], loc='upper right')
plt.show()

exit()