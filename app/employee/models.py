from app.tools.database import DatabaseManager

class EmployeeModel:
    def __init__(self) -> None:
        self.db  = DatabaseManager()

    def get_employee(self):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("SELECT * FROM employees")
            columns = [column[0] for column in cursor.description]
            result = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
            return True, result
        except Exception as e:
            return False, str(e)

    def get_employee_by_id(self, id):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("SELECT * FROM employees WHERE id = %s", (id,))
            columns = [column[0] for column in cursor.description]
            result = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
            return True, result
        except Exception as e:
            return False, str(e)