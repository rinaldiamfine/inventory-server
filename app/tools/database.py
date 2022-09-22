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

    
    def get_list_employee(self):
        cursor = self.connection.cursor()
        print(cursor, "CURSOR")
        cursor.execute("SELECT * FROM employees")
        result = cursor.fetchall()
        print(result, "RESULT")
        return result

    def get_employee(self, id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM employees WHERE id = %s", (id,))
        result = cursor.fetchone()
        return result

        # # self.cursor = self.db.cursor()
        # # self.engine = create_engine(config.DB_URI)

        # self.engine = create_engine(f"mysql+pymysql://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}/{config.DB_NAME}?charset=utf8mb4")
        # self.connection = self.engine.connect()
