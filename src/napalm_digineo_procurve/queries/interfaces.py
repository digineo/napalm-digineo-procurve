import typing

import attr
import netmiko

import napalm_digineo_procurve.templates.parser


@attr.s()
class Interface:
    port_id = attr.ib()  # type: str
    type = attr.ib()  # type: str
    intrusion_alert = attr.ib()  # type: str
    enabled = attr.ib()  # type: str
    status = attr.ib()  # type: str
    mode = attr.ib()  # type: str
    mdi_mode = attr.ib()  # type: str
    flow_control = attr.ib()  # type: str


def parse_response(raw_data: str) -> typing.Sequence[Interface]:
    d = napalm_digineo_procurve.templates.parser.parse(raw_data, "interfaces-brief")
    return [Interface(*item) for item in d]


def query(device: netmiko.BaseConnection):
    return parse_response(device.send_command("show interfaces brief"))
