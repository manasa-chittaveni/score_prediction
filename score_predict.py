import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("Datasets/students_scores.csv")

# Split into X (hours) and y (scores)
X = data[["Hours"]]
y = data["Scores"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict score for 8.5 hours of study
predicted_score = model.predict([[8.5]])
print(f"Predicted score for 8.5 hours of study: {predicted_score[0]:.2f}")

# Plot data and regression line
plt.scatter(X, y, color="blue", label="Actual scores")
plt.plot(X, model.predict(X), color="red", label="Regression line")
plt.xlabel("Hours Studied")
plt.ylabel("Scores")
plt.legend()
plt.show()
