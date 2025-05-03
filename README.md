## 🛠️ Installation
```bash
pip install paho-mqtt
npm install -g node-red node-red-dashboard
```

## 🔍 Verification
1. Install Java 8+
2. Run model checking:
```bash
cd verification
java -cp ../tla2tools.jar tlc2.TLC OfficeSpec.cfg
```