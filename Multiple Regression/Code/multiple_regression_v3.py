import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    root_mean_squared_error
)

# Dataset
data = {
    "StudyHours": [2,3,4,5,6,7,8,9,10,11,12,13],
    "Attendance": [60,65,68,70,74,78,82,85,88,90,93,95],
    "Assignments": [4,5,5,6,6,7,7,8,8,9,9,10],
    "Marks": [35,40,42,50,55,62,68,72,80,85,90,95]
}

df = pd.DataFrame(data)

# Display dataset
print("Dataset:")
print(df.head())

# Features
X = df[["StudyHours", "Attendance", "Assignments"]]

# Target
y = df["Marks"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Metrics
print("\nModel Evaluation")
print("R² Score:", r2_score(y_test, y_pred))
print("MAE:", mean_absolute_error(y_test, y_pred))
print("RMSE:", root_mean_squared_error(y_test, y_pred))

# Model parameters
print("\nIntercept:")
print(model.intercept_)

print("\nCoefficients:")
for feature, coef in zip(X.columns, model.coef_):
    print(feature, ":", coef)

# Compare actual vs predicted
comparison = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": y_pred
})

print("\nActual vs Predicted")
print(comparison)

# Predict new student's marks
new_student = pd.DataFrame({
    "StudyHours": [8],
    "Attendance": [85],
    "Assignments": [8]
})

predicted_marks = model.predict(new_student)

print("\nPredicted Marks for New Student:")
print(predicted_marks[0])

# Visualization
plt.figure(figsize=(7,5))
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Marks")
plt.ylabel("Predicted Marks")
plt.title("Actual vs Predicted Marks")
plt.grid(True)
plt.show()