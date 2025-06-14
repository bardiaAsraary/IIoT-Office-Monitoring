# 🚀 Industrial IoT Project

**👤 Student:** Bardia Asrari  
**📘 Course:** Industrial IoT  
**🏛️ University:** Università degli Studi di Messina  
---

## 📊 Dashboard Screenshot

![Dashboard](docs/dashboard.png)

---

## 🧾 Project Overview

This project demonstrates a simple **Industrial IoT (IIoT)** system that integrates:

- Sensor simulation via Python  
- MQTT-based communication  
- A Node-RED dashboard for real-time monitoring and control  
- Formal system property verification using **TLA+**

---

## 🗂️ Project Structure
```
Project/
├── docs/
│ ├── documentation.md # Detailed documentation
│ └── dashboard.png # Dashboard screenshot
├── node_red/
│ └── flows.json # Node-RED flow definitions
├── src/
│ └── sensor_simulator.py # Sensor simulation script
├── Verification/
│ ├── OfficeSpec.cfg # TLA+ configuration
│ ├── OfficeSpec.tla # TLA+ specification
│ └── states/ # TLC generated states
├── .gitignore
├── README.md
```
---

## 🛠️ Installation

Install the required dependencies:

```
pip install paho-mqtt
npm install -g node-red node-red-dashboard
```
## ⚙️ How to Run

1. Start MQTT Broker (Mosquitto)
```
net start mosquitto
```
2. Run the Sensor Simulator
```
python src/sensor_simulator.py
```
3. Start Node-RED
```
node-red
```
4. Import Flows into Node-RED

Import the file node_red/flows.json into your Node-RED editor.

5. Access the Dashboard

Open your browser and navigate to:
```
http://127.0.0.1:1880/
```
## 🔍 Formal Verification (TLA+)
### Requirements

Java 8 or later

TLA+ Tools

Run Model Checker
```
cd Verification
java -cp ../tla2tools.jar tlc2.TLC OfficeSpec.cfg
```
### 📄 Documentation
For detailed explanations on system architecture, components, and instructions, see:

📘 docs/documentation.md

### 📦 Artifacts

Sensor Simulation Code: src/sensor_simulator.py
---

## 🛠️ Technologies Used

- Python (for sensor simulation)
- Node-RED (for dashboard and flow orchestration)
- MQTT (Mosquitto broker)
- TLA+ (for formal verification)

---

## ⚙️ Installation

Install the required dependencies:
```
pip install paho-mqtt
npm install -g node-red node-red-dashboard
```
---
## ✅ Verification

1. **Install Java 8+** (required for TLA+ tools).
2. **Run Model Checking:**

    ```
    cd Verification
    java -cp ../tla2tools.jar tlc2.TLC OfficeSpec.cfg
---

Project Documentation: docs/documentation.md

## 📦 Artifacts

| Artifact Type         | Path/Description                   |
|---------------------- |------------------------------------|
| Simulation Code       | `src/sensor_simulator.py`          |
| Node-RED Flows        | `node_red/flows.json`              |
| Formal Verification   | TLA+ specs in `Verification/`      |
| Documentation         | `docs/documentation.md`            |
---


## 🔗 References

- [Node-RED Documentation](https://nodered.org/docs/)
- [Paho MQTT Python](https://www.eclipse.org/paho/index.php?page=clients/python/index.php)
- [TLA+ Tools](https://lamport.azurewebsites.net/tla/tools.html)

---
