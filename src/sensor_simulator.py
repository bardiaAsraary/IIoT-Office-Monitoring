import random
import time
import paho.mqtt.client as mqtt
import json

broker = "localhost"
client_id = "OfficeSimulator"

# Initialize client with MQTTv2 API
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id)

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("✅ Successfully connected to MQTT broker")
    else:
        print(f"❌ Connection failed: {reason_code}")

def simulate_sensors():
    zones = ["reception", "workspace", "meeting"]
    try:
        while True:
            for zone in zones:
                data = {
                    "temperature": round(20 + 5 * random.random(), 1),
                    "humidity": round(40 + 30 * random.random(), 1),
                    "light": random.randint(0, 1000),
                    "occupancy": random.choice([0, 1])
                }
                client.publish(f"office/{zone}/data", json.dumps(data))
                print(f"📤 Published to office/{zone}/data: {data}")
            time.sleep(10)
    except KeyboardInterrupt:
        print("\n🛑 Shutting down sensor simulator...")
        client.disconnect()

if __name__ == "__main__":
    client.on_connect = on_connect
    client.connect(broker, 1883, 60)  # Explicit port and timeout
    client.loop_start()
    simulate_sensors()