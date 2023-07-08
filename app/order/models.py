from app.tools.database import DatabaseManager
from app import config
from datetime import date

class OrderModel:
    def __init__(self) -> None:
        self.db  = DatabaseManager()
        
    def check_order_status(self):
        try:
            cursor = self.db.connection.cursor()
            default_status = config.DEFAULT_STATUS
            expired_status = config.EXPIRED_STATUS
            current_date = date.today()
            cursor.execute("SELECT * FROM orders WHERE is_active = 1 AND `end_date` < %s AND `status` = %s", (current_date, default_status, ))
            columns = [column[0] for column in cursor.description]
            order_ids = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
            for order_id in order_ids:
                cursor.execute("UPDATE orders SET status = %s WHERE id = %s", (expired_status, order_id['id']))
                self.db.connection.commit()
            cursor.close()
            self.db.connection.close()
            return "Finished to check the order status"
        except Exception as e:
            return str(e)

    def get_order(self):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("SELECT * FROM orders where is_active = 1")
            columns = [column[0] for column in cursor.description]
            result = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
            cursor.close()
            self.db.connection.close()
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
            cursor.close()
            self.db.connection.close()
            return True, result
        except Exception as e:
            return False, str(e)
        
    def get_order_expired(self, date, status):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("SELECT * FROM orders WHERE `end_date` < %s AND `status` = %s", (date, status, ))
            columns = [column[0] for column in cursor.description]
            result = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
            cursor.close()
            self.db.connection.close()
            return True, result
        except Exception as e:
            return False, str(e)

    def create_order(self, data):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("INSERT INTO orders (product_id, employee_id, qty, start_date, end_date, status) VALUES (%s, %s, %s, %s, %s, %s)", (data['product_id'], data['employee_id'], data['qty'], data['start_date'], data['end_date'], data['status']))
            self.db.connection.commit()
            cursor.close()
            self.db.connection.close()
            return True, "Order created successfully"
        except Exception as e:
            return False, str(e)
        
    def update_order_with_type(self, id, data):
        # try:
            cursor = self.db.connection.cursor()
            cursor.execute("UPDATE orders SET product_id = %s, employee_id = %s, qty = %s, status = %s WHERE id = %s", (data['product_id'], data['employee_id'], data['qty'], data['status'], id))
            self.db.connection.commit()
            # cursor.close()
            # self.db.connection.close()

            ## updaate the product
            cursor.execute("SELECT * FROM products WHERE id = %s", (data['product_id'],))
            columns = [column[0] for column in cursor.description]
            result = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
            if len(result) > 0:
                returned_product = int(data['qty']) + int(result.get("qty"))
                cursor.execute("UPDATE products SET qty = %s WHERE id = %s", (returned_product, data['product_id']))
                self.db.connection.commit()

            cursor.close()
            self.db.connection.close()

            return True, "Order updated successfully"
        # except Exception as e:
        #     return False, str(e)
        
    def update_order(self, id, data):
        # try:
            cursor = self.db.connection.cursor()
            cursor.execute("UPDATE orders SET product_id = %s, employee_id = %s, qty = %s, start_date = %s, end_date = %s, status = %s WHERE id = %s", (data['product_id'], data['employee_id'], data['qty'], data['start_date'], data['end_date'], data['status'], id))
            self.db.connection.commit()
            cursor.close()
            self.db.connection.close()
            return True, "Order updated successfully"
        # except Exception as e:
        #     return False, str(e)

    def delete_order(self, id):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("UPDATE orders SET is_active=0 WHERE id = %s", (id,))
            self.db.connection.commit()
            cursor.close()
            self.db.connection.close()
            return True, "Order deleted successfully"
        except Exception as e:
            return False, str(e)
