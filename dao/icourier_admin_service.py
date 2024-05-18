# icourier_admin_service.py

from abc import ABC, abstractmethod
from entity import Employee

class ICourierAdminService(ABC):
    @abstractmethod
    def add_courier_staff(self, name: str, contact_number: str) -> int:
        pass
