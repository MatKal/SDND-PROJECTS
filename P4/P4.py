import tensorflow as tf
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

    correction = 0.2 # this is a parameter to tune
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

    
    
#     image_flipped = np.fliplr(image)
#     images.append(image_flipped)
#     measure_flipped = -measurement
#     measurements.append(measure_flipped)

X_train = np.array(images)
y_train = np.array(measurements) 

from keras.models import Sequential
from keras.layers import Flatten, Dense, Lambda
from keras.layers.convolutional import Convolution2D as Conv2D
from keras.layers.pooling import MaxPooling2D

model = Sequential()
model.add(Lambda(lambda x: x / 255.0 - 0.5, input_shape=(160, 320, 3)))
model.add(Conv2D(6, 5, 5, activation='relu'))
model.add(MaxPooling2D())
model.add(Conv2D(6, 5, 5, activation='relu'))
model.add(MaxPooling2D())
model.add(Flatten())
model.add(Dense(120))
model.add(Dense(84))
model.add(Dense(1)) 

model.compile(loss='mse', optimizer='adam')
model.fit(X_train, y_train, validation_split=0.2, shuffle=True, epochs=5)
model.save('model.h5')

exit()