# courier_user_service_impl.py

from dao import ICourierUserService
from entity import Courier
import random

class CourierUserServiceImpl(ICourierUserService):
    tracking_number_generator = random.randint(1000, 9999)

    def __init__(self, company_obj):
        self.company_obj = company_obj

    def place_order(self, courier_obj: Courier) -> str:
        tracking_number = str(self.tracking_number_generator)
        courier_obj.set_tracking_number(tracking_number)
        self.tracking_number_generator += 1
        self.company_obj.add_courier_detail(courier_obj)
        return tracking_number

    def get_order_status(self, tracking_number: str) -> str:
        for courier in self.company_obj.get_courier_details():
            if courier.get_tracking_number() == tracking_number:
                return courier.get_status()
        return "Tracking Number not found"

    def cancel_order(self, tracking_number: str) -> bool:
        for courier in self.company_obj.get_courier_details():
            if courier.get_tracking_number() == tracking_number:
                return self.company_obj.get_courier_details().remove(courier)
        return False

    def get_assigned_order(self, courier_staff_id: int) -> list:
        assigned_orders = []
        for courier in self.company_obj.get_courier_details():
            if courier.get_user_id() == courier_staff_id:
                assigned_orders.append(courier)
        return assigned_orders
