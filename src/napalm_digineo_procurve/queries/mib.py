import typing

import netmiko


def read_mib_value(device: netmiko.BaseConnection, oid: str) -> str:
    output = device.send_command("getMIB {}".format(oid))

    if output.strip() == "{}: No such name.".format(oid):
        raise RuntimeError(output)

    return output.split(" = ")[1].strip()


def walk_mib_value(
    device: netmiko.BaseConnection, oid: str
) -> typing.Generator[str, str, None]:
    output = device.send_command("walkMIB {}".format(oid))

    if output.strip() == "{}: No such name.":
        raise RuntimeError(output)

    return (l.split(" = ") for l in output.split("\n"))
