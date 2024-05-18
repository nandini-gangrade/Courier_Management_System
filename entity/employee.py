# employee.py

class Employee:
    def __init__(self, employee_id, employee_name, email, contact_number, role, salary):
        self.__employee_id = employee_id
        self.__employee_name = employee_name
        self.__email = email
        self.__contact_number = contact_number
        self.__role = role
        self.__salary = salary

    # Getters
    def get_employee_id(self):
        return self.__employee_id

    def get_employee_name(self):
        return self.__employee_name

    def get_email(self):
        return self.__email

    def get_contact_number(self):
        return self.__contact_number

    def get_role(self):
        return self.__role

    def get_salary(self):
        return self.__salary

    # Setters
    def set_employee_name(self, employee_name):
        self.__employee_name = employee_name

    def set_email(self, email):
        self.__email = email

    def set_contact_number(self, contact_number):
        self.__contact_number = contact_number

    def set_role(self, role):
        self.__role = role

    def set_salary(self, salary):
        self.__salary = salary

    def __str__(self):
        return f"Employee ID: {self.__employee_id}, Employee Name: {self.__employee_name}, Email: {self.__email}, Contact Number: {self.__contact_number}, Role: {self.__role}, Salary: {self.__salary}"

