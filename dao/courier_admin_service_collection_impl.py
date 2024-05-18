# courier_admin_service_collection_impl.py

from dao import ICourierAdminService, CourierCompanyCollection, CourierUserServiceCollectionImpl
from entity import Employee

class CourierAdminServiceCollectionImpl(CourierUserServiceCollectionImpl, ICourierAdminService):
    def __init__(self, company_obj: CourierCompanyCollection):
        super().__init__(company_obj)

    def add_courier_staff(self, name: str, contact_number: str) -> int:
        employee_id = len(self.company_obj.get_employee_details()) + 1
        new_employee = Employee(employee_id, name, "", contact_number, "", 0)
        self.company_obj.add_employee_detail(new_employee)
        return employee_id
