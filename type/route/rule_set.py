from ..common import IpVersion, Network, Protocol

from pydantic import BaseModel
from typing import Optional, Union

def rule_set(type: str):
    def wrapper(cls):
        orig_init = cls.__init__
        def __init__(self, **kwargs):
            orig_init(self, type=type, **kwargs)
        cls.__init__ = __init__
        return cls
    return wrapper

class Rule_set(BaseModel):
    type: str
    tag: str

class HeadlessRule(BaseModel):
    query_type: Optional[list[Union[int, str]]] = None
    network: Optional[list[str]] = None
    domain: Optional[list[str]] = None
    domain_suffix: Optional[list[str]] = None
    domain_keyword: Optional[list[str]] = None
    domain_regex: Optional[list[str]] = None
    source_ip_cidr: Optional[list[str]] = None
    ip_cidr: Optional[list[str]] = None
    source_port: Optional[list[int]] = None
    source_port_range: Optional[list[str]] = None
    port: Optional[list[int]] = None
    port_range: Optional[list[str]] = None
    process_name: Optional[list[str]] = None
    process_path: Optional[list[str]] = None
    package_name: Optional[list[str]] = None
    wifi_ssid: Optional[list[str]] = None
    wifi_bssid: Optional[list[str]] = None
    invert: Optional[bool] = None

@rule_set("inline")
class Inline(Rule_set):
    rules: list[HeadlessRule]

@rule_set("local")
class Local(Rule_set):
    format: str
    path: str

@rule_set("remote")
class Remote(Rule_set):
    format: str
    url: str
    download_detour: Optional[str] = None
    update_interval: Optional[str] = None
