#!/usr/bin/env python

import asyncio
import websockets
import json
import time

async def reply(websocket, path):
    nodes = [
        { "id": 0, "label": "Myriel", "group": 1 },
        { "id": 1, "label": "Napoleon", "group": 1 },
        { "id": 2, "label": "Mlle.Baptistine", "group": 1 },
        { "id": 3, "label": "Mme.Magloire", "group": 1 },
        { "id": 4, "label": "CountessdeLo", "group": 1 },
        { "id": 5, "label": "Geborand", "group": 1 },
        { "id": 6, "label": "Champtercier", "group": 1 },
        { "id": 7, "label": "Cravatte", "group": 1 },
        { "id": 8, "label": "Count", "group": 1 },
        { "id": 9, "label": "OldMan", "group": 1 },
        { "id": 10, "label": "Labarre", "group": 2 },
        { "id": 11, "label": "Valjean", "group": 2 },
        { "id": 12, "label": "Marguerite", "group": 3 },
        { "id": 13, "label": "Mme.deR", "group": 2 },
        { "id": 14, "label": "Isabeau", "group": 2 },
        { "id": 15, "label": "Gervais", "group": 2 },
        { "id": 16, "label": "Tholomyes", "group": 3 },
        { "id": 17, "label": "Listolier", "group": 3 }
    ]
    
    edges = [
        { "from": 1, "to": 0 },
        { "from": 2, "to": 0 },
        { "from": 3, "to": 0 },
        { "from": 3, "to": 2 },
        { "from": 4, "to": 0 }
    ]
    
    data = {
        "nodes": nodes,
        "edges": edges
    }
    
    await websocket.send(json.dumps(data))
    
    # Wait a bit and then update the data
    time.sleep(5)
    
    data["edges"] = [
        { "from": 1, "to": 0 },
        { "from": 2, "to": 0 },
        { "from": 3, "to": 0 }
    ]
    
    await websocket.send(json.dumps(data))
    

asyncio.get_event_loop().run_until_complete(
    websockets.serve(reply, "localhost", 8001))

asyncio.get_event_loop().run_forever()