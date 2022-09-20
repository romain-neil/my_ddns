import os.path
import time
import sys

from typing import List

from connector.MailInABoxConnector import MailInABoxConnector
from connector.PowerDnsConnector import PowerDnsConnector
from util.text import get_public_ip, get_public_ipv6, info


def parse_params(param_list: List[str]) -> dict:
    parsed_params_list = {}

    for p in param_list:
        if not p.__contains__('='):
            continue
        if p.startswith('--'):
            p = p.removeprefix('--')

        param: List[str] = p.split('=')
        parsed_params_list[str(param[0])] = str(param[1])

    return parsed_params_list


def main():
    current_ip = ""
    current_ipv6 = ""

    parameters = {}

    if len(sys.argv) > 1:
        parameters = parse_params(sys.argv)
    else:
        # Parameters are stored in a config file
        params = []
        with open('./config.txt') as file:
            for line in file:
                params.append(line.rstrip())

        parameters = parse_params(params)

    # Set connector independant vars
    domain = str(parameters.get('domain'))
    file = str(parameters.get('file'))

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

    while True:
        last_ip = get_public_ip()
        last_ipv6 = get_public_ipv6()

        if last_ip != current_ip:
            ip_to_update_list.append(last_ip)
            current_ip = last_ip
            should_update_dns = True
            info(f"Public ip is no longer anymore {current_ip}, now it's {last_ip}")

        if last_ipv6 != current_ipv6:
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
