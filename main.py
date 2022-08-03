import os.path
import time
import sys

from connector.MailInABoxConnector import MailInABoxConnector
from connector.PowerDnsConnector import PowerDnsConnector
from util.text import get_public_ip


def main():
    current_ip = ""
    domain = None

    # Parse parameters
    domain_or_filename = sys.argv[1]
    instance_url = sys.argv[2]

    username = sys.argv[3]
    password = sys.argv[4]

    # TODO: parse parameters (--api-key=... --user=... etc)
    api_key = ''
    zone = ''
    user = ''

    # Check if domain parameter is a filename
    if os.path.exists('./' + domain_or_filename):
        domain = []

        with open('./' + domain_or_filename) as file:
            domain.append(line.rstrip() for line in file)

    else:
        domain = domain_or_filename

    connector = PowerDnsConnector()

    # Set optionals parameters for powerdns connector
    connector.set_optional_parameter('api_key', api_key)
    connector.set_optional_parameter('zone', zone)

    connector.set_instance(instance_url)

    while True:
        last_ip = get_public_ip()

        if last_ip != current_ip:
            print("Public ip is no longer anymore {0}, now it's {1}".format(current_ip, last_ip))

            current_ip = last_ip

            if isinstance(domain, list):
                for d in domain:
                    connector.update_dns(d, current_ip)
            else:
                connector.update_dns(domain, current_ip)

        time.sleep(300)


if __name__ == "__main__":
    main()
