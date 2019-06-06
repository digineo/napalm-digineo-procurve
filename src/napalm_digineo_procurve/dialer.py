import napalm.base.exceptions
import netmiko


def dial(
    device_type, hostname, username, password, timeout, netmiko_optional_args=None
):
    # Override parent class method to remove the call to enable
    # privileged mode.
    if netmiko_optional_args is None:
        netmiko_optional_args = {}
    try:
        con = netmiko.ConnectHandler(
            device_type=device_type,
            host=hostname,
            username=username,
            password=password,
            timeout=timeout,
            **netmiko_optional_args
        )
    except netmiko.NetMikoTimeoutException:
        raise napalm.base.exceptions.ConnectionException(
            "Cannot connect to {}".format(hostname)
        )

    return con
