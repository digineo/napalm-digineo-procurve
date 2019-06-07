import typing

try:
    import importlib.resources as importlib_resources
except ImportError:
    import importlib_resources
import textfsm

assets_package = ".".join(__name__.split(".")[:-1] + ["assets"])


def open_asset(asset_name: str) -> typing.TextIO:
    return importlib_resources.open_text(assets_package, asset_name)


def read_template(template_name: str) -> textfsm.TextFSM:
    with open_asset(template_name) as fp:
        return textfsm.TextFSM(fp)
