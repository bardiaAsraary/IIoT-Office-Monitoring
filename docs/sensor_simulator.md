Overview
The Sensor Simulator is a Python script that generates and publishes simulated environmental sensor data (temperature, humidity, light, occupancy) for various office zones. It uses MQTT to send data, making it ideal for testing IoT dashboards or pipelines, such as the Node-RED dashboard in this project.

🚀 Features
Simulates multiple office zones (e.g., reception, workspace, meeting)

Publishes realistic random sensor data

Publishes to MQTT topics at regular intervals

Configurable via a JSON settings file

Graceful shutdown on keyboard interrupt

⚙️ Configuration
The simulator reads its settings from .vscode/settings.json.

Example configuration
json
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
  }
}
Key	Description
broker	MQTT broker address (e.g., localhost)
port	MQTT broker port (default: 1883)
client_id	MQTT client identifier
zones	List of simulated office zones
publish_interval_seconds	Time in seconds between data publications
topics_format	MQTT topic format string (e.g., office/{zone}/data)
sensor_ranges	Min/max values for each sensor type
🔍 How It Works
Loads configuration from .vscode/settings.json.

Connects to the MQTT broker using the Paho MQTT client.

Simulates sensor data for each zone:

Temperature: 20–25°C

Humidity: 40–70%

Light: 0–1000 lux

Occupancy: 0 or 1 (absent/present)

Publishes data to topics like office/reception/data.

Repeats at the configured interval until interrupted.

▶️ Usage
1. Install Dependencies
bash
pip install paho-mqtt
2. Configure the Simulator
Edit .vscode/settings.json as needed (see above).

3. Run the Simulator
bash
python src/sensor_simulator.py
4. Stop the Simulator
Press <kbd>Ctrl</kbd> + <kbd>C</kbd> to gracefully stop the simulator.

📋 Example Output
text
✅ Successfully connected to MQTT broker
📤 Published to office/reception/data: {'temperature': 22.1, 'humidity': 55.3, 'light': 812, 'occupancy': 1}
📤 Published to office/workspace/data: {'temperature': 21.7, 'humidity': 44.2, 'light': 533, 'occupancy': 0}
...
🛑 Shutting down sensor simulator...
<details> <summary>⚙️ Customization</summary>
Add/Remove zones: Edit the zones list in the config file.

Change sensor ranges: Modify sensor_ranges values.

Adjust publish interval: Change publish_interval_seconds.

Change MQTT topic format: Edit topics_format.

</details> <details> <summary>🛠️ Troubleshooting</summary>
Connection failed: Ensure the MQTT broker is running and accessible.

Import errors: Install all dependencies (pip install paho-mqtt).

Configuration errors: Verify .vscode/settings.json for typos or missing fields.

</details>
📂 Source Code
The simulator script is located at:
src/sensor_simulator.py