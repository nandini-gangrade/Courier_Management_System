# main.py

from dao.courier_service_db import CourierServiceDb 
from dao.courier_user_service_collection_impl import CourierUserServiceCollectionImpl
from dao.courier_admin_service_impl import CourierAdminServiceImpl
from dao.courier_company_collection import CourierCompanyCollection
from util import *
from exception import *
from entity import *
import pyodbc

class Main:
    def __init__(self):
        self.courier_service = CourierServiceDb()
        self.company_collection = CourierCompanyCollection("XYZ Courier Company")
        self.admin_service = CourierAdminServiceImpl(self.company_collection)
        self.user_service = CourierUserServiceCollectionImpl(self.company_collection)

    def display_main_menu(self):
        print("Welcome to the Courier Management System!")
        print("1. Place a new courier order")
        print("2. Get the status of a courier order")
        print("3. Cancel a courier order")
        print("4. Get a list of orders assigned to a specific courier staff member")
        print("5. Add a new courier staff member to the system")
        print("6. Generate revenue report")
        print("7. Retrieve delivery history")
        print("8. Generate shipment status report")
        print("9. Exit")

    def run(self):
        while True:
            self.display_main_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.place_order()
            elif choice == '2':
                self.get_order_status()
            elif choice == '3':
                self.cancel_order()
            elif choice == '4':
                self.get_assigned_order()
            elif choice == '5':
                self.add_courier_staff()
            elif choice == '6':
                self.generate_revenue_report()
            elif choice == '7':
                self.retrieve_delivery_history()
            elif choice == '8':
                self.generate_shipment_status_report()
            elif choice == '9':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    def place_order(self):
        sender_name = input("Enter sender's name: ")
        sender_address = input("Enter sender's address: ")
        receiver_name = input("Enter receiver's name: ")
        receiver_address = input("Enter receiver's address: ")
        weight = float(input("Enter weight of the courier: "))
        status = "Pending"  # Initial status
        user_id = int(input("Enter user ID: "))  # Assuming user ID is needed
        courier_obj = Courier(None, sender_name, sender_address, receiver_name, receiver_address, weight, status, None, None, user_id)
        try:
            tracking_number = self.user_service.place_order(courier_obj)
            print("Courier placed successfully. Tracking number:", tracking_number)
        except Exception as e:
            print(f"An error occurred while placing the order: {e}")

    def get_order_status(self):
        tracking_number = input("Enter tracking number: ")
        try:
            status = self.user_service.get_order_status(tracking_number)
            print("Courier Status:", status)
        except TrackingNumberNotFoundException as e:
            print("Tracking number not found:", e)
        except Exception as e:
            print(f"An error occurred while getting order status: {e}")

    def cancel_order(self):
        tracking_number = input("Enter tracking number of order to cancel: ")
        try:
            success = self.user_service.cancel_order(tracking_number)
            if success:
                print("Courier order cancelled successfully.")
            else:
                print("Failed to cancel courier order. Please check the tracking number.")
        except TrackingNumberNotFoundException as e:
            print("Tracking number not found:", e)
        except Exception as e:
            print(f"An error occurred while cancelling the order: {e}")

    def get_assigned_order(self):
        courier_staff_id = int(input("Enter courier staff ID: "))
        try:
            assigned_orders = self.user_service.get_assigned_order(courier_staff_id)
            if assigned_orders:
                print("Orders assigned to courier staff:")
                for order in assigned_orders:
                    print(order)
            else:
                print("No orders assigned to the provided courier staff ID.")
        except InvalidEmployeeIdException as e:
            print("Invalid employee ID:", e)
        except Exception as e:
            print(f"An error occurred while getting assigned orders: {e}")

    def add_courier_staff(self):
        name = input("Enter employee name: ")
        contact_number = input("Enter employee contact number: ")
        try:
            employee_id = self.admin_service.add_courier_staff(name, contact_number)
            print("Courier staff added successfully. Employee ID:", employee_id)
        except Exception as e:
            print(f"An error occurred while adding courier staff: {e}")

    def generate_revenue_report(self):
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        try:
            revenue = self.courier_service.generate_revenue_report(start_date, end_date)
            if revenue is not None:
                print("Total revenue generated:", revenue)
            else:
                print("Failed to generate revenue report.")
        except Exception as e:
            print(f"An error occurred while generating revenue report: {e}")

    def retrieve_delivery_history(self):
        parcel_id = input("Enter parcel ID: ")
        try:
            delivery_history = self.courier_service.retrieve_delivery_history(parcel_id)
            if delivery_history:
                print("Delivery history for parcel ID:", parcel_id)
                for entry in delivery_history:
                    print(entry)
            else:
                print("Failed to retrieve delivery history.")
        except Exception as e:
            print(f"An error occurred while retrieving delivery history: {e}")

    def generate_shipment_status_report(self):
        try:
            shipment_report = self.courier_service.generate_shipment_status_report()
            if shipment_report:
                print("Shipment status report:")
                for shipment in shipment_report:
                    print(shipment)
            else:
                print("Failed to generate shipment status report.")
        except Exception as e:
            print(f"An error occurred while generating shipment status report: {e}")

if __name__ == "__main__":
    main_module = Main()
    main_module.run()
