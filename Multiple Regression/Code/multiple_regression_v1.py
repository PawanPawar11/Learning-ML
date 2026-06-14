from sklearn.linear_model import LinearRegression

# Input features
# [Study Hours, Attendance]
X = [
    [2, 60],
    [4, 70],
    [6, 80],
    [8, 90],
    [10, 95]
]

# Output (Marks)
y = [40, 50, 60, 75, 90]

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict marks for:
# Study Hours = 7
# Attendance = 85
prediction = model.predict([[7, 85]])

print("Predicted Marks:", prediction[0])