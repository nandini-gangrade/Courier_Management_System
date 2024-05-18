# icourier_user_service.py

from abc import ABC, abstractmethod
from entity.courier import Courier

class ICourierUserService(ABC):
    @abstractmethod
    def place_order(self, courier_obj: Courier) -> str:
        pass

    @abstractmethod
    def get_order_status(self, tracking_number: str) -> str:
        pass

    @abstractmethod
    def cancel_order(self, tracking_number: str) -> bool:
        pass

    @abstractmethod
    def get_assigned_order(self, courier_staff_id: int) -> list:
        pass
