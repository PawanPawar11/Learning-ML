import numpy as np

# Sample data
area = np.array([500, 800, 1000, 1200, 1500])
price = np.array([25, 40, 50, 60, 75])

# Calculate slope (m)
m = (np.mean(area * price) - np.mean(area) * np.mean(price)) / \
    (np.mean(area * area) - np.mean(area) ** 2)

# Calculate intercept (b)
b = np.mean(price) - m * np.mean(area)

# Display equation
print("Linear Regression Equation:")
print(f"Price = {m:.2f} * Area + {b:.2f}")

# Predict price
new_area = 1100
predicted_price = m * new_area + b

print(f"Predicted price for {new_area} sq ft = ₹{predicted_price:.2f} lakhs")
