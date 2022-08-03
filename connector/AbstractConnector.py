from abc import abstractmethod, ABC


class AbstractConnector(ABC):
    """
    Represent an abstract connector, to be inherited by dns software' connectors
    """

    @abstractmethod
    def get_optionals_parameters(self) -> list[str]:
        """
        Define a list of optionals parameters required by the connector
        The function return a list of parameter name, set in the connnector by calling set_optional_param(param_name, param_value)
        """
        pass

    @abstractmethod
    def set_optional_parameter(self, param_name: str, param_value: str):
        """
        @see get_optionals_parameters
        """
        pass

    @abstractmethod
    def auth(self, username: str, password: str):
        """
        Authenticate to the service

        @deprecated

        :param username:
        :param password:
        :return:
        """
        pass

    @abstractmethod
    def set_instance(self, url: str):
        """
        Set the instance url

        @deprecated

        """
        pass

    @abstractmethod
    def update_dns(self, domain: str, ip: str):
        """Update the dns ip to the service"""
        pass
