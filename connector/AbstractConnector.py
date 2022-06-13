from abc import abstractmethod, ABC


class AbstractConnector(ABC):

    @abstractmethod
    def auth(self, username, password):
        """
        Authenticate to the service

        Parameters
        ----------
        username : str
            The service username
        password: str
            The service password
        """
        pass

    @abstractmethod
    def set_instance(self, url):
        """
        Set the instance url

        Parameters
        ----------
        url : str
            The instance url
        """
        pass

    @abstractmethod
    def update_dns(self, domain, ip):
        """
        Update the dns ip to the service

        Parameters
        ----------
        domain : str
        ip : str
        """
        pass
