import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

# Sample dataset
data = {
    "Years": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Salary": [45, 50, 60, 80, 110, 150, 200, 260, 330, 410]
}

df = pd.DataFrame(data)

# Features and target
X = df[["Years"]]
y = df["Salary"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Convert X into polynomial features
poly = PolynomialFeatures(degree=2)

X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Train model
model = LinearRegression()
model.fit(X_train_poly, y_train)

# Predictions
y_pred = model.predict(X_test_poly)

# Evaluation
print("R² Score:", r2_score(y_test, y_pred))
print("MAE:", mean_absolute_error(y_test, y_pred))

# Coefficients
print("\nIntercept:", model.intercept_)
print("Coefficients:", model.coef_)

# Visualization
X_curve = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
X_curve_poly = poly.transform(X_curve)

y_curve = model.predict(X_curve_poly)

plt.scatter(X, y, label="Actual Data")
plt.plot(X_curve, y_curve, label="Polynomial Curve")
plt.xlabel("Years")
plt.ylabel("Salary")
plt.title("Polynomial Regression")
plt.legend()
plt.show()