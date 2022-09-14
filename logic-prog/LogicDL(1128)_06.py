'''
Github: https://github.com/converges/DL-starter/
Author: An
'''
''' Exercise 06: Python DL
Create hundreds data and try teaching a multiplication to keras.
Show a graph of epoch vs loss fucntions values.
* Multiplication is not a good example for machine learning, but just try it.
'''
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

num_list = [i for i in range(-128, 127)] # QTY = 256

X = [(x, y) for x in num_list for y in num_list if x <= y] # QTY: 256H2 = 32,896.
Y = [x*y for x,y in X]

model = Sequential()
model.add(Dense(60, input_dim=2, activation='relu'))
model.add(Dense(30, activation='relu'))
model.add(Dense(1, activation='relu'))
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
hist = model.fit(X, Y, epochs=100, batch_size=1000)

evaluation = model.evaluate(X, Y)
print(f"\n Test Accuracy: {evaluation[1]:.4f}\n Loss: {evaluation[0]:.4f}")

losses = hist.history['loss']

plt.figure(figsize=(10, 4))
plt.plot(list(range(len(losses))), losses, c='purple', label='Loss')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()
plt.title("Deep Learning: Loss for Each Epoch.")
plt.show()
# Done: 2021-11-21.



