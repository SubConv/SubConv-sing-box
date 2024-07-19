from .common import Strategy, IpVersion, Network, Protocol
import typing

from pydantic import BaseModel

class Server(BaseModel):
    address: str
    tag: str = None
    address_resolver: str = None
    address_strategy: Strategy = None
    strategy: Strategy = None
    detour: str = None
    client_subnet: str = None

class Rule(BaseModel):
    inbound: list[str] = None
    server: str
    ip_version: IpVersion = None
    query_type: list[typing.Union[int, str]] = None
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
    disable_cache: bool = None
    rewrite_ttl: int = None
    client_subnet: str = None
    geoip: list[str] = None
    ip_cidr: list[str] = None
    ip_is_private: bool = None
    rule_set_ip_cidr_accept_empty: bool = None


class Fakeip(BaseModel):
    enabled: bool = True
    inet4_range: str = None
    inet6_range: str = None


class Dns(BaseModel):
    servers: list[Server] = None
    rules: list[Rule] = None
    final: str = None
    strategy: Strategy = None
    disable_cache: bool = None
    disable_expire: bool = None
    independent_cache: bool = None
    reverse_mapping: bool = None
    client_subnet: str = None
    fakeip: Fakeip = None
