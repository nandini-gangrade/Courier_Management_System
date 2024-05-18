from util.db_connection import DBConnection
import pyodbc

class CourierServiceDb:
    connection = None

    def __init__(self):
        self.connection = DBConnection.get_connection()

    def insert_parcel(self, parcel_data):
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO Parcel (column1, column2, ...) VALUES (?, ?, ...)", parcel_data)
            self.connection.commit()
            cursor.close()
        except pyodbc.Error as e:
            print(f"Error inserting parcel: {e}")

    def update_payment_status(self, payment_id, new_status):
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE Payment SET PaymentStatus = ? WHERE PaymentID = ?", new_status, payment_id)
            self.connection.commit()
            cursor.close()
        except pyodbc.Error as e:
            print(f"Error updating payment status: {e}")

    def retrieve_customer_orders(self, customer_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Order WHERE CustomerID = ?", customer_id)
            customer_orders = cursor.fetchall()
            cursor.close()
            return customer_orders
        except pyodbc.Error as e:
            print(f"Error retrieving customer orders: {e}")
            return None

    def generate_revenue_report(self, start_date, end_date):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT SUM(Amount) FROM Payment WHERE PaymentDate BETWEEN ? AND ?", start_date, end_date)
            total_revenue = cursor.fetchone()[0]
            cursor.close()
            return total_revenue
        except pyodbc.Error as e:
            print(f"Error generating revenue report: {e}")
            return None

    def retrieve_delivery_history(self, parcel_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
    SELECT DeliveryDate
FROM [Order]
WHERE OrderID = (SELECT OrderID FROM Parcel WHERE ParcelID = ?);
''', (parcel_id,))
            delivery_history = cursor.fetchall()
            cursor.close()
            return delivery_history
        except pyodbc.Error as e:
            print(f"Error retrieving delivery history: {e}")
            return None

    def generate_shipment_status_report(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Courier WHERE Status = 'In Transit'")
            in_transit_shipments = cursor.fetchall()
            cursor.close()
            return in_transit_shipments
        except pyodbc.Error as e:
            print(f"Error generating shipment status report: {e}")

    def get_assigned_order(self, courier_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM [Order] WHERE CourierID = ?", courier_id)
            assigned_orders = cursor.fetchall()
            cursor.close()
            return assigned_orders
        except pyodbc.Error as e:
            print(f"Error retrieving assigned orders: {e}")
            return None
