# Industrial IoT Project

**Author:** Bardia Asrari  
**Course:** Industrial IoT  
**University:** Università degli Studi di Messina

---

## 📑 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Verification](#verification)
- [Documentation](#documentation)
- [Artifacts](#artifacts)
- [Notes](#notes)
- [References](#references)

---

## 📝 Overview

This project demonstrates a simple Industrial IoT (IIoT) system integrating sensor simulation, MQTT-based communication, and a Node-RED dashboard for real-time monitoring and control. The project also includes formal verification of system properties using TLA+.

---

## 📁 Project Structure

Project/
├── docs/
│ ├── documentation.md
│ └── dashboard.png
├── node_red/
│ └── flows.json
├── src/
│ └── sensor_simulator.py
├── Verification/
│ ├── OfficeSpec.cfg
│ ├── OfficeSpec.tla
│ └── states/
├── .gitignore
├── README.md

text

---

## 🛠️ Technologies Used

- Python (for sensor simulation)
- Node-RED (for dashboard and flow orchestration)
- MQTT (Mosquitto broker)
- TLA+ (for formal verification)

---

## ⚙️ Installation

Install the required dependencies:

pip install paho-mqtt
npm install -g node-red node-red-dashboard

text

---

## 🚦 How to Run

1. **Start Mosquitto (MQTT Broker):**
    ```
    mosquitto -v
    ```
2. **Run the Sensor Simulator:**
    ```
    python src/sensor_simulator.py
    ```
3. **Start Node-RED:**
    ```
    node-red
    ```
    - Import the provided `node_red/flows.json` into your Node-RED instance.
4. **Access the Dashboard:**
    - Open your browser and go to [http://localhost:1880/ui](http://localhost:1880/ui)

---

## ✅ Verification

1. **Install Java 8+** (required for TLA+ tools).
2. **Run Model Checking:**
    ```
    cd Verification
    java -cp ../tla2tools.jar tlc2.TLC OfficeSpec.cfg
    ```

---

## 📚 Documentation

- See `docs/documentation.md` for a detailed explanation of the system, design choices, and usage instructions.
- Node-RED dashboard screenshot:  
  ![Dashboard Screenshot](docs/dashboard.png)

---

## 📦 Artifacts

| Artifact Type         | Path/Description                   |
|---------------------- |------------------------------------|
| Simulation Code       | `src/sensor_simulator.py`          |
| Node-RED Flows        | `node_red/flows.json`              |
| Formal Verification   | TLA+ specs in `Verification/`      |
| Documentation         | `docs/documentation.md`            |

---

## 📝 Notes

- Ensure all software is installed and running on compatible versions.
- The project is designed for reproducibility and can serve as a demonstrator or teaching material for IIoT concepts.
- For any issues or questions, please refer to the documentation or contact the project author.

---

## 🔗 References

- [Node-RED Documentation](https://nodered.org/docs/)
- [Paho MQTT Python](https://www.eclipse.org/paho/index.php?page=clients/python/index.php)
- [TLA+ Tools](https://lamport.azurewebsites.net/tla/tools.html)

---
