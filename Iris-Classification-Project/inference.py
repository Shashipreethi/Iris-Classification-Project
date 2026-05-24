import joblib
import numpy as np

# Load saved model
model = joblib.load("models/best_iris_model.pkl")

# Example flower measurements
sample = np.array([
    [5.1, 3.5, 1.4, 0.2]
])

# Predict species
prediction = model.predict(sample)

print("Predicted Species:")
print(prediction[0])