import imp
from fastapi import APIRouter, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi import Response
import json
import http.client
from fastapi import Response
from app.tools.background import app_background
from app.employee.models import EmployeeModel
from app.tools.authorization import validate_token

EmployeeRoute = APIRouter()

@EmployeeRoute.get("/employee", tags=['Employees'])
def employee_list(request: Request):
    '''Employee List'''
    try:
        employee = EmployeeModel()
        
        headers = request.headers
        status_decode_uid, decode_uid = validate_token(
            headers=headers
        )
        if not status_decode_uid:
            return Response(content=decode_uid, status_code=http.client.UNAUTHORIZED)
        
        status, res = employee.get_employee()
        if not status:
            return Response(content=res, status_code=http.client.BAD_REQUEST)

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
    
@EmployeeRoute.get("/employee/{id}", tags=['Employees'])
def employee_detail(request: Request, id: int):
    '''Employee Detail'''
    try:
        employee = EmployeeModel()
        
        headers = request.headers
        status_decode_uid, decode_uid = validate_token(
            headers=headers
        )
        if not status_decode_uid:
            return Response(content=decode_uid, status_code=http.client.UNAUTHORIZED)
        
        status, res = employee.get_employee_by_id(id)
        if not status:
            return Response(content=res, status_code=http.client.BAD_REQUEST)

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
    
@EmployeeRoute.post("/employee", tags=['Employees'])
async def employee_create(request: Request):
    '''Employee Create'''
    try:
        employee = EmployeeModel()
        datas = await request.json()
        
        headers = request.headers
        status_decode_uid, decode_uid = validate_token(
            headers=headers
        )
        if not status_decode_uid:
            return Response(content=decode_uid, status_code=http.client.UNAUTHORIZED)
        
        status, res = employee.create_employee(
            data=datas
        )
        if not status:
            return Response(content=res, status_code=http.client.BAD_REQUEST)

        return Response(
            content=res,
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
    
@EmployeeRoute.put("/employee/{id}", tags=['Employees'])
async  def employee_update(request: Request, id: int):
    '''Employee Update'''
    try:
        employee = EmployeeModel()
        datas = await request.json()
        
        headers = request.headers
        status_decode_uid, decode_uid = validate_token(
            headers=headers
        )
        if not status_decode_uid:
            return Response(content=decode_uid, status_code=http.client.UNAUTHORIZED)
        
        status, res = employee.update_employee(
            id=id,
            data=datas
        )
        if not status:
            return Response(content=res, status_code=http.client.BAD_REQUEST)

        return Response(
            content=res,
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
    
@EmployeeRoute.delete("/employee/{id}", tags=['Employees'])
def employee_delete(request: Request, id: int):
    '''Employee Delete'''
    try:
        employee = EmployeeModel()
        
        headers = request.headers
        status_decode_uid, decode_uid = validate_token(
            headers=headers
        )
        if not status_decode_uid:
            return Response(content=decode_uid, status_code=http.client.UNAUTHORIZED)
        
        status, res = employee.delete_employee(
            id=id
        )
        if not status:
            return Response(content=res, status_code=http.client.BAD_REQUEST)

        return Response(
            content=res,
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
        