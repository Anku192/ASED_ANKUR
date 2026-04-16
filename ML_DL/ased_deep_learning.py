import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Input

# -------------------------------
# 🔹 MODEL 1: REGRESSION (y = 2x)
# -------------------------------
x1 = np.array([[4],[5],[6],[7],[8],[9],[10]])
y1 = np.array([8,10,12,14,16,18,20])

model1 = Sequential()
model1.add(Input(shape=(1,)))
model1.add(Dense(100, activation="relu"))
model1.add(Dense(50, activation="relu"))
model1.add(Dense(1))

model1.compile(loss="mean_squared_error", optimizer="adam")
model1.fit(x1, y1, epochs=200)

model1.save("dl_model_regression.h5")


# -------------------------------
# 🔹 MODEL 2: BINARY CLASSIFICATION
# -------------------------------
X2 = np.array([[30],[40],[50],[60],[20],[10],[70]])
y2 = np.array([0,1,1,1,0,0,1])

model2 = Sequential()
model2.add(Input(shape=(1,)))
model2.add(Dense(100, activation='relu'))
model2.add(Dense(50, activation='relu'))
model2.add(Dense(1, activation='sigmoid'))

model2.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model2.fit(X2, y2, epochs=100)

model2.save("dl_model_classification.h5")


# -------------------------------
# 🔹 MODEL 3: DIABETES DATASET
# -------------------------------
df = pd.read_csv("NBD.csv")

X3 = df.drop('diabetes', axis=1)
y3 = df['diabetes']

model3 = Sequential()
model3.add(Input(shape=(X3.shape[1],)))
model3.add(Dense(100, activation='relu'))
model3.add(Dense(50, activation='relu'))
model3.add(Dense(1, activation='sigmoid'))

model3.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model3.fit(X3, y3, epochs=100)

model3.save("dl_model_diabetes.h5")

print("All models trained and saved!")