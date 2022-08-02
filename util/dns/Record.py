import ipaddress
from enum import Enum
from typing import Union


class RecordType(Enum):
    """
    Enum to use when define a dns record type
    """
    A = 1
    AAAA = 2
    PTR = 3
    CNAME = 4
    NS = 5

    # Keep last
    DEFAULT = 0


class Record:
    """
    Class which represent a DNS record
    """

    def __init__(self, content: str, record_type: RecordType = RecordType.DEFAULT, ttl: int = 86400):
        self.record_type = record_type
        self.ttl = ttl
        self.content = content

    def is_ip(self):
        valid = False

        try:
            ipaddress.ip_address(self.content)
            valid = True
        except ValueError:
            pass

        return valid

    def get_ip(self) -> Union[ipaddress.IPv4Address, ipaddress.IPv6Address]:
        return ipaddress.ip_address(self.content)

    def get_record_type(self):
        """
        Return the record type corresponding to value passed in constructor (A, AAAA or CNAME)
        """
        try:
            ipaddress.IPv4Address(self.content)
            return RecordType.A
        except ValueError:
            try:
                ipaddress.IPv6Address(self.content)
                return RecordType.AAAA
            except ValueError:
                return RecordType.CNAME
