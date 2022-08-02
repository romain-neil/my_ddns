import requests


def get_public_ip():
    r = requests.get(url="https://api.ipify.org/?format=json")
    data = r.json()

    return data['ip']


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


def warn(text):
    print(f"{BGColors.WARNING}{text}{BGColors.ENDC}")


def error(text):
    print(f"{BGColors.FAIL}{text}{BGColors.ENDC}")


def success(text):
    print(f"{BGColors.OKGREEN}{text}{BGColors.ENDC}")

