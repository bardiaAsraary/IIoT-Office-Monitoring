# 🏭 Industrial IoT Monitoring System with Secure WAMP Communication

![Dashboard](docs/dashboard.png)


## 📌 Overview
A **secure industrial IoT monitoring system** featuring:
- ✅ RISC-V MCU emulation with Renode
- ✅ End-to-end TLS 1.2 encryption
- ✅ Real-time dashboard (Node-RED)
- ✅ Certificate-based device authentication

---

## 🚀 Quick Start
### Prerequisites
```bash
# Ubuntu/Debian (Linux/macOS/WSL)
sudo apt update && sudo apt install -y \
    git python3-pip build-essential \
    libssl-dev cmake gcc-riscv64-unknown-elf
```

## Clone & Setup
```
git clone https://github.com/your-username/industrial-iot-wamp.git
cd industrial-iot-wamp
```

## 🛠️ Step-by-Step Setup
1. Hardware Emulation (Renode)
What it does: Emulates the RISC-V HiFive1 board.
```
# Download and install Renode
wget https://dl.antmicro.com/projects/renode/builds/renode-latest.linux-portable.tar.gz
tar -xzf renode-latest.linux-portable.tar.gz

# Start Renode and load the board
./renode/renode
```

In Renode CLI:

```
mach create "HiFive1"
machine LoadPlatformDescription @platforms/cpus/sifive-hifive1.repl
```

## 2. WAMP Router Setup

What it does: Handles secure communication between devices.

```
pip install autobahn[twisted,serialization,encryption]

# Start the router (edit paths to your certs)
python3 wamp_router/router.py \
    --tlscert certs/server-cert.pem \
    --tlskey certs/server-key.pem \
    --cacert certs/ca-cert.pem
```

## 3. Generate Certificates

Why? Ensures all devices authenticate via TLS.
```
# Generate Certificate Authority (CA)
openssl req -x509 -newkey rsa:4096 -sha384 -nodes \
    -keyout certs/ca-key.pem -out certs/ca-cert.pem \
    -days 365 -subj "/CN=IoT-CA"

# Server Certificate (for WAMP router)
openssl req -newkey rsa:2048 -nodes -keyout certs/server-key.pem \
    -out certs/server-req.pem -subj "/CN=localhost"
openssl x509 -req -in certs/server-req.pem -CA certs/ca-cert.pem \
    -CAkey certs/ca-key.pem -CAcreateserial -out certs/server-cert.pem

# Client Certificate (for MCU)
openssl req -newkey rsa:2048 -nodes -keyout certs/client-key.pem \
    -out certs/client-req.pem -subj "/CN=HiFive1"
openssl x509 -req -in certs/client-req.pem -CA certs/ca-cert.pem \
    -CAkey certs/ca-key.pem -out certs/client-cert.pem -days 365 -sha384
```

## 4. Flash Firmware to Emulated MCU
What it does: Runs the sensor monitoring code on the RISC-V emulator.

```
cd firmware
make clean all  # Builds firmware using riscv-gcc

# In Renode monitor:
(monitor) sysbus LoadELF @build/sensor_app.elf
(monitor) start
```

## 5. Launch Node-RED Dashboard

What it shows: Real-time sensor data visualization.

```
npm install -g --unsafe-perm node-red
npm install node-red-contrib-wamp  # WAMP plugin

node-red flows/dashboard.json  # Start dashboard
```
👉 Access at: http://localhost:1880/ui

## 📂 Project Structure
```
industrial-iot-wamp/
├── firmware/          # RISC-V C code and Makefile
├── wamp_router/       # Python WAMP router code
├── certs/             # X.509 certificates
├── flows/             # Node-RED dashboard config
├── docs/              # Diagrams/screenshots
└── scripts/           # Helper scripts (optional)
```