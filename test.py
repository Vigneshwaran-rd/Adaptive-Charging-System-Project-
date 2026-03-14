import numpy as np
import tensorflow as tf
import joblib

# Load scaler
scaler = joblib.load("scaler.save")

# Load trained model
model = tf.keras.models.load_model("battery_model.h5", compile=False)

# Example input: SOH, SOC, Temperature
input_data = np.array([[0.9, 0.7, 30]])

# Normalize input (same as training)
input_scaled = scaler.transform(input_data)

# Predict
prediction = model.predict(input_scaled)

print("Predicted Voltage:", prediction[0][0])
print("Predicted Current:", prediction[0][1])