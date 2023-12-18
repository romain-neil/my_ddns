import json

import requests

from connector.AbstractConnector import AbstractConnector
from util.dns.Record import Record
from util.text import success, error


class CloudflareConnector(AbstractConnector):
    """
    Cloudflare connector
    @author Romain NEIL
    """

    def __init__(self):
        self.instance_url = "api.cloudflare.com/client"
        self.api_version = "v4"

        self.params = {}

    def get_optionals_parameters(self) -> list[str]:
        return [
            'has_api_key',
            'domain',
            'ttl',
            'proxied'
        ]

    def set_optional_parameter(self, param_name: str, param_value: str):
        self.params[param_name] = param_value

    def build_headers(self):
        auth_header = 'X-Auth-Email'

        if self.params.get('has_api_key', False):
            auth_header = 'X-Api-Key'

        return {
            # auth_header: self.params.
        }

    def build_params(self, domain: str, record: Record) -> str:
        return json.dumps({
            "content": record.get_ip(),
            "name": domain,
            "type": record.get_record_type().name,
            "ttl": self.params.get('ttl', 3600),
            "proxied": self.params.get('proxied', 'false')
        })

    def update_dns(self, domain: str, ip: str):
        record = Record(str(ip))

        r = requests.put(
            url=f"https://{self.instance_url}/{self.api_version}/zones/zone_identifier/dns_records/identifier",
            headers=self.build_headers()
        )

        if 200 <= r.status_code < 300:
            success(f"[SUCCESS]: Update domain to {record.content}")
        else:
            resp = json.loads(r.content)

            error(f"[ERROR]: Cannot update domain")
            error(f"{resp.error.message}")
