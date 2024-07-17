from . import v2transport

import enum
from pydantic import BaseModel

class Strategy(enum.Enum):
    prefer_ipv4 = "prefer_ipv4"
    prefer_ipv6 = "prefer_ipv6"
    ipv4_only = "ipv4_only"
    ipv6_only = "ipv6_only"

class IpVersion(enum.Enum): # 4 / 6
    v4 = 4
    v6 = 6

class Network(enum.Enum):
    tcp = "tcp"
    udp = "udp"

class Protocol(enum.Enum):
    http = "http"
    tls = "tls"
    quic = "quic"
    stun = "stun"
    dns = "dns"
    bittorrent = "bittorrent"
    dtls = "dtls"

class Listen(BaseModel):
    listen: str
    listen_port: int = None
    tcp_fast_open: bool = None
    tcp_multi_path: bool = None
    udp_fragment: bool = None
    udp_timeout: str = None
    detour: str = None
    sniff: bool = None
    sniff_override_destination: bool = None
    sniff_timeout: str = None
    domain_strategy: Strategy = None
    udp_disable_domain_unmapping: bool = None

class Utls(BaseModel):
    enabled: bool = True
    fingerprint: str = None

class Reality(BaseModel):
    public_key: str
    short_id: str
    enabled: bool = True
    max_time_difference: str = None

class Tls(BaseModel):
    enabled: bool = True
    disable_sni: bool = None
    server_name: str = None
    insecure: bool = None
    alpn: list[str] = None
    min_version: str = None
    max_version: str = None
    cipher_suites: list[str] = None
    utls: Utls = None
    reality: Reality = None

class Brutal(BaseModel):
    up_mbps: int
    down_mbps: int
    enabled: bool = True

class Multiplex(BaseModel):
    enabled: bool = True
    protocol: str = None
    max_connections: int = None
    min_streams: int = None
    max_streams: int = None
    padding: bool = None
    brutal: Brutal = None

class Udp_over_tcp(BaseModel):
    enabled: bool = True
    version: int = None


__all__ = [
    "Strategy",
    "IpVersion",
    "Network",
    "Protocol",
    "Listen",
    "Utls",
    "Reality",
    "Tls",
    "Brutal",
    "Multiplex",
    "Udp_over_tcp",
    "v2transport"
]