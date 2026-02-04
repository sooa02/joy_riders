from abc import ABC, abstractmethod
import requests

class APICaller(ABC):
    def downloadapi(self, url, headers, params):
        return requests.get(url, headers=headers, params=params)

    @abstractmethod
    def getdata(self, *args):
        pass