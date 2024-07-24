from . import v2transport

from typing import Optional
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
    listen_port: Optional[int] = None
    tcp_fast_open: Optional[bool] = None
    tcp_multi_path: Optional[bool] = None
    udp_fragment: Optional[bool] = None
    udp_timeout: Optional[str] = None
    detour: Optional[str] = None
    sniff: Optional[bool] = None
    sniff_override_destination: Optional[bool] = None
    sniff_timeout: Optional[str] = None
    domain_strategy: Optional[Strategy] = None
    udp_disable_domain_unmapping: Optional[bool] = None

class Utls(BaseModel):
    enabled: bool = True
    fingerprint: Optional[str] = None

class Reality(BaseModel):
    public_key: str
    short_id: str
    enabled: bool = True
    max_time_difference: Optional[str] = None

class Tls(BaseModel):
    enabled: bool = True
    disable_sni: Optional[bool] = None
    server_name: Optional[str] = None
    insecure: Optional[bool] = None
    alpn: Optional[list[str]] = None
    min_version: Optional[str] = None
    max_version: Optional[str] = None
    cipher_suites: Optional[list[str]] = None
    utls: Optional[Utls] = None
    reality: Optional[Reality] = None

class Brutal(BaseModel):
    up_mbps: int
    down_mbps: int
    enabled: bool = True

class Multiplex(BaseModel):
    enabled: bool = True
    protocol: Optional[str] = None
    max_connections: Optional[int] = None
    min_streams: Optional[int] = None
    max_streams: Optional[int] = None
    padding: Optional[bool] = None
    brutal: Optional[Brutal] = None

class Udp_over_tcp(BaseModel):
    enabled: bool = True
    version: Optional[int] = None


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