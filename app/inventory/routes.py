from fastapi import APIRouter, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Response
import json
import http.client
from fastapi import Response
from app.tools.background import app_background

InventoryRoute = APIRouter()

websites = Jinja2Templates(directory="app/templates")

@InventoryRoute.get("/dashboard", response_class=HTMLResponse, tags=['Dashboards'])
async def website_dashboard(request: Request):
    '''Dashboard View'''
    return websites.TemplateResponse("dashboard.html", {"request": request})

@InventoryRoute.get("/inventory", tags=['Inventories'])
def inventory_list(request: Request):
    '''Inventory List'''
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
    
@InventoryRoute.post("/inventory", tags=['Inventories'])
def inventory_create(request: Request):
    '''Create Inventory'''
    res = "Inventory Created"
    return Response(
        content=json.dumps(str(res)),
        status_code=http.client.OK,
        media_type='application/json'
    )
    
@InventoryRoute.get("/inventory/{id}", tags=['Inventories'])
def inventory_detail(request: Request, id: int):
    '''Inventory Detail'''
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
    
@InventoryRoute.put("/inventory/{id}", tags=['Inventories'])
def inventory_update(request: Request, id: int):
    '''Update Inventory'''
    res = "Inventory Updated"
    return Response(
        content=json.dumps(str(res)),
        status_code=http.client.OK,
        media_type='application/json'
    )
    
@InventoryRoute.delete("/inventory/{id}", tags=['Inventories'])
def inventory_delete(request: Request, id: int):
    '''Delete Inventory'''
    res = "Inventory Deleted"
    return Response(
        content=json.dumps(str(res)),
        status_code=http.client.OK,
        media_type='application/json'
    )