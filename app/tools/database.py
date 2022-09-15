import mysql.connector
from sqlalchemy import create_engine
import config
import pymysql

class DatabaseManager:
    '''Database Manager'''
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=config.DB_NAME
        )
        # # self.cursor = self.db.cursor()
        # # self.engine = create_engine(config.DB_URI)

        # self.engine = create_engine(f"mysql+pymysql://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}/{config.DB_NAME}?charset=utf8mb4")
        # self.connection = self.engine.connect()
