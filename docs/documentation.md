# Overview

The Sensor Simulator is a Python script that simulates environmental sensors (temperature, humidity, light, and occupancy) for different office zones. It publishes sensor data to an MQTT broker at configurable intervals, making it useful for testing IoT platforms, dashboards, or data pipelines.

---

## Features

- Simulates multiple zones (e.g., reception, workspace, meeting)
- Publishes random but realistic sensor data:
  - Temperature
  - Humidity
  - Light
  - Occupancy
- MQTT integration using the `paho-mqtt` library
- Configurable via a JSON settings file
- Graceful shutdown on keyboard interrupt

---

## Prerequisites

- Python 3.x
- `paho-mqtt` library

```bash
pip install paho-mqtt
```

A running MQTT broker (e.g., Mosquitto)
Configuration file: .vscode/settings.json
---
## Configuration

The simulator reads its settings from .vscode/settings.json.
### Example Configuration

```
{
  "broker": "localhost",
  "port": 1883,
  "client_id": "OfficeSimulator",
  "zones": ["reception", "workspace", "meeting"],
  "publish_interval_seconds": 10,
  "topics_format": "office/{zone}/data",
  "sensor_ranges": {
    "temperature": [15, 30],
    "humidity": [30, 70],
    "light": [0, 1000],
    "occupancy": [0, 1]
  },
  "tlaplus": {
    "modelChecker": {}
  }
}
```
---
## Key Settings

broker: MQTT broker address

port: MQTT broker port (default: 1883)

client_id: MQTT client identifier

zones: List of office zones to simulate

publish_interval_seconds: Time between data publications

topics_format: MQTT topic format for publishing

sensor_ranges: Value ranges for each sensor type
---
## Usage

### Install Dependencies
```
pip install paho-mqtt
```
### Configure the simulator

Edit .vscode/settings.json with your desired settings.

### Run the simulator
```
python sensor_simulator.py
```
### Stopping the simulator

Press Ctrl+C to gracefully shut down.
---
## Code Structure

Configuration loading: Reads settings from .vscode/settings.json

MQTT Client: Initializes and connects to the broker

Sensor Simulation: Generates random sensor values for each zone and publishes them to MQTT topics

Graceful Shutdown: Handles keyboard interrupts to disconnect cleanly
---
## Example Output

✅ Successfully connected to MQTT broker
📤 Published to office/reception/data: {'temperature': 22.4, 'humidity': 58.2, 'light': 721, 'occupancy': 1}
📤 Published to office/workspace/data: {'temperature': 20.1, 'humidity': 42.7, 'light': 500, 'occupancy': 0}
...
🛑 Shutting down sensor simulator...

---
## Customization

Add or remove zones in the configuration file

Adjust sensor ranges for more realistic or extreme values

Change publishing intervals to simulate faster or slower environments

Modify topic format to match your MQTT topic structure

## Troubleshooting

Connection failed: Ensure your MQTT broker is running and accessible

Import errors: Make sure all dependencies are installed

Configuration errors: Double-check your .vscode/settings.json for typos or missing fields