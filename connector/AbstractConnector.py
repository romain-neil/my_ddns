from abc import abstractmethod, ABC


class AbstractConnector(ABC):

    @abstractmethod
    def auth(self, username, password):
        """
        Authenticate to the service
        :param username:
        :param password:
        :return:
        """
        pass

    @abstractmethod
    def set_instance(self, url):
        """Set the instance url"""
        pass

    @abstractmethod
    def update_dns(self, domain, ip):
        """Update the dns ip to the service"""
        pass
