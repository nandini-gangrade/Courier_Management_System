# courier_company_collection.py

class CourierCompanyCollection:
    def __init__(self, company_name):
        self.__company_name = company_name
        self.__courier_details = []
        self.__employee_details = []
        self.__location_details = []

    def get_courier_details(self):
        return self.__courier_details

    def get_employee_details(self):
        return self.__employee_details

    def get_location_details(self):
        return self.__location_details

    def add_courier_detail(self, courier):
        self.__courier_details.append(courier)

    def add_employee_detail(self, employee):
        self.__employee_details.append(employee)

    def add_location_detail(self, location):
        self.__location_details.append(location)
