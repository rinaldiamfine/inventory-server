from app.tools.database import DatabaseManager

class OrderModel:
    def __init__(self) -> None:
        self.db  = DatabaseManager()

    def get_order(self):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("SELECT * FROM orders where is_active = 1")
            columns = [column[0] for column in cursor.description]
            result = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
            return True, result
        except Exception as e:
            return False, str(e)

    def get_order_by_id(self, id):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("SELECT * FROM orders WHERE id = %s", (id,))
            columns = [column[0] for column in cursor.description]
            result = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
            return True, result
        except Exception as e:
            return False, str(e)

    def create_order(self, data):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("INSERT INTO orders (product_id, employee_id, qty, start_date, end_date, status) VALUES (%s, %s, %s, %s, %s, %s)", (data['product_id'], data['employee_id'], data['qty'], data['start_date'], data['end_date'], data['status']))
            self.db.connection.commit()
            return True, "Order created successfully"
        except Exception as e:
            return False, str(e)

    def update_order(self, id, data):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("UPDATE orders SET product_id = %s, employee_id = %s, qty = %s, start_date = %s, end_date = %s, status = %s WHERE id = %s", (data['product_id'], data['employee_id'], data['qty'], data['start_date'], data['end_date'], data['status'], id))
            self.db.connection.commit()
            return True, "Order updated successfully"
        except Exception as e:
            return False, str(e)

    def delete_order(self, id):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("UPDATE orders SET is_active=0 WHERE id = %s", (id,))
            self.db.connection.commit()
            return True, "Order deleted successfully"
        except Exception as e:
            return False, str(e)
