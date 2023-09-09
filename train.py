import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split

data=pd.read_csv("Output/dataset.csv", header=None, skiprows=1)

X = data.iloc[ : , :-1].values
Y = data.iloc[ : , -1].values

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size= 0.2)

model= tf.keras.models.Sequential([
    tf.keras.layers.Dense(6, activation="relu"),
    tf.keras.layers.Dense(20, activation="relu"),
    tf.keras.layers.Dense(10, activation= "relu"),
    tf.keras.layers.Dense(8, activation= "softmax")
])

model.compile(optimizer="adam",
              loss= "sparse_categorical_crossentropy",
              metrics=["accuracy"])

model.fit(X_train, Y_train, epochs=72)
model.evaluate(X_test, Y_test)
model.save("my_snake_model.h5")

