#!/usr/bin/env python

import asyncio
import websockets
import json
import time

async def reply(websocket, path):
    graph_json = {
        "nodes": [
            {
                "id": "Cosima",
                "group": 4
            }
        ],
        "links": [
            # {
            #     "source": "Mme.Burgon",
            #     "target": "Cosima",
            #     "value": 1
            # }
        ]
    }
    
    # Wait a bit and then update the data
    time.sleep(2)
    
    await websocket.send(json.dumps(graph_json))
    

asyncio.get_event_loop().run_until_complete(
    websockets.serve(reply, "localhost", 8001))

asyncio.get_event_loop().run_forever()