import asyncio
from autobahn.asyncio.websocket import WebSocketClientProtocol, WebSocketClientFactory

class ListenerProtocol(WebSocketClientProtocol):
    def onConnect(self, response):
        print("Connected to:", response.peer)
        
    def onOpen(self):
        print("WebSocket connection open")
        self.sendMessage('["HELLO", "default", {"roles": {"subscriber": {}}}]'.encode('utf8'))
        
    def onMessage(self, payload, isBinary):
        print("RAW WAMP MESSAGE:", payload.decode('utf8'))
        
    def onClose(self, wasClean, code, reason):
        print("Connection closed:", reason)

async def main():
    factory = WebSocketClientFactory("ws://localhost:8080")  # Try ws:// first
    factory.protocol = ListenerProtocol
    
    try:
        await asyncio.get_event_loop().create_connection(factory, 'localhost', 8080)
    except ConnectionRefusedError:
        print("\n❌ Connection failed. Please check:")
        print("- Is WAMP router running?")
        print("- Try 'ws://' instead of 'wss://' if no TLS")
        print("- Firewall blocking port 8080?")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
    asyncio.get_event_loop().run_forever()