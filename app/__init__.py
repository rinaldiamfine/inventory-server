from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
import config
import app.metadata as metadatas
import json
from app.tools.socket import socket
from app.tools.mail import MailManager
from app.tools.database import DatabaseManager

# app = FastAPI(openapi_tags=metadatas.tags_metadata)
app = FastAPI()
app_socket = socket
configuration = config
mail = MailManager()
# database = None
database = DatabaseManager()

app.mount("/packages", StaticFiles(directory="app/packages"), name="packages")

from app.order.routes import OrderRoute
from app.employee.routes import EmployeeRoute
from app.department.routes import DepartmentRoute
from app.product.routes import ProductRoute
from app.user.routes import UserRoute

app.include_router(OrderRoute)
app.include_router(EmployeeRoute)
app.include_router(DepartmentRoute)
app.include_router(ProductRoute)
app.include_router(UserRoute)