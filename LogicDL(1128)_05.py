'''
Github: https://github.com/converges/DL-starter/
Author: An
'''
''' Exercise 05: Python DL
Create a dataset and try teaching calculating y=x^2 - 5x to keras.
Show a graph of epoch vs loss fucntions values.
* Multiplication & Power are not good examples for machine learning, but just try it.
'''
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

X = [0, 5, 10, 12, 17, 19, 23, 55, -32, -13, -63, -128]
Y = [x**2 - 5*x for x in X]

# Original Model.
model1 = Sequential()
model1.add(Dense(60, input_dim=1, activation='sigmoid')) #(a)
model1.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
hist = model1.fit(X, Y, epochs=100, batch_size=5) #(a)

evaluation = model1.evaluate(X, Y)
print(f"\n Test Accuracy: {evaluation[1]:.4f}\n Loss: {evaluation[0]:.4f}")

losses = hist.history['loss']

plt.figure(figsize=(10, 4))
plt.plot(list(range(len(losses))), losses, c='purple', label='Loss')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()
plt.title("Deep Learning: Loss for Each Epoch.")
plt.show()

# Advanced Model.
model2 = Sequential()
# model.add(Dense(60, input_dim=1, activation='sigmoid')) #(a)
model2.add(Dense(60, input_dim=1, activation='relu')) #(b)
model2.add(Dense(30, activation='relu')) #(b)
model2.add(Dense(1, activation='relu')) #(b)
model2.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
# hist = model.fit(X, Y, epochs=100, batch_size=5) #(a)
hist = model2.fit(X, Y, epochs=100, batch_size=3) #(b)

evaluation = model2.evaluate(X, Y)
print(f"\n Test Accuracy: {evaluation[1]:.4f}\n Loss: {evaluation[0]:.4f}")

losses = hist.history['loss']

plt.figure(figsize=(10, 4))
plt.plot(list(range(len(losses))), losses, c='purple', label='Loss')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()
plt.title("Deep Learning: Loss for Each Epoch.")
plt.show()
# Done: 21-11-21.