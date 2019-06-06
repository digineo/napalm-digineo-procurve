import dataclasses

import netmiko

import napalm_digineo_procurve.templates.parser


@dataclasses.dataclass()
class DeviceInformation:
    device_name: str
    vendor_name: str


def parse_response(raw_data: str) -> DeviceInformation:
    d = napalm_digineo_procurve.templates.parser.parse(
        raw_data, "display-device-manuinfo"
    ).pop()
    return DeviceInformation(device_name=d[0].strip(), vendor_name=d[1].strip())


def query(device: netmiko.BaseConnection):
    return parse_response(device.send_command("display device manuinfo"))
