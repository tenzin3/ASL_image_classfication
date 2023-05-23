# -*- coding: utf-8 -*-
"""Basic_without_dropout.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14n4ynWOgWGuFEB71H2QJmMnRtxQft8K6

## Project Hand Sign

# Importing
"""

import numpy as np 
import pandas as pd 
import tensorflow as tf

tf.__version__

"""# Importing data sets"""

train_dataset = pd.read_csv("sign_mnist_train.csv")
test_dataset = pd.read_csv("sign_mnist_test.csv")

"""# Training and Test DataSet

**Training DataSet**
"""

train_dataset.head()

"""# Train and Test Set Extraction

"""

X_train = train_dataset.iloc[:,1:]
Y_train = train_dataset.iloc[:,0]

X_test = test_dataset.iloc[:,1:]
Y_test = test_dataset.iloc[:,0]

"""# Normalisation

"""

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

X_train/=255
X_test/=255

"""# Reshaping for Cov2d Input"""

X_train = np.array(X_train)
X_test = np.array(X_test)

X_train= X_train.reshape(X_train.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)

"""# Training and Test Data Sets

**X Train**
"""

print("X_Train-> "+str(list(X_train.shape)))
print("Y_Train-> "+str(list(Y_train.shape)))

print("X_Test->  "+str(list(X_test.shape)))
print("Y_test->  "+str(list(Y_test.shape)))

"""# Encoding the labels"""

from keras.utils import to_categorical 
Y_train = to_categorical(Y_train, dtype ="uint8") 
Y_test = to_categorical(Y_test, dtype ="uint8")

"""# Data Augmentation

**Not needed because of Large number of dataset**

# CNN model

# Initialising
"""

cnn = tf.keras.models.Sequential()

"""Convulation Layer"""

cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=6, activation='relu', input_shape=[28, 28, 1]))

"""Pooling"""

cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

"""2nd Convulation Layer"""

cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=6, activation='relu'))

"""2nd Pooling

"""

cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

"""Flatten"""

cnn.add(tf.keras.layers.Flatten())

"""Dropout"""

cnn.add(tf.keras.layers.Dropout(0.5))

"""Full Connection"""

cnn.add(tf.keras.layers.Dense(units=128, activation='relu'))

"""Output Layer"""

cnn.add(tf.keras.layers.Dense(units=25, activation='sigmoid'))

"""# Model Summary"""

cnn.summary()

"""# Compiling the model"""

cnn.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics=['accuracy'])

"""# Training the model on Training Set"""

history =cnn.fit(X_train, Y_train,validation_data=(X_test, Y_test) ,batch_size = 32, epochs = 20)

"""# Graph for Train and Test Set"""

import matplotlib.pyplot as plt

# list all data in history
print(history.history.keys())

#Epoch
last_epoch=20-1



# summarize history for accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
Title_Output_Accuracy=" Training="+str(round(history.history['accuracy'][last_epoch],3))+" Validation="+str(round(history.history['val_accuracy'][last_epoch],3));
plt.title("model accuracy: "+Title_Output_Accuracy)
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()


# summarize history for loss

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
Title_Output_Loss=" Training="+str(round(history.history['loss'][last_epoch],3))+" Validation="+str(round(history.history['val_loss'][last_epoch],3));
plt.title('model loss: '+Title_Output_Loss)
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

"""# Accuracy per classes"""

from sklearn.metrics import classification_report
import numpy as np

Y_test = np.argmax(Y_test, axis=1) # Convert one-hot to index
Y_pred = cnn.predict_classes(X_test)
print(classification_report(Y_test, Y_pred))

"""#Video Capture"""

