# Adaptive Charging System Project

## Overview
The **Adaptive Charging System** is a smart battery management solution designed to improve battery safety, efficiency, and lifespan. The system continuously monitors battery parameters such as **State of Charge (SOC), State of Health (SOH), voltage, current, and temperature**, and adapts the charging process accordingly.

This project uses an **ESP32 microcontroller and sensor modules** to collect real-time battery data and apply intelligent charging control.

---

## Objectives
- Monitor important battery parameters in real time
- Improve battery lifespan through adaptive charging
- Prevent battery overheating and overcharging
- Display battery information such as SOC, SOH, and temperature
- Implement edge-based battery monitoring

---

## System Architecture
The system consists of the following components:

- ESP32 Microcontroller
- INA219 Current and Voltage Sensor
- Temperature Sensor (DS18B20)
- LCD Display
- Battery Source
- Charging Control Logic

Sensors collect battery data and send it to the ESP32 for processing. The system calculates SOC and SOH and displays the values on the LCD.

---

## Hardware Components

| Component | Purpose |
|-----------|---------|
| ESP32 | Main controller for processing and communication |
| INA219 | Measures voltage and current |
| DS18B20 | Measures battery temperature |
| LCD Display | Displays SOC, SOH, and temperature |
| Battery | Energy storage system |
| Charging Circuit | Controls charging behavior |

---

## Software Requirements
- Arduino IDE
- ESP32 Board Package

### Required Libraries
- Wire
- Adafruit INA219
- OneWire
- DallasTemperature
- LiquidCrystal_I2C

---

## Features
- Real-time battery monitoring
- SOC (State of Charge) calculation
- SOH (State of Health) estimation
- Temperature monitoring
- Adaptive charging control
- LCD display for live battery data

---

## Working Principle
1. The INA219 sensor measures battery voltage and current.
2. The DS18B20 sensor measures battery temperature.
3. The ESP32 processes the collected data.
4. SOC and SOH values are calculated.
5. The system adapts charging based on battery condition.
6. Battery data is displayed on the LCD screen.

---

## Applications
- Electric Vehicles
- Energy Storage Systems
- Smart Battery Chargers
- Portable Electronic Devices
- Renewable Energy Systems

---



---

## License
This project is developed for educational and research purposes.
