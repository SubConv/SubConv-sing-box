from ..common import IpVersion, Network, Protocol

from dataclasses import dataclass

@dataclass
class Rule:
    inbound: list[str]
    ip_version: IpVersion = None
    network: Network = None
    auth_user: list[str] = None
    protocol: list[Protocol] = None
    domain: list[str] = None
    domain_suffix: list[str] = None
    domain_keyword: list[str] = None
    domain_regex: list[str] = None
    source_ip_cidr: list[str] = None
    source_ip_is_private: bool = None
    source_port: list[int] = None
    source_port_range: list[str] = None
    port: list[int] = None
    port_range: list[str] = None
    process_name: list[str] = None
    process_path: list[str] = None
    package_name: list[str] = None
    user: list[str] = None
    user_id: list[int] = None
    clash_mode: str = None
    wifi_ssid: list[str] = None
    wifi_bssid: list[str] = None
    rule_set: list[str] = None
    rule_set_ip_cidr_match_source: bool = None
    invert: bool = None
    outbound: list[str] = None
    geoip: list[str] = None
    ip_cidr: list[str] = None
    ip_is_private: bool = None