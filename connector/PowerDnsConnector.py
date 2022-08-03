import datetime
import json

import requests

from connector.AbstractConnector import AbstractConnector
from util.dns.Record import Record
from util.text import success, error, warn, info


class PowerDnsConnector(AbstractConnector):
    """
    Power DNS Connector
    @author Romain NEIL
    """

    def __init__(self):
        self.instance_url = None
        self.password = None
        self.username = None

        self.params = {}

    def get_optionals_parameters(self):
        return [
            'api_key',
            'domain',
            'zone'
        ]

    def set_optional_parameter(self, param_name: str, param_value: str):
        self.params[param_name] = param_value

    def build_params(self, domain: str, record: Record) -> str:
        return json.dumps({
            "rrsets":
                [{
                    "name": domain,
                    "type": str.upper(record.record_type.name),
                    "ttl": record.ttl,
                    "changetype": "REPLACE",
                    "records": [{
                        "content": record.content,
                        "disabled": False
                    }],
                    "comments": [{
                        "content": "modify record",
                        "account": f"{self.params.get('user')}",
                        "modified_at": int(round(datetime.datetime.now().timestamp()))
                    }]
                }]
        })

    def auth(self, username, password):
        pass

    def set_instance(self, url):
        self.instance_url = url

    def update_dns(self, domain, ip):
        record = Record(str(ip))
        record.set_ip_record_type()

        data = self.build_params(domain, record)

        r = requests.patch(
            url=f"{self.params.get('instance-url')}/api/v1/servers/localhost/zones/{self.params.get('zone')}",
            headers={"X-API-Key": self.params.get('api-key')},
            data=data
        )

        if 200 <= r.status_code < 300:
            success(f"[SUCCESS] Make domain point to {record.content}")
        else:
            error(f"[ERROR] cannot update url. Reason : {r.reason}")
            warn(f"The url was {r.url}")
            info(f"The json object was : {data}")
