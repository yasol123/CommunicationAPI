from abc import ABC, abstractmethod

class EmailServiceInterface(ABC):
    
    @abstractmethod
    def send_email(self, to_email: str, subject: str, body: str) -> dict:
        pass

    @abstractmethod
    def send_welcome_email(self, to_email: str) -> dict:
        pass

    @abstractmethod
    def send_billing_email(self, to_email: str) -> dict:
        pass

    @abstractmethod
    def send_notification_email(self, to_email: str) -> dict:
        pass
