# exceptions/custom_exceptions.py

class TrackingNumberNotFoundException(Exception):
    def __init__(self, message="Tracking number not found"):
        self.message = message
        super().__init__(self.message)

class InvalidEmployeeIdException(Exception):
    def __init__(self, message="Invalid employee ID"):
        self.message = message
        super().__init__(self.message)
