import dataclasses

import netmiko

import napalm_digineo_procurve.templates.parser


@dataclasses.dataclass()
class SystemInformation:
    hostname: str
    os_version: str
    serial_number: str

    cpu_utilization: float

    memory_total: int
    memory_free: int


def parse_response(raw_data: str) -> SystemInformation:
    d = napalm_digineo_procurve.templates.parser.parse(
        raw_data, "system-information"
    ).pop()
    return SystemInformation(
        hostname=d[0],
        os_version=d[1],
        serial_number=d[2],
        cpu_utilization=float(d[3]) / 100,
        memory_total=int(d[4].replace(",", "")),
        memory_free=int(d[5].replace(",", "")),
    )


def query(device: netmiko.BaseConnection):
    return parse_response(device.send_command("show system information"))
