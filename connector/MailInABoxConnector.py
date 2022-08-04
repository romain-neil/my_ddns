import requests

from connector.AbstractConnector import AbstractConnector
from util.text import success, error


class MailInABoxConnector(AbstractConnector):
    """
    Connector for a mail in a box server
    """

    def __init__(self):
        self.instance_url = None
        self.password = None
        self.username = None

        self.params = {}

    def get_optionals_parameters(self) -> list[str]:
        return [
            'username',
            'password',
            'instance-url'
        ]

    def set_optional_parameter(self, param_name: str, param_value: str):
        self.params[param_name] = param_value

    def update_dns(self, domain, ip):
        r = requests.put(
            url=f"https://{self.params.get('password')}/admin/dns/custom/{domain}",
            auth=(self.params.get('username'), self.params.get('password'))
        )

        if 200 <= r.status_code < 300:
            success(f"[SUCCESS] Make new ip point to {domain}")
        else:
            error(f"Error: cannot update url. Reason : {r.reason}")
