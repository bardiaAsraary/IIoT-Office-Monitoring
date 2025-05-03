Industrial IoT Project
Student: Bardia Asrari
Course: Industrial IoT
University: Università degli Studi di Messina

📊 Dashboard Screenshot
![Dashboard](scree 🚀 Project Overview

This project demonstrates a simple Industrial IoT (IIoT) system integrating sensor simulation, MQTT-based communication, and a Node-RED dashboard for real-time monitoring and control. The project also includes formal verification of system properties using TLA+.

🗂️ Project Structure
text
Project/
├── docs/
│   ├── documentation.md
│   └── dashboard.png
├── node_red/
│   └── flows.json
├── src/
│   └── sensor_simulator.py
├── Verification/
│   ├── OfficeSpec.cfg
│   ├── OfficeSpec.tla
│   └── states/
├── .gitignore
├── README.md
🛠️ Installation
Install the required dependencies:

bash
pip install paho-mqtt
npm install -g node-red node-red-dashboard
⚙️ How to Run
Start Mosquitto (MQTT Broker):

bash
mosquitto -v
Run the Sensor Simulator:

bash
python src/sensor_simulator.py
Start Node-RED:

bash
node-red
Import the provided node_red/flows.json into your Node-RED instance.

Access the Dashboard:

Open your browser and navigate to http://localhost:1880/ui to view the dashboard.

🔍 Verification
Install Java 8+ (required for TLA+ tools).

Run Model Checking:

bash
cd Verification
java -cp ../tla2tools.jar tlc2.TLC OfficeSpec.cfg
📄 Documentation
See docs/documentation.md for a detailed explanation of the system, design choices, and usage instructions.

The Node-RED dashboard screenshot is available at docs/dashboard.png.

📦 Artifacts
Simulation Code: src/sensor_simulator.py

Node-RED Flows: node_red/flows.json

Formal Verification: TLA+ specs in Verification/

Documentation: docs/documentation.md

📝 Notes
Ensure all software is installed and running on compatible versions.

The project is designed for reproducibility and can serve as a demonstrator or teaching material for IIoT concepts.

For any issues or questions, please refer to the documentation or contact the project author.

📚 References
Node-RED Documentation

Paho MQTT Python

TLA+ Tools