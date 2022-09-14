'''
Github: https://github.com/converges/DL-starter/
Author: An
'''
''' Exercise 03: Python DL
Find a Hyper-parameter with better result(accuracy).
Just Exercise, try it.
'''
# Hyper-parameter
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from keras.models import load_model
#
#
np.random.seed(3)
tf.random.set_seed(3)

# (1) csv -> ndarray.
# Download a csv file first.
Data_set = np.loadtxt("C:/Users/AN/Documents/Mathematics/LogicProg/data/ThoraricSurgery.csv", delimiter=',')

X = Data_set[:, 0:17]
Y = Data_set[:, 17]

model = Sequential()
model.add(Dense(60, input_dim=17, activation='tanh')) # activation func for input-perceptron 'sigmoid' -> 'tanh', 
model.add(Dense(30, activation='sigmoid')) # new hidden layers
model.add(Dense(15, activation='sigmoid'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
model.fit(X, Y, epochs=1000, batch_size=25) # epoch 100 -> 1000, batch_size 10 -> 25

evaluation = model.evaluate(X, Y)[1]

model.save("my_model.h5")

print(f"\n Test Accuracy: {model.evaluate(X, Y)[1]:.4f}")
# 0.9404 (When I tested)
# Done: 2021-11-11