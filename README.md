# 🚀 Industrial IoT Project

**👤 Student:** Bardia Asrari  
**📘 Course:** Industrial IoT  
**🏛️ University:** Università degli Studi di Messina  
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

yaml
Copy
Edit

---

## 🛠️ Installation

Install the required dependencies:

```bash
pip install paho-mqtt
npm install -g node-red node-red-dashboard
⚙️ How to Run
1. Start MQTT Broker (Mosquitto)
bash
Copy
Edit
mosquitto -v
2. Run the Sensor Simulator
bash
Copy
Edit
python src/sensor_simulator.py
3. Start Node-RED
bash
Copy
Edit
node-red
4. Import Flows into Node-RED
Import the file node_red/flows.json into your Node-RED editor.

5. Access the Dashboard
Open your browser and navigate to:

bash
Copy
Edit
http://localhost:1880/ui
🔍 Formal Verification (TLA+)
Requirements
Java 8 or later

TLA+ Tools

Run Model Checker
bash
Copy
Edit
cd Verification
java -cp ../tla2tools.jar tlc2.TLC OfficeSpec.cfg
📄 Documentation
For detailed explanations on system architecture, components, and instructions, see:

📘 docs/documentation.md

📦 Artifacts
Sensor Simulation Code: src/sensor_simulator.py
=======
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
>>>>>>> 7b015e96dfa264e887ced86643b7982220b4e2aa

---

TLA+ Verification Specs: Verification/

Project Documentation: docs/documentation.md

📝 Notes
Ensure all tools are correctly installed and compatible with your OS.

This project is designed for reproducibility and educational use.

For questions or issues, refer to the documentation or contact the author.
=======
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

Paho MQTT Python Client
=======
## 🔗 References

- [Node-RED Documentation](https://nodered.org/docs/)
- [Paho MQTT Python](https://www.eclipse.org/paho/index.php?page=clients/python/index.php)
- [TLA+ Tools](https://lamport.azurewebsites.net/tla/tools.html)

---
