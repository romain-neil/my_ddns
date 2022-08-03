import ipaddress

import requests


def get_public_ip():
    r = requests.get(url="https://api.ipify.org/?format=json")
    data = r.json()

    return data['ip']


def get_public_ipv6():
    r = requests.get(url="https://api64.ipify.org/?format=json")
    data = r.json()
    ip = ''

    try:
        ip = ipaddress.IPv6Address(data['ip'])
    except ValueError:
        pass

    return ip


class BGColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def info(text: str):
    print(f"{BGColors.OKBLUE}{text}{BGColors.ENDC}")


def warn(text: str):
    print(f"{BGColors.WARNING}{text}{BGColors.ENDC}")


def error(text: str):
    print(f"{BGColors.FAIL}{text}{BGColors.ENDC}")


def success(text: str):
    print(f"{BGColors.OKGREEN}{text}{BGColors.ENDC}")
