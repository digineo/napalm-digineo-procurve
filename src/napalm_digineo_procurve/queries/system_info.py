import attr
import netmiko

import napalm_digineo_procurve.templates.parser


@attr.s()
class SystemInformation:
    hostname = attr.ib()  # type: str
    os_version = attr.ib()  # type: str
    serial_number = attr.ib()  # type: str

    cpu_utilization = attr.ib()  # type: float

    memory_total = attr.ib()  # type: int
    memory_free = attr.ib()  # type: int


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
