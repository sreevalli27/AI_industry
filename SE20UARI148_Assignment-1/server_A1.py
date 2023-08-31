import asyncio
import websockets
import json

async def handle_client(websocket, path):
    async for message in websocket:
        data = json.loads(message)
        client_message = data.get('message', '')
        
        print(f"Received Message: {client_message}")
        response_message = f"Server says: Hello this is server! You said: {client_message}"
        
        response_data = {"status": "Message Received!", "response_message": response_message}
        await websocket.send(json.dumps(response_data))

start_server = websockets.serve(handle_client, "139.59.28.124", 5001)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
