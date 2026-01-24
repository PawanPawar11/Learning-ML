import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

area = np.array([400, 500, 650, 800, 1000, 1200, 1500, 1800]).reshape(-1, 1)
price = np.array([20, 25, 32, 40, 50, 60, 75, 90])

X_train, X_test, y_train, y_test = train_test_split(
    area, price, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("MSE:", mean_squared_error(y_test, y_pred))
print("R²:", r2_score(y_test, y_pred))

new_area = np.array([[1100]])
print("Predicted price:", model.predict(new_area)[0])
