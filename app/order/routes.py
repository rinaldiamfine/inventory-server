from fastapi import APIRouter, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Response
import json
import http.client
from fastapi import Response
from app.tools.background import app_background

OrderRoute = APIRouter()

websites = Jinja2Templates(directory="app/templates")

@OrderRoute.get("/order", tags=['Inventories'])
def order_list(request: Request):
    '''Order List'''
    res = {
        "data": [
            {"id": 1, "name": "John Doe", "age": 42},
            {"id": 2, "name": "Jane Doe", "age": 36}
        ]
    }
    return Response(
        content=json.dumps(str(res)),
        status_code=http.client.OK,
        media_type='application/json'
    )
    
@OrderRoute.post("/order", tags=['Inventories'])
def order_create(request: Request):
    '''Create Order'''
    res = "Order Created"
    return Response(
        content=json.dumps(str(res)),
        status_code=http.client.OK,
        media_type='application/json'
    )
    
@OrderRoute.get("/order/{id}", tags=['Inventories'])
def order_detail(request: Request, id: int):
    '''Order Detail'''
    res = {
        "data": [
            {"id": id, "name": "John Doe", "age": 42},
        ]
    }
    return Response(
        content=json.dumps(str(res)),
        status_code=http.client.OK,
        media_type='application/json'
    )
    
@OrderRoute.put("/order/{id}", tags=['Inventories'])
def order_update(request: Request, id: int):
    '''Update Order'''
    res = "Order Updated"
    return Response(
        content=json.dumps(str(res)),
        status_code=http.client.OK,
        media_type='application/json'
    )
    
@OrderRoute.delete("/order/{id}", tags=['Inventories'])
def order_delete(request: Request, id: int):
    '''Delete Order'''
    res = "Order Deleted"
    return Response(
        content=json.dumps(str(res)),
        status_code=http.client.OK,
        media_type='application/json'
    )