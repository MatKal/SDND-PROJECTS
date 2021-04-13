# P4 - .py Version
import matplotlib.pyplot as plt
import numpy as np
import csv
import cv2

lines = []
with open('./data/driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        lines.append(line)

lines.pop(0)
        
images = []
measurements = []

for line in lines: 
    steering_center = float(line[3])

    correction = 0.1
    steering_left = steering_center + correction
    steering_right = steering_center - correction
    
    path = './data/IMG/'
    img_center = cv2.imread(path + line[0].split('/')[-1])
    img_left = cv2.imread(path + line[1].split('/')[-1])
    img_right = cv2.imread(path + line[2].split('/')[-1])
    
    images.append(img_center)
    measurements.append(steering_center)
    
    images.append(img_left)
    measurements.append(steering_left)

    images.append(img_right)
    measurements.append(steering_right)

ag_images, ag_measurements = [], []
for image, measurement in zip(images, measurements):
    ag_images.append(image)
    ag_measurements.append(measurement)
    
    ag_images.append(cv2.flip(image, 1))
    ag_measurements.append(measurement*-1.0)

X_train = np.array(ag_images)
y_train = np.array(ag_measurements) 

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
history_object = model.fit(X_train, y_train, validation_split=0.2, shuffle=True, epochs=25)
model.save('model.h5')

print('Model Saved!')

print(history_object.history.keys())
plt.plot(history_object.history['loss'])
plt.plot(history_object.history['val_loss'])
plt.title('model mean squared error loss')
plt.ylabel('mean squared error loss')
plt.xlabel('epoch')
plt.legend(['training set', 'validation set'], loc='upper right')
plt.show()

exit()