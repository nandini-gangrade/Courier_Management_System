# entity/courier.py

class Courier:
    def __init__(self, courier_id, sender_name, sender_address, receiver_name, receiver_address, weight, status, tracking_number, delivery_date, user_id):
        self.__courier_id = courier_id
        self.__sender_name = sender_name
        self.__sender_address = sender_address
        self.__receiver_name = receiver_name
        self.__receiver_address = receiver_address
        self.__weight = weight
        self.__status = status
        self.__tracking_number = tracking_number
        self.__delivery_date = delivery_date
        self.__user_id = user_id

    # Getters
    def get_courier_id(self):
        return self.__courier_id

    def get_sender_name(self):
        return self.__sender_name

    def get_sender_address(self):
        return self.__sender_address

    def get_receiver_name(self):
        return self.__receiver_name

    def get_receiver_address(self):
        return self.__receiver_address

    def get_weight(self):
        return self.__weight

    def get_status(self):
        return self.__status

    def get_tracking_number(self):
        return self.__tracking_number

    def get_delivery_date(self):
        return self.__delivery_date

    def get_user_id(self):
        return self.__user_id

    # Setters
    def set_sender_name(self, sender_name):
        self.__sender_name = sender_name

    def set_sender_address(self, sender_address):
        self.__sender_address = sender_address

    def set_receiver_name(self, receiver_name):
        self.__receiver_name = receiver_name

    def set_receiver_address(self, receiver_address):
        self.__receiver_address = receiver_address

    def set_weight(self, weight):
        self.__weight = weight

    def set_status(self, status):
        self.__status = status

    def set_tracking_number(self, tracking_number):
        self.__tracking_number = tracking_number

    def set_delivery_date(self, delivery_date):
        self.__delivery_date = delivery_date

    def __str__(self):
        return f"Courier ID: {self.__courier_id}, Sender: {self.__sender_name}, Receiver: {self.__receiver_name}, Status: {self.__status}, Tracking Number: {self.__tracking_number}"
