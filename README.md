# my_ddns
Open Source DDNS, with connectors

## Requirements

- Python 3^
- pip

## Installation

Use pip and the requirements.txt file

## Usage

For now, connector used is hardcoded. Modify to meet your needs.

(Old mail in a box connector command, to be modified in short future :)
`python3 main.py {ddns domain} {miab domain} {username} {password}`

For a normal usage, the parameters have to be specified as `--parameter-name=parameter-value`

Here a PowerDNS command exemple:
`python3 main.py --domain="test.exemple.org." --instance-url="https://pdns.exemple.org" --zone="exemple.org" --user="user" --api-key="some_api_key"`

The script will automatically check each 300s (5min) for ip update

## Compatibility

You will find [here](compatibility.md) the basic compatibility list, with a little part of roadmap