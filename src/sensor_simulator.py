import random
import time
import paho.mqtt.client as mqtt
import json

broker = "localhost"
client_id = "OfficeSimulator"

# Initialize client with callback API version
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, client_id)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Successfully connected to MQTT broker")
    else:
        print(f"Connection failed with code {rc}")

def simulate_sensors():
    zones = ["reception", "workspace", "meeting"]
    try:
        while True:
            for zone in zones:
                # Generate realistic office data
                data = {
                    "temperature": round(20 + 5 * random.random(), 1),
                    "humidity": round(40 + 30 * random.random(), 1),
                    "light": random.randint(0, 1000),
                    "occupancy": random.choice([0, 1])
                }
                
                # Publish to MQTT
                client.publish(f"office/{zone}/data", json.dumps(data))
                print(f"Published to office/{zone}/data: {data}")
            
            time.sleep(10)  # 10-second update interval
    except KeyboardInterrupt:
        print("\nShutting down sensor simulator...")
        client.disconnect()

if __name__ == "__main__":
    # Set up callback
    client.on_connect = on_connect
    
    # Connect to broker
    try:
        client.connect(broker)
        client.loop_start()
        simulate_sensors()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.loop_stop()