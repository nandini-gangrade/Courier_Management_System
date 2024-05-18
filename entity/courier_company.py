# dao/courier_company_collection.py

class CourierCompanyCollection:
    def __init__(self, company_name):
        self.__company_name = company_name
        self.__courier_details = []
        self.__employee_details = []
        self.__location_details = []

    # Getters
    def get_company_name(self):
        return self.__company_name

    def get_courier_details(self):
        return self.__courier_details

    def get_employee_details(self):
        return self.__employee_details

    def get_location_details(self):
        return self.__location_details

    # Setters
    def set_company_name(self, company_name):
        self.__company_name = company_name

    def add_courier_detail(self, courier):
        self.__courier_details.append(courier)

    def add_employee_detail(self, employee):
        self.__employee_details.append(employee)

    def add_location_detail(self, location):
        self.__location_details.append(location)

    def __str__(self):
        return f"Company Name: {self.__company_name}"
