import numpy as np
from keras.models import load_model

# -------------------------------
# 🔹 LOAD MODELS
# -------------------------------
model1 = load_model("dl_model_regression.h5")
model2 = load_model("dl_model_classification.h5")
model3 = load_model("dl_model_diabetes.h5")


# -------------------------------
# 🔹 TEST MODEL 1 (Regression)
# -------------------------------
x_test = np.array([[12.0]])
pred1 = model1.predict(x_test)

print("Regression Prediction (Expected ~24):", pred1[0][0])


# -------------------------------
# 🔹 TEST MODEL 2 (Classification)
# -------------------------------
x_test2 = np.array([[55]])
pred2 = model2.predict(x_test2)

print("Classification Raw Output:", pred2[0][0])

# Convert to class (0 or 1)
class_result = 1 if pred2[0][0] > 0.5 else 0
print("Predicted Class:", class_result)


# -------------------------------
# 🔹 TEST MODEL 3 (Diabetes)
# -------------------------------
x_test3 = np.array([[45, 63]])  # Must match dataset features
pred3 = model3.predict(x_test3)

print("Diabetes Raw Output:", pred3[0][0])

# Convert to class
diabetes_result = 1 if pred3[0][0] > 0.5 else 0
print("Diabetes Prediction:", diabetes_result)