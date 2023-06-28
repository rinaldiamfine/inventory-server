from fastapi import APIRouter, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Response
import json
import http.client
from fastapi import Response
from app.tools.background import app_background
from app.order.models import OrderModel
from app.tools.authorization import validate_token
from datetime import datetime, date

OrderRoute = APIRouter()
websites = Jinja2Templates(directory="app/templates")

def default(o):
    if isinstance(o, (date, datetime)):
        return o.isoformat()

@OrderRoute.get("/order", tags=['Orders'])
def order_list(request: Request):
    '''Order List'''
    try:
        order = OrderModel()
        
        headers = request.headers
        status_decode_uid, decode_uid = validate_token(
            headers=headers
        )
        if not status_decode_uid:
            return Response(content=decode_uid, status_code=http.client.UNAUTHORIZED)
        
        status, res = order.get_order()
        if not status:
            return Response(content=res, status_code=http.client.BAD_REQUEST)
        return Response(
            content=json.dumps(res, default=default),
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


@OrderRoute.get("/order/{id}", tags=['Orders'])
def order_detail(request: Request, id: int):
    '''Order Detail'''
    try:
        order = OrderModel()
        
        headers = request.headers
        status_decode_uid, decode_uid = validate_token(
            headers=headers
        )
        if not status_decode_uid:
            return Response(content=decode_uid, status_code=http.client.UNAUTHORIZED)
        
        status, res = order.get_order_by_id(id)
        if not status:
            return Response(content=res, status_code=http.client.BAD_REQUEST)
        return Response(
            content=json.dumps(res, default=default),
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
    
@OrderRoute.post("/order", tags=['Orders'])
async def order_create(request: Request):
    '''Create Order'''
    try:
        data = await request.json()
        order = OrderModel()
        
        headers = request.headers
        status_decode_uid, decode_uid = validate_token(
            headers=headers
        )
        if not status_decode_uid:
            return Response(content=decode_uid, status_code=http.client.UNAUTHORIZED)
        
        status, res = order.create_order(data)
        if not status:
            return Response(content=res, status_code=http.client.BAD_REQUEST)
        return Response(
            content=json.dumps(res, default=default),
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

    
@OrderRoute.put("/order/{id}", tags=['Orders'])
async def order_update(request: Request, id: int):
    '''Update Order'''
    try:
        data = await request.json()
        order = OrderModel()
        
        headers = request.headers
        status_decode_uid, decode_uid = validate_token(
            headers=headers
        )
        if not status_decode_uid:
            return Response(content=decode_uid, status_code=http.client.UNAUTHORIZED)
        
        status, res = order.update_order(id, data)
        if not status:
            return Response(content=res, status_code=http.client.BAD_REQUEST)
        return Response(
            content=json.dumps(res, default=default),
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
    
@OrderRoute.delete("/order/{id}", tags=['Orders'])
def order_delete(request: Request, id: int):
    '''Delete Order'''
    try:
        order = OrderModel()
        
        headers = request.headers
        status_decode_uid, decode_uid = validate_token(
            headers=headers
        )
        if not status_decode_uid:
            return Response(content=decode_uid, status_code=http.client.UNAUTHORIZED)
        
        status, res = order.delete_order(id)
        if not status:
            return Response(content=res, status_code=http.client.BAD_REQUEST)
        return Response(
            content=json.dumps(res, default=default),
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
        