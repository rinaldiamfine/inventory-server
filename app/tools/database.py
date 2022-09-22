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