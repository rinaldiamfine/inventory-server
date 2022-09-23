from app.tools.database import DatabaseManager

class EmployeeModel:
    def __init__(self) -> None:
        self.db  = DatabaseManager()

    def get_employee(self):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("SELECT * FROM employees where is_active = 1")
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

    def create_employee(self, data):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("INSERT INTO employees (name, email, department_id, badge_id) VALUES (%s, %s, %s, %s)", (data['name'], data['email'], data['department_id'], data['badge_id']))
            self.db.connection.commit()
            return True, "Employee created successfully"
        except Exception as e:
            return False, str(e)

    def update_employee(self, id, data):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("UPDATE employees SET name = %s, email = %s, department_id = %s, badge_id = %s WHERE id = %s", (data['name'], data['email'], data['department_id'], data['badge_id'], id))
            self.db.connection.commit()
            return True, "Employee updated successfully"
        except Exception as e:
            return False, str(e)

    def delete_employee(self, id):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("UPDATE employees SET is_active=0 WHERE id = %s", (id))
            self.db.connection.commit()
            return True, "Employee deleted successfully"
        except Exception as e:
            return False, str(e)