#!/usr/bin/python3
import json
import os

from napalm import get_network_driver


def print_json(vals):
    print(json.dumps(vals, sort_keys=True, indent=4, separators=(",", ": ")))


driver = get_network_driver("digineo_procurve")

key_file = os.path.expanduser("~/.ssh/id_rsa")

device = driver(
    os.environ.get("SWITCH_IP"),
    "manager",
    password=None,
    optional_args={
        "use_keys": True,
        "key_file": key_file,
        "session_log": "/tmp/napalm",
    },
)
device.open()
try:
    print_json(device.get_environment())

    print_json(device.get_facts())

    print_json(device.get_lldp_neighbors())

finally:
    device.close()
