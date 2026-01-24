import numpy as np

area = np.array([500, 800, 1000, 1200, 1500])
price = np.array([25, 40, 50, 60, 75])

# Fit a straight line (degree = 1)
m, b = np.polyfit(area, price, 1)

print(f"Price = {m:.2f} * Area + {b:.2f}")

# Predict price
new_area = 1100
predicted_price = m * new_area + b

print(f"Predicted price for {new_area} sq ft = ₹{predicted_price:.2f} lakhs")
