from connector.AbstractConnector import AbstractConnector


class CloudflareConnector(AbstractConnector):
    """
    Cloudflare connector
    @author Romain NEIL
    """

    def __init__(self):
        self.instance_url = None
        self.password = None
        self.username = None

        self.params = {}

    def get_optionals_parameters(self) -> list[str]:
        pass

    def set_optional_parameter(self, param_name: str, param_value: str):
        pass

    def update_dns(self, domain: str, ip: str):
        pass
