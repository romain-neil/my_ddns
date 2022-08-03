import os.path
import time
import sys

from connector.MailInABoxConnector import MailInABoxConnector
from connector.PowerDnsConnector import PowerDnsConnector
from util.text import get_public_ip, get_public_ipv6, info


def parse_params() -> dict:
    parsed_params_list = {}

    for p in sys.argv:
        if p.startswith('--'):
            p = p.removeprefix('--')
            param: list[str] = p.split('=')

            parsed_params_list[param[0]] = param[1]

    return parsed_params_list


def main():
    current_ip = ""
    current_ipv6 = ""
    domain = None

    parameters = parse_params()

    # Set connector independant vars
    domain_or_filename = parameters.get('domain')

    # Check if domain parameter is a filename
    if os.path.exists('./' + domain_or_filename):
        domain = []

        with open('./' + domain_or_filename) as file:
            domain.append(line.rstrip() for line in file)

    else:
        domain = domain_or_filename

    connector = PowerDnsConnector()

    # For each parameter, set it in the connector
    for param in parameters:
        connector.set_optional_parameter(param[0], param[1])

    # Tableau de la liste des ip à mettre à jour
    ip_to_update_list: list = []

    while True:
        last_ip = get_public_ip()
        last_ipv6 = get_public_ipv6()

        if last_ip != current_ip:
            ip_to_update_list.append(last_ip)
            current_ip = last_ip
            info(f"Public ip is no longer anymore {current_ip}, now it's {last_ip}")

        if last_ipv6 != current_ipv6:
            ip_to_update_list.append(last_ipv6)
            current_ipv6 = last_ipv6
            info(f"Public ipv6 is no longer anymore {current_ipv6}, now it's {last_ipv6}")

        if isinstance(domain, list):
            for d in domain:
                for ip in ip_to_update_list:
                    connector.update_dns(d, ip)
        else:
            for ip in ip_to_update_list:
                connector.update_dns(domain_or_filename, ip)

        time.sleep(300)


if __name__ == "__main__":
    main()
