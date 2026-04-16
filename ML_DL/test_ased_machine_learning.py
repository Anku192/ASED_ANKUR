import numpy as np
import pandas as pd
import pickle

# Load dataset
df = pd.read_csv('/mnt/data/Housing.csv')

# Convert categorical to numeric
df = pd.get_dummies(df, drop_first=True)

# Features and target
X = df.drop('price', axis=1)
y = df['price']

# Train-test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train
model.fit(X_train, y_train)

# Save model + columns
pickle.dump(model, open('house_model.pkl', 'wb'))
pickle.dump(X.columns, open('model_columns.pkl', 'wb'))

print("Model trained and saved!")