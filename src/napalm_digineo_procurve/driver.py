import collections

import napalm.base
import napalm.base.exceptions
import napalm.base.netmiko_helpers

import napalm_digineo_procurve.device
import napalm_digineo_procurve.dialer
import napalm_digineo_procurve.queries.uptime


class NetworkDriver(napalm.base.NetworkDriver):
    def __init__(self, hostname, username, password, timeout=60, optional_args=None):
        if optional_args is None:
            optional_args = {}
        self.hostname = hostname
        self.username = username
        self.password = password
        self.timeout = timeout

        self.netmiko_optional_args = napalm.base.netmiko_helpers.netmiko_args(
            optional_args
        )
        self.netmiko_optional_args.setdefault("port", 22)

        self.device = None

    def _netmiko_open(self, device_type, netmiko_optional_args=None):
        return napalm_digineo_procurve.dialer.dial(
            device_type,
            self.hostname,
            self.username,
            self.password,
            self.timeout,
            netmiko_optional_args,
        )

    def open(self):
        self.device = self._netmiko_open(
            "hp_procurve_ssh", netmiko_optional_args=self.netmiko_optional_args
        )

    def close(self):
        self.device.disconnect()
        self.device = None

    def is_alive(self):
        if self.device is None:
            return {"is_alive": False}
        return {"is_alive": self.device.is_alive()}

    def get_environment(self):
        s = napalm_digineo_procurve.device.get_system_information(self.device)

        return {
            "fans": {},
            "temperature": {},
            "power": {},
            "cpu": {"0": {"%usage": s.cpu_utilization * 100.0}},
            "memory": {"available_ram": s.memory_total, "used_ram": s.memory_free},
        }

    def get_facts(self):
        s = napalm_digineo_procurve.device.get_system_information(self.device)
        d = napalm_digineo_procurve.device.get_device_manufacturer_info(self.device)
        i = napalm_digineo_procurve.device.get_interfaces(self.device)

        try:
            uptime = napalm_digineo_procurve.device.get_uptime(self.device)
        except napalm_digineo_procurve.queries.uptime.UnexpectedResponse:
            # RuntimeError is most likely caused by the fact that the active
            # user can't query the uptime. Though luck.
            uptime = 0

        return {
            "uptime": uptime,
            "vendor": d.vendor_name,
            "os_version": s.os_version,
            "serial_number": s.serial_number,
            "model": d.device_name,
            "hostname": s.hostname,
            "fqdn": s.hostname,
            "interface_list": [x.port_id for x in i],
        }

    def get_lldp_neighbors(self):
        d = napalm_digineo_procurve.device.get_lldp_neighbors(self.device)

        ports = collections.defaultdict(list)
        for item in d:
            ports[item["Local Port"]].append(
                {"hostname": item["SysName"], "port": item["PortId"]}
            )

        return dict(ports)
