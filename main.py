import time
import sys

from connector.MailInABoxConnector import MailInABoxConnector
from util import get_public_ip


def main():
    current_ip = ""

    # Parse parameters
    domain = sys.argv[1]
    instance_url = sys.argv[2]

    username = sys.argv[3]
    password = sys.argv[4]

    connector = MailInABoxConnector()
    connector.auth(username, password)
    connector.set_instance(instance_url)

    while True:
        last_ip = get_public_ip()

        if last_ip != current_ip:
            print("Public ip is no longer anymore {0}, now it's {1}".format(current_ip, last_ip))

            current_ip = last_ip

            connector.update_dns(domain, current_ip)

        time.sleep(300)


if __name__ == "__main__":
    main()
