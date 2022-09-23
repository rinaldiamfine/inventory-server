from fastapi import APIRouter, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi import Response
import json
import http.client
from fastapi import Response
from app.tools.background import app_background
from app.product.models import ProductModel

ProductRoute = APIRouter()

@ProductRoute.get("/product", tags=['Products'])
def product_list(request: Request):
    '''Product List'''
    try:
        product = ProductModel()
        status, res = product.get_product()
        if not status:
            return Response(content=res, status_code=400)

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
        status, res = product.get_product_by_id(id)
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
    
@ProductRoute.post("/product", tags=['Products'])
async def product_create(request: Request):
    '''Product Create'''
    try:
        product = ProductModel()
        datas = await request.json()
        status, res = product.create_product(datas)
        if not status:
            return Response(content=res, status_code=400)

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
        datas = await request.json()
        status, res = product.update_product(id, datas)
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
    
@ProductRoute.delete("/product/{id}", tags=['Products'])
def product_delete(request: Request, id: int):
    '''Product Delete'''
    try:
        product = ProductModel()
        status, res = product.delete_product(id)
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