import typing

import netmiko

import napalm_digineo_procurve.queries.interfaces
import napalm_digineo_procurve.queries.lldp_neighbors
import napalm_digineo_procurve.queries.device_info
import napalm_digineo_procurve.queries.system_info
import napalm_digineo_procurve.queries.uptime


def get_uptime(device: netmiko.BaseConnection) -> float:
    return napalm_digineo_procurve.queries.uptime.query(device)


def get_system_information(
    device: netmiko.BaseConnection
) -> napalm_digineo_procurve.queries.system_info.SystemInformation:
    return napalm_digineo_procurve.queries.system_info.query(device)


def get_device_manufacturer_info(
    device: netmiko.BaseConnection
) -> napalm_digineo_procurve.queries.device_info.DeviceInformation:
    return napalm_digineo_procurve.queries.device_info.query(device)


def get_interfaces(
    device: netmiko.BaseConnection
) -> typing.Sequence[napalm_digineo_procurve.queries.interfaces.Interface]:
    return napalm_digineo_procurve.queries.interfaces.query(device)


def get_lldp_neighbors(
    device: netmiko.BaseConnection
) -> typing.List[typing.Mapping[str, str]]:
    return napalm_digineo_procurve.queries.lldp_neighbors.query(device)
