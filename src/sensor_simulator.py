import paho.mqtt.client as mqtt
import ssl
import time
import random


# Broker Configuration
BROKER_ADDRESS = "localhost"
PORT = 8884
TOPIC = "sensor/temperature"

# TLS Certificate Paths
CA_CERT = "certs/ca.crt"
CLIENT_CERT = "certs/client-cert.pem"
CLIENT_KEY = "certs/client-key.pem"

# Create MQTT Client
client = mqtt.Client()

# Configure TLS
client.tls_set(
    ca_certs=CA_CERT,
    certfile=CLIENT_CERT,
    keyfile=CLIENT_KEY,
    tls_version=ssl.PROTOCOL_TLSv1_2
)
client.tls_insecure_set(False)

# On Connect Callback
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected securely to broker.")
    else:
        print(f"❌ Failed to connect. Return code={rc}")

client.on_connect = on_connect

# Connect to Broker
print("🔄 Connecting to MQTT broker...")
client.connect(BROKER_ADDRESS, PORT)
client.loop_start()

# Publish simulated data
try:
    while True:
        temp = round(random.uniform(20.0, 30.0), 2)
        print(f"📤 Publishing {temp}°C to topic '{TOPIC}'")
        client.publish(TOPIC, str(temp))
        time.sleep(3)
except KeyboardInterrupt:
    print("\n🛑 Stopping simulator...")
    client.loop_stop()
    client.disconnect()

