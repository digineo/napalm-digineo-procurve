import typing

import netmiko

import napalm_digineo_procurve.templates.parser


def parse_response(raw_data: str) -> typing.List[typing.Mapping[str, str]]:
    d = napalm_digineo_procurve.templates.parser.parse(
        raw_data, "lldp-info-remote-device"
    )
    return [dict(zip(e[0], (a.strip() for a in e[1]))) for e in d]


def query(device: netmiko.BaseConnection):
    return parse_response(device.send_command("show lldp info remote-device detail"))
