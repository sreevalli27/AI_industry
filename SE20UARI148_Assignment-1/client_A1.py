import asyncio
import websockets
import json

async def main():
    async with websockets.connect("ws://localhost:5001") as websocket:
        try:
            while True:
                message = input("Enter your message: ")
                data = {"message": message}
                await websocket.send(json.dumps(data))
                
                response = await websocket.recv()
                response_data = json.loads(response)
                response_message = response_data.get("response_message", "No response")
                print("Server Response:", response_message)
        except KeyboardInterrupt:
            print("Client disconnected")

asyncio.get_event_loop().run_until_complete(main())
