import dataclasses
import typing

import netmiko

import napalm_digineo_procurve.templates.parser


@dataclasses.dataclass()
class Interface:
    port_id: str
    type: str
    intrusion_alert: str
    enabled: str
    status: str
    mode: str
    mdi_mode: str
    flow_control: str


def parse_response(raw_data: str) -> typing.Sequence[Interface]:
    d = napalm_digineo_procurve.templates.parser.parse(
        raw_data, "interfaces-brief"
    )
    return [Interface(*item) for item in d]


def query(device: netmiko.BaseConnection):
    return parse_response(device.send_command("show interfaces brief"))
