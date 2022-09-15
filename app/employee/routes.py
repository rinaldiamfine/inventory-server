from fastapi import APIRouter, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi import Response
import json
import http.client
from fastapi import Response
from app.tools.background import app_background

EmployeeRoute = APIRouter()

@EmployeeRoute.get("/employee", tags=['Employees'])
def employee_list(request: Request):
    '''Employee List'''
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
    
@EmployeeRoute.get("/employee/{id}", tags=['Employees'])
def employee_detail(request: Request, id: int):
    '''Employee Detail'''
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
    
@EmployeeRoute.post("/employee", tags=['Employees'])
def employee_create(request: Request):
    '''Employee Create'''
    res = "Employee Create"
    return Response(
        content=json.dumps(str(res)),
        status_code=http.client.OK,
        media_type='application/json'
    )
    
@EmployeeRoute.put("/employee/{id}", tags=['Employees'])
def employee_update(request: Request, id: int):
    '''Employee Update'''
    res = "Employee Update"
    return Response(
        content=json.dumps(str(res)),
        status_code=http.client.OK,
        media_type='application/json'
    )
    
@EmployeeRoute.delete("/employee/{id}", tags=['Employees'])
def employee_delete(request: Request, id: int):
    '''Employee Delete'''
    res = "Employee Delete"
    return Response(
        content=json.dumps(str(res)),
        status_code=http.client.OK,
        media_type='application/json'
    )