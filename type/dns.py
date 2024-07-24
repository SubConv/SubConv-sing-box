from .common import Strategy, IpVersion, Network, Protocol
from typing import Optional, Union

from pydantic import BaseModel

class Server(BaseModel):
    address: str
    tag: Optional[str] = None
    address_resolver: Optional[str] = None
    address_strategy: Optional[Strategy] = None
    strategy: Optional[Strategy] = None
    detour: Optional[str] = None
    client_subnet: Optional[str] = None

class Rule(BaseModel):
    inbound: Optional[list[str]] = None
    server: str
    ip_version: Optional[IpVersion] = None
    query_type: Optional[list[Union[int, str]]] = None
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
    outbound: Optional[list[str]] = None
    disable_cache: Optional[bool] = None
    rewrite_ttl: Optional[int] = None
    client_subnet: Optional[str] = None
    geoip: Optional[list[str]] = None
    ip_cidr: Optional[list[str]] = None
    ip_is_private: Optional[bool] = None
    rule_set_ip_cidr_accept_empty: Optional[bool] = None


class Fakeip(BaseModel):
    enabled: bool = True
    inet4_range: Optional[str] = None
    inet6_range: Optional[str] = None


class Dns(BaseModel):
    servers: Optional[list[Server]] = None
    rules: Optional[list[Rule]] = None
    final: Optional[str] = None
    strategy: Optional[Strategy] = None
    disable_cache: Optional[bool] = None
    disable_expire: Optional[bool] = None
    independent_cache: Optional[bool] = None
    reverse_mapping: Optional[bool] = None
    client_subnet: Optional[str] = None
    fakeip: Optional[Fakeip] = None
