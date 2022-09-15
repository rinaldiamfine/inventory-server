from fastapi import APIRouter, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi import Response
import json
import http.client
from fastapi import Response
from app.tools.background import app_background

ProductRoute = APIRouter()

@ProductRoute.get("/product", tags=['Products'])
def product_list(request: Request):
    '''Product List'''
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
    
@ProductRoute.get("/product/{id}", tags=['Products'])
def product_detail(request: Request, id: int):
    '''Product Detail'''
    res = {
        "data": {
            "id": id,
            "name": "John Doe",
            "age": 42
        }
    }
    return Response(
        content=json.dumps(str(res)),
        status_code=http.client.OK,
        media_type='application/json'
    )
    
@ProductRoute.post("/product", tags=['Products'])
def product_create(request: Request):
    '''Product Create'''
    res = "Product Create"
    return Response(
        content=json.dumps(str(res)),
        status_code=http.client.OK,
        media_type='application/json'
    )
    
@ProductRoute.put("/product/{id}", tags=['Products'])
def product_update(request: Request, id: int):
    '''Product Update'''
    res = "Product Update"
    return Response(
        content=json.dumps(str(res)),
        status_code=http.client.OK,
        media_type='application/json'
    )
    
@ProductRoute.delete("/product/{id}", tags=['Products'])
def product_delete(request: Request, id: int):
    '''Product Delete'''
    res = "Product Delete"
    return Response(
        content=json.dumps(str(res)),
        status_code=http.client.OK,
        media_type='application/json'
    )