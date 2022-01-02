import requests

from connector.AbstractConnector import AbstractConnector
from util import success, error


class MailInABoxConnector(AbstractConnector):

    def __init__(self):
        self.instance_url = None
        self.password = None
        self.username = None

    def auth(self, username, password):
        self.username = username
        self.password = password

    def set_instance(self, url):
        self.instance_url = url

    def update_dns(self, domain, ip):
        r = requests.put(
            url="https://{0}/admin/dns/custom/{1}".format(self.instance_url, domain),
            auth=(self.username, self.password)
        )

        if 200 <= r.status_code < 300:
            success(f"[SUCCESS] Make new ip point to {domain}")
        else:
            error(f"Error: cannot update url. Reason : {r.reason}")
