try:
    import pathlib
except ImportError:
    import pathlib2 as pathlib

import napalm_digineo_procurve.queries.device_info
import napalm_digineo_procurve.queries.interfaces
import napalm_digineo_procurve.queries.lldp_neighbors


def load_asset(asset_name: str):
    p = pathlib.Path(__file__).parent / "assets" / asset_name
    return p.read_text()


def test_query_device_info():
    d = napalm_digineo_procurve.queries.device_info.parse_response(
        load_asset("display-device-manuinfo_example")
    )
    assert d.device_name == "HP J9774A 8p PoEP 10/100/1000-T"
    assert d.vendor_name == "HP"


def test_query_interfaces():
    d = napalm_digineo_procurve.queries.interfaces.parse_response(
        load_asset("interfaces-brief_example")
    )
    assert len(d) == 10
    assert d[:2] == [
        napalm_digineo_procurve.queries.interfaces.Interface(
            port_id="1",
            type="100/1000T",
            intrusion_alert="No",
            enabled="Yes",
            status="Down",
            mode="1000FDx",
            mdi_mode="MDI",
            flow_control="off",
        ),
        napalm_digineo_procurve.queries.interfaces.Interface(
            port_id="2",
            type="100/1000T",
            intrusion_alert="No",
            enabled="Yes",
            status="Up",
            mode="1000FDx",
            mdi_mode="MDIX",
            flow_control="off",
        ),
    ]


def test_query_lldp_neighbors():
    d = napalm_digineo_procurve.queries.lldp_neighbors.parse_response(
        load_asset("lldp-info-remote-device_example")
    )
    assert len(d) == 4
    assert d[1] == {
        "ChassisId": "172.16.2.14",
        "ChassisType": "network-address",
        "Local Port": "6",
        "PortDescr": "NET PORT",
        "PortId": "000413AAAAAA:P1",
        "PortType": "local",
        "SysName": "snom370",
        "System Capabilities Enabled": "bridge, telephone",
        "System Capabilities Supported": "bridge, telephone",
        "System Descr": "snom;snom370-SIP 8.7.5.35;lid:8.7.5.35",
    }
