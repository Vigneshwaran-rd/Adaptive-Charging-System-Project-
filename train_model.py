import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import joblib

# ----------------------------
# 1. Load Dataset
# ----------------------------
data = pd.read_csv("battery.csv")

# Inputs (Features)
X = data[['SOH', 'SOC', 'Temperature']]

# Outputs (Targets)
y = data[['Voltage', 'Current']]

# ----------------------------
# 2. Normalize Input Data
# ----------------------------
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Save scaler (needed later in ESP32)
joblib.dump(scaler, "scaler.save")

# ----------------------------
# 3. Split Data
# ----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# ----------------------------
# 4. Build Small Neural Network
# ----------------------------
model = tf.keras.Sequential([
    tf.keras.layers.Dense(8, activation='relu', input_shape=(3,)),
    tf.keras.layers.Dense(4, activation='relu'),
    tf.keras.layers.Dense(2)
])

# ----------------------------
# 5. Compile Model
# ----------------------------
model.compile(
    optimizer='adam',
    loss='mse',
    metrics=['mae']
)

# ----------------------------
# 6. Train Model
# ----------------------------
model.fit(X_train, y_train, epochs=100, batch_size=16)

# ----------------------------
# 7. Evaluate Model
# ----------------------------
loss, mae = model.evaluate(X_test, y_test)
print("Test Loss:", loss)
print("Test MAE:", mae)

# ----------------------------
# 8. Save Model
# ----------------------------
model.save("battery_model.h5")

# ----------------------------
# 9. Convert to TFLite
# ----------------------------
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()

with open("battery_model.tflite", "wb") as f:
    f.write(tflite_model)

print("Training and conversion completed successfully.")