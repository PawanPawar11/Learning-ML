from sklearn.linear_model import LinearRegression
import numpy as np

area = np.array([500, 800, 1000, 1200, 1500]).reshape(-1, 1)
price = np.array([25, 40, 50, 60, 75])

model = LinearRegression()
model.fit(area, price)

m = model.coef_[0]
b = model.intercept_

print(f"Price = {m:.2f} * Area + {b:.2f}")

new_area = np.array([[1100]])
predicted_price = model.predict(new_area)

print(f"Predicted price for 1100 sq ft = ₹{predicted_price[0]:.2f} lakhs")
