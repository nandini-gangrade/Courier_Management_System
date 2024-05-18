# dao/courier_user_service_collection_impl.py

from .icourier_user_service import ICourierUserService
from entity.courier import Courier
from .courier_company_collection import CourierCompanyCollection
from exception.custom_exception import TrackingNumberNotFoundException, InvalidEmployeeIdException

class CourierUserServiceCollectionImpl(ICourierUserService):
    def __init__(self, company_collection):
        self.company_collection = company_collection

    def place_order(self, courier):
        self.company_collection.add_courier_detail(courier)
        return courier.gettracking_number

    def get_order_status(self, tracking_number):
        for courier in self.company_collection.get_courier_details():
            if courier.tracking_number == tracking_number:
                return courier.status
        raise TrackingNumberNotFoundException()

    def cancel_order(self, tracking_number):
        for courier in self.company_collection.get_courier_details():
            if courier.tracking_number == tracking_number:
                courier.status = 'Cancelled'
                return True
        raise TrackingNumberNotFoundException()

    def get_assigned_order(self, courier_staff_id):
        assigned_orders = []
        for courier in self.company_collection.get_courier_details():
            if courier.assigned_to == courier_staff_id:
                assigned_orders.append(courier)
        if not assigned_orders:
            raise InvalidEmployeeIdException()
        return assigned_orders
