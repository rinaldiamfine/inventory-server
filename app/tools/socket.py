from fastapi import WebSocket
from typing import List, Dict
import os

class ConnectionSocketManager:
    '''Connection Socket Manager'''
    def __init__(self):
        self.active_connections: List[Dict] = []

    async def connect(self, websocket: WebSocket, model: str, index: int):
        await websocket.accept()
        context = {
            'model': model,
            'id': index,
            'socket': websocket
        }
        self.active_connections.append(context)

    def disconnect(self, websocket: WebSocket, index: int):
        for connection in self.active_connections:
            if connection['id'] == index:
                if connection['socket'] == websocket:
                    self.active_connections.remove(connection)

    async def send(self, message: str, index: int):
        for connection in self.active_connections:
            if connection['id'] == index:
                await connection['socket'].send_text(message)
    
    async def send_data(self, data: dict, index: int):
        for connection in self.active_connections:
            if connection['id'] == index:
                strData = str(data)
                await connection['socket'].send_text(strData)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection['socket'].send_text(message)
            
socket = ConnectionSocketManager()