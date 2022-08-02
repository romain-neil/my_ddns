import json

import requests

from connector.AbstractConnector import AbstractConnector
from util.dns.Record import Record
from util.text import success, error


def build_params(domain: str, record: Record) -> str:
    return json.dumps({
        "rrsets": [
            {
                "name": domain,
                "type": str.upper(record.record_type.name),
                "ttl": record.ttl,
                "changetype": "REPLACE",
                "records": [{
                    "content": record.content,
                    "disabled": False
                }]
            }
        ]
    })


class PowerDnsConnector(AbstractConnector):
    """
    Power DNS Connector
    @author Romain NEIL
    """

    def __init__(self, api_key: str, zone: str):
        self.instance_url = None
        self.password = None
        self.username = None

        self.api_key = api_key
        self.zone = zone

    def auth(self, username, password):
        # Api key for powerdsn is username
        self.api_key = username
        pass

    def set_instance(self, url):
        pass

    def update_dns(self, domain, ip):
        record = Record(ip)

        r = requests.patch(
            url="{0}/api/servers/localhost/zones/{1}".format(self.instance_url, self.zone),
            headers={"X-API-Key": self.api_key},
            data=build_params(domain, record)
        )

        if 200 <= r.status_code < 300:
            success(f"[SUCCESS] Make domain point to {record.content}")
        else:
            error(f"[ERROR] cannot update url. Reason : {r.reason}")
