
"""
Simple ML model using sklearn
"""

from sklearn import model_selection
from sklearn import linear_model

# data
x = [[10], [7], [5], [8]]
y = [20, 14, 10, 16]

# split data
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y)

# model
model = linear_model.LinearRegression()
model.fit(x_train, y_train)

# prediction
pred = model.predict(x_test)

print(f"Predictions: {pred}")

