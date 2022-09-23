from fastapi import APIRouter, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi import Response
import json
import http.client
from fastapi import Response
from app.tools.background import app_background
from app.department.models import DepartmentModel

DepartmentRoute = APIRouter()

@DepartmentRoute.get("/department", tags=['Departments'])
def department_list(request: Request):
    '''Department List'''
    try:
        department = DepartmentModel()
        status, res = department.get_department()
        if not status:
            return Response(content=res, status_code=400)

        print("Employees: ", res)
        return Response(
            content=json.dumps(res),
            status_code=http.client.OK,
            media_type='application/json'
        )
    except Exception as e:
        print(e)
        return Response(
            content=json.dumps({'message': 'Error'}),
            status_code=http.client.INTERNAL_SERVER_ERROR,
            media_type='application/json'
        )

@DepartmentRoute.get("/department/{id}", tags=['Departments'])
def department_detail(request: Request, id: int):
    '''Department Detail'''
    try:
        department = DepartmentModel()
        status, res = department.get_department_by_id(id)
        if not status:
            return Response(content=res, status_code=400)
            
        return Response(
            content=json.dumps(res),
            status_code=http.client.OK,
            media_type='application/json'
        )
    except Exception as e:
        print(e)
        return Response(
            content=json.dumps({'message': 'Error'}),
            status_code=http.client.INTERNAL_SERVER_ERROR,
            media_type='application/json'
        )