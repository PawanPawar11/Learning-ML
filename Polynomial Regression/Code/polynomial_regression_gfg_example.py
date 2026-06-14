import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Load dataset
datas = pd.read_csv("data.csv")

# Feature and target variables
X = datas.iloc[:, 1:2].values
y = datas.iloc[:, 2].values

# ---------------------------
# Linear Regression
# ---------------------------
lin = LinearRegression()
lin.fit(X, y)

# ---------------------------
# Polynomial Regression
# ---------------------------
poly = PolynomialFeatures(degree=4)

X_poly = poly.fit_transform(X)

lin2 = LinearRegression()
lin2.fit(X_poly, y)

# ---------------------------
# Linear Regression Graph
# ---------------------------
plt.scatter(X, y, color="blue")
plt.plot(X, lin.predict(X), color="red")

plt.title("Linear Regression")
plt.xlabel("Temperature")
plt.ylabel("Pressure")

plt.show()

# ---------------------------
# Polynomial Regression Graph
# ---------------------------
plt.scatter(X, y, color="blue")
plt.plot(
    X,
    lin2.predict(poly.fit_transform(X)),
    color="red"
)

plt.title("Polynomial Regression")
plt.xlabel("Temperature")
plt.ylabel("Pressure")

plt.show()

# ---------------------------
# Linear Regression Prediction
# ---------------------------
pred = 110.0
predarray = np.array([[pred]])

linear_prediction = lin.predict(predarray)
print("Linear Prediction:", linear_prediction)

# ---------------------------
# Polynomial Regression Prediction
# ---------------------------
pred2 = 110.0
pred2array = np.array([[pred2]])

poly_prediction = lin2.predict(
    poly.fit_transform(pred2array)
)

print("Polynomial Prediction:", poly_prediction)