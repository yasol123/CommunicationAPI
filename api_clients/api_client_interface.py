from abc import ABC, abstractmethod

class APIClientInterface(ABC):
    
    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def make_api_request(self, endpoint: str, method: str = 'GET', data: dict = None) -> dict:
        pass
