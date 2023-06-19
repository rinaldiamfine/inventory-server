from fastapi import APIRouter, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi import Response
import json
import http.client
from fastapi import Response
from app.tools.background import app_background
from app.product.models import ProductModel
from app.tools.authorization import validate_token

ProductRoute = APIRouter()

@ProductRoute.get("/product", tags=['Products'])
def product_list(request: Request):
    '''Product List'''
    try:
        product = ProductModel()
        
        headers = request.headers
        status_decode_uid, decode_uid = validate_token(
            headers=headers
        )
        if not status_decode_uid:
            return Response(content=decode_uid, status_code=http.client.UNAUTHORIZED)
        
        status, res = product.get_product()
        if not status:
            return Response(content=res, status_code=http.client.BAD_REQUEST)

        print("Products: ", res)
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
    
@ProductRoute.get("/product/{id}", tags=['Products'])
def product_detail(request: Request, id: int):
    '''Product Detail'''
    try:
        product = ProductModel()
        
        headers = request.headers
        status_decode_uid, decode_uid = validate_token(
            headers=headers
        )
        if not status_decode_uid:
            return Response(content=decode_uid, status_code=http.client.UNAUTHORIZED)
        
        status, res = product.get_product_by_id(id)
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
    
@ProductRoute.post("/product", tags=['Products'])
async def product_create(request: Request):
    '''Product Create'''
    try:
        product = ProductModel()
        datas = await request.json()
        
        headers = request.headers
        status_decode_uid, decode_uid = validate_token(
            headers=headers
        )
        if not status_decode_uid:
            return Response(content=decode_uid, status_code=http.client.UNAUTHORIZED)
        
        status, res = product.create_product(datas)
        if not status:
            return Response(content=res, status_code=http.client.BAD_REQUEST)

        return Response(
            content=json.dumps(res),
            status_code=http.client.CREATED,
            media_type='application/json'
        )
    except Exception as e:
        print(e)
        return Response(
            content=json.dumps({'message': 'Error'}),
            status_code=http.client.INTERNAL_SERVER_ERROR,
            media_type='application/json'
        )
    
@ProductRoute.put("/product/{id}", tags=['Products'])
async def product_update(request: Request, id: int):
    '''Product Update'''
    try:
        product = ProductModel()
        
        headers = request.headers
        status_decode_uid, decode_uid = validate_token(
            headers=headers
        )
        if not status_decode_uid:
            return Response(content=decode_uid, status_code=http.client.UNAUTHORIZED)
        
        datas = await request.json()
        status, res = product.update_product(id, datas)
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
    
@ProductRoute.delete("/product/{id}", tags=['Products'])
def product_delete(request: Request, id: int):
    '''Product Delete'''
    try:
        product = ProductModel()
        
        headers = request.headers
        status_decode_uid, decode_uid = validate_token(
            headers=headers
        )
        if not status_decode_uid:
            return Response(content=decode_uid, status_code=http.client.UNAUTHORIZED)
        
        status, res = product.delete_product(id)
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
        