from ..common import IpVersion, Network, Protocol

from pydantic import BaseModel
from typing import Optional

class Rule(BaseModel):
    inbound: Optional[list[str]] = None
    ip_version: Optional[IpVersion] = None
    network: Optional[Network] = None
    auth_user: Optional[list[str]] = None
    protocol: Optional[list[Protocol]] = None
    domain: Optional[list[str]] = None
    domain_suffix: Optional[list[str]] = None
    domain_keyword: Optional[list[str]] = None
    domain_regex: Optional[list[str]] = None
    source_ip_cidr: Optional[list[str]] = None
    source_ip_is_private: Optional[bool] = None
    source_port: Optional[list[int]] = None
    source_port_range: Optional[list[str]] = None
    port: Optional[list[int]] = None
    port_range: Optional[list[str]] = None
    process_name: Optional[list[str]] = None
    process_path: Optional[list[str]] = None
    package_name: Optional[list[str]] = None
    user: Optional[list[str]] = None
    user_id: Optional[list[int]] = None
    clash_mode: Optional[str] = None
    wifi_ssid: Optional[list[str]] = None
    wifi_bssid: Optional[list[str]] = None
    rule_set: Optional[list[str]] = None
    rule_set_ip_cidr_match_source: Optional[bool] = None
    invert: Optional[bool] = None
    outbound: Optional[str] = None
    geoip: Optional[list[str]] = None
    ip_cidr: Optional[list[str]] = None
    ip_is_private: Optional[bool] = None