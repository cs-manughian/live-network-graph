#!/usr/bin/env python

import asyncio
import websockets
import json

async def reply(websocket, path):
    data_points = [
        [4, 8, 15, 16, 23, 42],
        [1, 2, 3, 16, 23, 42],
        [4, 6, 18, 9, 3, 12]
    ]
    
    for point in data_points:
        await websocket.send(json.dumps(point))

asyncio.get_event_loop().run_until_complete(
    websockets.serve(reply, 'localhost', 8001))

asyncio.get_event_loop().run_forever()