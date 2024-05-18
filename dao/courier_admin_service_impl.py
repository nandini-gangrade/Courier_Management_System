# dao/courier_admin_service_impl.py

from .icourier_admin_service import ICourierAdminService

class CourierAdminServiceImpl(ICourierAdminService):
    def __init__(self, company_collection):
        self.company_collection = company_collection

    def add_courier_staff(self, name, contact_number):
        max_existing_employee_id = max([employee.EmployeeID for employee in self.company_collection.get_employee_details()])
        employee_id = max_existing_employee_id + 1
        employee_id = len(self.company_collection.get_employee_details()) + 1
        self.company_collection.add_employee_detail({
            'employee_id': employee_id,
            'name': name,
            'contact_number': contact_number
        })
        return employee_id
