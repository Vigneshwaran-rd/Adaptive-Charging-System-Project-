import scipy.io
import pandas as pd
import numpy as np

mat = scipy.io.loadmat("B0005.mat")

battery = mat['B0005'][0,0]

cycles = battery['cycle'][0]

rows = []
initial_capacity = None

for cycle in cycles:

    cycle_type = cycle['type'][0]

    if cycle_type == 'discharge':

        data = cycle['data'][0,0]

        voltage = data['Voltage_measured'][0]
        current = data['Current_measured'][0]
        temperature = data['Temperature_measured'][0]
        capacity = data['Capacity'][0,0]

        if initial_capacity is None:
            initial_capacity = capacity

        soh = capacity / initial_capacity

        soc = (voltage - np.min(voltage)) / (np.max(voltage) - np.min(voltage))

        for i in range(len(voltage)):
            rows.append([
                soh,
                soc[i],
                temperature[i],
                voltage[i],
                current[i]
            ])

df = pd.DataFrame(rows, columns=[
    "SOH", "SOC", "Temperature", "Voltage", "Current"
])

df.to_csv("battery.csv", index=False)

print("Conversion completed successfully.")