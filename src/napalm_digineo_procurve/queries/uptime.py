import re

import netmiko


class UnexpectedResponse(Exception):
    """Device responded in an unexpected way."""


def query(device: netmiko.BaseConnection):
    """Fetch device uptime and return the value in seconds."""
    r = device.send_command("show uptime")

    m = re.match(r"^(?P<d>\d+):(?P<H>\d+):(?P<M>\d+):(?P<S>\d+).(?P<f>\d+)$", r)
    if not m:
        raise UnexpectedResponse()

    factors = {"d": 86400.0, "H": 3600.0, "M": 60.0, "S": 1.0, "f": 0.1}
    return sum(factors[k] * float(v) for k, v in m.groupdict().items())
