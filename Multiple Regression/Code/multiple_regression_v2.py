import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

# Create dataset
data = {
    "StudyHours": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "Attendance": [60, 65, 70, 72, 75, 80, 85, 88, 90, 95],
    "Marks": [35, 40, 45, 50, 55, 65, 70, 75, 85, 90]
}

df = pd.DataFrame(data)

# Independent variables (X)
X = df[["StudyHours", "Attendance"]]

# Dependent variable (y)
y = df["Marks"]

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print("R² Score:", r2)
print("Mean Absolute Error:", mae)

# Coefficients
print("\nIntercept:", model.intercept_)
print("Coefficients:", model.coef_)

# Predict for a new student
new_data = pd.DataFrame({
    "StudyHours": [7],
    "Attendance": [82]
}) # 7 study hours, 82% attendance

predicted_marks = model.predict(new_data)

print("\nPredicted Marks:", predicted_marks[0])

# Visualization
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Marks")
plt.ylabel("Predicted Marks")
plt.title("Actual vs Predicted Marks")
plt.show()