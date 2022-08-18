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

    parameters = parse_params()

    # Set connector independant vars
    domain = parameters.get('domain')
    file = parameters.get('file')

    # Check if domain parameter is a filename
    if domain is None and file is not None:
        if os.path.exists('./' + file):
            domain = []

            with open('./' + file) as file:
                domain.append(line.rstrip() for line in file)

    connector = PowerDnsConnector()

    # For each parameter, set it in the connector
    for param in parameters:
        connector.set_optional_parameter(param, parameters.get(param))

    # Tableau de la liste des ip à mettre à jour
    ip_to_update_list: list = []

    should_update_dns = False
    
    should_update_ipv4 = True
    should_update_ipv6 = True

    only_update = parameters.get('only-update')
    if only_update is not None:
        #  --only-update=ipv4 or ipv6
        if only_update == 'ipv4':
            should_update_ipv6 = False
        else:
            should_update_ipv4 = False

    while True:
        last_ip = get_public_ip()
        last_ipv6 = get_public_ipv6()

        if last_ip != current_ip and should_update_ipv4:
            ip_to_update_list.append(last_ip)
            current_ip = last_ip
            should_update_dns = True
            info(f"Public ip is no longer anymore {current_ip}, now it's {last_ip}")

        if last_ipv6 != current_ipv6 and should_update_ipv6:
            ip_to_update_list.append(last_ipv6)
            current_ipv6 = last_ipv6
            should_update_dns = True
            info(f"Public ipv6 is no longer anymore {current_ipv6}, now it's {last_ipv6}")

        if should_update_dns:
            if isinstance(domain, list):
                for d in domain:
                    for ip in ip_to_update_list:
                        connector.update_dns(d, ip)
            else:
                for ip in ip_to_update_list:
                    connector.update_dns(domain, ip)

            should_update_dns = False

        time.sleep(300)


if __name__ == "__main__":
    main()
