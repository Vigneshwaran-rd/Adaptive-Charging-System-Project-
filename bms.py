# bms_test.py
import numpy as np
import tensorflow as tf
import joblib
import pandas as pd

# ----------------------------
# 1. Load Trained Model & Scaler
# ----------------------------
model = tf.keras.models.load_model("battery_model.h5", compile=False)
scaler = joblib.load("scaler.save")

# ----------------------------
# 2. Load Training Feature Ranges (for clipping)
# ----------------------------
data = pd.read_csv("battery.csv")
X_train = data[['SOH','SOC','Temperature']]
feature_min = X_train.min()
feature_max = X_train.max()

# ----------------------------
# 3. SOC Calculation Function
# ----------------------------
def calculate_soc(prev_soc, current, dt, capacity):
    soc_drop = (current * dt) / capacity * 100
    new_soc = prev_soc - soc_drop
    return max(0, min(100, new_soc))  # clamp between 0-100

# ----------------------------
# 4. SOH Calculation Function
# ----------------------------
def calculate_soh(cycle_count, degradation_rate=0.03):
    soh = 100 - (cycle_count * degradation_rate)
    return max(0, soh)

# ----------------------------
# 5. Example Sensor / Battery Inputs
# ----------------------------
temperature = 30           # °C
prev_soc = 80              # initial SOC %
current_measured = 1.5     # A
dt = 0.1                   # hours since last measurement
battery_capacity = 10      # Ah
cycle_count = 120          # total charge cycles

# ----------------------------
# 6. Calculate SOC & SOH
# ----------------------------
soc = calculate_soc(prev_soc, current_measured, dt, battery_capacity)
soh = calculate_soh(cycle_count)

print(f"Calculated SOC: {soc:.2f}%")
print(f"Calculated SOH: {soh:.2f}%")

# ----------------------------
# 7. Clip Values to Training Range
# ----------------------------
soh_clipped = np.clip(soh, feature_min['SOH'], feature_max['SOH'])
soc_clipped = np.clip(soc, feature_min['SOC'], feature_max['SOC'])
temperature_clipped = np.clip(temperature, feature_min['Temperature'], feature_max['Temperature'])

# ----------------------------
# 8. Prepare Input for Model
# ----------------------------
input_data = np.array([[soh_clipped, soc_clipped, temperature_clipped]])
input_scaled = scaler.transform(input_data)  # scale using saved scaler

print("Scaled input for model:", input_scaled)

# ----------------------------
# 9. Predict Voltage & Current
# ----------------------------
prediction = model.predict(input_scaled, verbose=0)

predicted_voltage = prediction[0][0]
predicted_current = prediction[0][1]

print(f"Predicted Voltage: {predicted_voltage:.2f} V")
print(f"Predicted Current: {predicted_current:.2f} A")