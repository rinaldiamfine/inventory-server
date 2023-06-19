from app.tools.database import DatabaseManager

class ProductModel:
    def __init__(self):
        self.db = DatabaseManager()

    def get_product(self):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("SELECT * FROM products where is_active = 1")
            columns = [column[0] for column in cursor.description]
            result = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
            return True, result
        except Exception as e:
            return False, str(e)

    def get_product_by_id(self, id):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("SELECT * FROM products WHERE id = %s", (id,))
            columns = [column[0] for column in cursor.description]
            result = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
            return True, result
        except Exception as e:
            return False, str(e)

    def create_product(self, data):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("INSERT INTO products (name, code, qty) VALUES (%s, %s, %s)", (data['name'], data['code'], data['qty']))
            self.db.connection.commit()
            return True, "Product created successfully"
        except Exception as e:
            return False, str(e)

    def update_product(self, id, data):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("UPDATE products SET name = %s, code = %s, qty = %s WHERE id = %s", (data['name'], data['code'], data['qty'], id))
            self.db.connection.commit()
            return True, "Product updated successfully"
        except Exception as e:
            return False, str(e)

    def delete_product(self, id):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("UPDATE products SET is_active=0 WHERE id = %s", (id,))
            self.db.connection.commit()
            cursor.close()
            self.db.connection.close()
            return True, "Product deleted successfully"
        except Exception as e:
            return False, str(e)