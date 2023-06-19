from fastapi import APIRouter, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi import Response
import json
import http.client
from fastapi import Response
from app.tools.background import app_background
from app.user.models import UserModel
from app.tools.authorization import validate_token

UserRoute = APIRouter()

@UserRoute.post("/login", tags=['Login'])
async def user_authentication(request: Request):
    '''User Authentication'''
    try:
        user = UserModel()
        datas = await request.json()
        
        status, res = user.auth_users(
            username=datas.get("username"),
            password=datas.get("password")
        )
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
