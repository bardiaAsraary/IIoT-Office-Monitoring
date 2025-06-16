from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner
import asyncio
import ssl
import json

class RouterSession(ApplicationSession):
    async def onJoin(self, details):
        print("WAMP Router Ready")
        
        # Register RPC endpoint
        await self.register(self.get_sensor_data, "sensors.get_data")
        
        # Handle subscriptions
        self.subscribe(self.on_sensor_data, "sensors.data")
    
    async def get_sensor_data(self):
        return {"status": "active", "sensors": 3}
    
    def on_sensor_data(self, data):
        print(f"Received sensor data: {data}")
        # Broadcast to dashboard
        self.publish("dashboard.update", json.dumps(data))

if __name__ == "__main__":
    # TLS configuration
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.load_cert_chain("certs/server-cert.pem", "certs/server-key.pem")
    ssl_context.load_verify_locations("certs/ca-cert.pem")
    ssl_context.verify_mode = ssl.CERT_REQUIRED
    
    # Start router
    runner = ApplicationRunner(
        url="wss://localhost:8080/ws",
        realm="iot_realm",
        ssl=ssl_context
    )
    print("Starting WAMP router on wss://localhost:8080/ws")
    runner.run(RouterSession)