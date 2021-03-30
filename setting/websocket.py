import asyncio
import websockets
import time
import redis


async def data(websocket, path):
    while True:
        r =redis.StrictRedis()
        p = r.pubsub()
        p.subscribe("name")
        for i in p.listen():
            print( int(i["data"]) )
            await websocket.send( str(int(i["data"])) )
        await asyncio.sleep(0.05)

    
start_server = websockets.serve(data, "0.0.0.0", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
