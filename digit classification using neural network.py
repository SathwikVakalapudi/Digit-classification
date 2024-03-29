# -*- coding: utf-8 -*-
"""Untitled

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gKlR9KyF7GSnuMjysUr_HgLVZoivS5k1
"""

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt
import numpy as np

(X_train,y_train),(X_test,y_test)=keras.datasets.mnist.load_data()

len(X_train)

X_train[0].shape

X_train[0]

plt.matshow(X_train[0])

y_train[0]

y_train[:5]

X_train=X_train/255
X_test=X_test/255

X_train_flattened=X_train.reshape(X_train.shape[0],-1)
X_test_flattened=X_test.reshape(X_test.shape[0],-1)

X_train_flattened.shape

model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, input_shape=(784,), activation='sigmoid')
])



model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)



model.fit(X_train_flattened, y_train, epochs=20)



model.evaluate(X_test_flattened,y_test)

plt.matshow(X_test[0])

y_predicted=model.predict(X_test_flattened)

y_predicted[0]

np.argmax(y_predicted[0])

y_predicted_labels=[np.argmax(i) for i in y_predicted]
y_predicted_labels[:5]

y_test[:5]

cm=tf.math.confusion_matrix(labels=y_test,predictions=y_predicted_labels)
cm

import seaborn as sn
sn.heatmap(cm,annot=True)

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(100, activation='relu'),
    tf.keras.layers.Dense(10,activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(X_train, y_train, epochs=2)