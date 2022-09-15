from fastapi import APIRouter, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi import Response
import json
import http.client
from fastapi import Response
from app.tools.background import app_background

DepartmentRoute = APIRouter()

@DepartmentRoute.get("/department", tags=['Departments'])
def department_list(request: Request):
    '''Department List'''
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