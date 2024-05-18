class User:
    def __init__(self, user_id, user_name, email, password, contact_number, address):
        self.__user_id = user_id
        self.__user_name = user_name
        self.__email = email
        self.__password = password
        self.__contact_number = contact_number
        self.__address = address

    # Getters
    def get_user_id(self):
        return self.__user_id

    def get_user_name(self):
        return self.__user_name

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def get_contact_number(self):
        return self.__contact_number

    def get_address(self):
        return self.__address

    # Setters
    def set_user_name(self, user_name):
        self.__user_name = user_name

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password

    def set_contact_number(self, contact_number):
        self.__contact_number = contact_number

    def set_address(self, address):
        self.__address = address

    def __str__(self):
        return f"User ID: {self.__user_id}, User Name: {self.__user_name}, Email: {self.__email}, Contact Number: {self.__contact_number}, Address: {self.__address}"
