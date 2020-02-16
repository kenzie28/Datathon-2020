# mlp for regression
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

# load the dataset
players = pd.read_csv("refined_players.csv")

players = players[["overall", "age", "shooting", "passing", "dribbling", "physic", "predicted_growth", "actual_growth"]]

# Select all features and the output
features = players.values[:, :-1]
output = players.values[:, -1]

x_train, x_test, y_train, y_test = train_test_split(features, output, test_size=0.33, random_state=28)

x_train, x_test, y_train, y_test = np.asarray(x_train), np.asarray(x_test), np.asarray(y_train), np.asarray(y_test)

print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

# determine the number of input features
n = x_train.shape[1]

# Creates the model of neural networks
model = Sequential()
model.add(Dense(12, activation='sigmoid', kernel_initializer='he_normal', input_shape=(n,)))
model.add(Dense(12, activation='sigmoid', kernel_initializer='he_normal'))
model.add(Dense(10, activation='sigmoid', kernel_initializer='he_normal'))
model.add(Dense(10, activation='sigmoid', kernel_initializer='he_normal'))
model.add(Dense(1))

# Compiles neural network model
model.compile(optimizer='adam', loss='mse')

# fit the model
model.fit(x_train, y_train, epochs=150, batch_size=32, verbose=0)

# evaluate the model
error = model.evaluate(x_test, y_test, verbose=0)
print('MSE: %.3f, RMSE: %.3f' % (error, np.sqrt(error)))

print("Input overall: ")
overall = (int(input()) - 66.97467291883756) / 6.879008402727097

print("Input player age: ")
age = (int(input()) - 24.890963297441242) / 4.331509309626816

print("Input player shooting stat: ")
shooting = (int(input()) - 52.94455540118096) / 14.049862406642577

print("Input player passing stat: ")
passing = (int(input()) - 57.84677839527614) / 10.57396927130625

print("Input player dribbling stat: ")
dribbling = (int(input()) - 62.87407375246035) / 10.512036950280264

print("Input player physic: ")
physic = (int(input()) - 65.7168432326039) / 9.583705626210728

print("Input player predicted growth: ")
pred_growth = (int(input()) - 4.922238624522404) / 5.046966889427111

new_data = [overall, age, shooting, passing, dribbling, physic, pred_growth]
yhat = model.predict([new_data])
print('Predicted: %.3f' % yhat)

