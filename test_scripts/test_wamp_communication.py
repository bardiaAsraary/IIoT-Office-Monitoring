from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner
import asyncio

class Tester(ApplicationSession):
    async def onJoin(self, details):
        # Test publication
        self.publish("sensors.data", {"test": 42})
        print("Published test message")
        
        # Test RPC
        result = await self.call("sensors.get_data")
        print("RPC Result:", result)
        
        self.leave()

if __name__ == "__main__":
    ssl_context = ssl.create_default_context()
    ssl_context.load_verify_locations("certs/ca-cert.pem")
    ssl_context.load_cert_chain("certs/mcu-cert.pem", "certs/mcu-key.pem")
    
    runner = ApplicationRunner(
        "wss://localhost:8080/ws", 
        "iot_realm",
        ssl=ssl_context
    )
    print("Testing WAMP communication...")
    runner.run(Tester)