from ..common import IpVersion, Network, Protocol

from dataclasses import dataclass

import typing

def rule_set(type: str):
    def wrapper(cls):
        orig_init = cls.__init__
        def __init__(self, **kwargs):
            orig_init(self, type=type, **kwargs)
        cls.__init__ = __init__
        return cls
    return wrapper

@dataclass(kw_only=True)
class Rule_set:
    type: str
    tag: str

@dataclass(kw_only=True)
class HeadlessRule:
    query_type: typing.List[typing.Union[int, str]] = None
    network: list[str] = None
    domain: list[str] = None
    domain_suffix: list[str] = None
    domain_keyword: list[str] = None
    domain_regex: list[str] = None
    source_ip_cidr: list[str] = None
    ip_cidr: list[str] = None
    source_port: list[int] = None
    source_port_range: list[str] = None
    port: list[int] = None
    port_range: list[str] = None
    process_name: list[str] = None
    process_path: list[str] = None
    package_name: list[str] = None
    wifi_ssid: list[str] = None
    wifi_bssid: list[str] = None
    invert: bool = None

@rule_set("inline")
class Inline:
    rules: list[HeadlessRule]

@rule_set("local")
class Local:
    format: str
    path: str

@rule_set("remote")
class  Remote:
    format: str
    url: str
    download_detour: str = None
    update_interval: str =None
