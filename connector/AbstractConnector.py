from abc import abstractmethod, ABC


class AbstractConnector(ABC):

    @abstractmethod
    def auth(self, username, password):
        pass

    @abstractmethod
    def set_instance(self, url):
        pass

    @abstractmethod
    def update_dns(self, domain, ip):
        pass
