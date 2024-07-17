from .common import Network, Tls, Multiplex, Udp_over_tcp, v2transport

import typing
import enum
from dataclasses import dataclass

_T = typing.TypeVar('_T')

def outbound(type: str):
    def wrapper(cls: _T) -> _T:
        orig_init = cls.__init__
        def __init__(self, **kwargs):
            kwargs["type"] = type
            orig_init(self, **kwargs)
        cls.__init__ = __init__
        return cls
    return wrapper

@dataclass(kw_only=True)
class Outbound:
    type: str
    tag: str

@outbound("direct")
@dataclass(kw_only=True)
class Direct(Outbound):
    override_address: str = None
    override_port: int = None
    proxy_protocol: int = None

@outbound("block")
@dataclass(kw_only=True)
class Block(Outbound):
    pass

@outbound("socks")
@dataclass(kw_only=True)
class Socks(Outbound):
    server: str
    server_port: int
    version: int = None
    username: str = None
    password: str = None
    network: Network = None
    udp_over_tcp: Udp_over_tcp = None

@outbound("http")
@dataclass(kw_only=True)
class Http(Outbound):
    server: str
    server_port: int
    username: str = None
    password: str = None
    path: str = None
    headers: dict[str, str] = None
    tls: Tls = None

@outbound("shadowsocks")
@dataclass(kw_only=True)
class Shadowsocks(Outbound):
    server: str
    server_port: int
    method: str
    method: str
    plugin: str = None
    plugin_opts: str = None
    network: Network = None
    udp_over_tcp: Udp_over_tcp = None
    multiplex: Multiplex = None

@outbound("vmess")
@dataclass(kw_only=True)
class Vmess(Outbound):
    server: str
    server_port: int
    uuid: str
    security: str = None
    alter_id: int = None
    global_padding: bool = None
    authenticated_length: bool = None
    network: Network = None
    tls: Tls = None
    packet_encoding: str = None
    multiplex: Multiplex = None
    transport: v2transport.V2transport = None

@outbound("trojan")
@dataclass(kw_only=True)
class Trojan(Outbound):
    server: str
    server_port: int
    password: str
    network: Network = None
    tls: Tls = None
    multiplex: Multiplex = None
    transport: v2transport.V2transport = None

@outbound("wireguard")
@dataclass(kw_only=True)
class Wireguard(Outbound):
    server: str
    server_port: int
    local_address: list[str]
    private_key: str
    peer_public_key: str
    system_interface: bool = None
    gso: bool = None
    interface_name: str = None
    pre_shared_key: str = None
    reserved: list = None
    workers: int = None
    mtu: int = None
    network: Network = None

@outbound("hysteria")
@dataclass(kw_only=True)
class Hysteria(Outbound):
    server: str
    server_port: int
    up_mbps: int
    down_mbps: int
    tls: Tls
    obfs: str = None
    auth: str = None
    auth_str: str = None
    recv_window_conn: int = None
    recv_window: int = None
    disable_mtu_discovery: bool = None
    network: Network = None

@outbound("shadowtls")
@dataclass(kw_only=True)
class Shadowtls(Outbound):
    server: str
    server_port: int
    tls: Tls
    version: int = None
    password: str = None

@outbound("vless")
@dataclass(kw_only=True)
class Vless(Outbound):
    server: str
    server_port: int
    uuid: str
    flow: str = None
    network: Network = None
    tls: Tls = None
    packet_encoding: str = None
    multiplex: Multiplex = None
    transport: v2transport.V2transport = None

@outbound("tuic")
@dataclass(kw_only=True)
class Tuic(Outbound):
    server: str
    server_port: int
    uuid: str
    tls: Tls
    password: str = None
    congestion_control: str = None
    udp_relay_mode: str = None
    udp_over_stream: bool = None
    zero_rtt_handshake: bool = None
    heartbeat: str = None
    network: Network = None

@dataclass(kw_only=True)
class Hysteria2_obfs:
    type: str
    password: str

@outbound("hysteria2")
@dataclass(kw_only=True)
class Hysteria2(Outbound):
    server: str
    server_port: int
    tls: Tls
    up_mbps: int = None
    down_mbps: int = None
    obfs: Hysteria2_obfs = None
    password: str = None
    network: Network = None
    brutal_debug: bool = None

@outbound("tor")
@dataclass(kw_only=True)
class Tor(Outbound):
    executable_path: str = None
    extra_args: list = None
    data_directory: str = None
    torrc: dict = None

@outbound("ssh")
@dataclass(kw_only=True)
class Ssh(Outbound):
    server: str
    server_port: int = None
    user: str = None
    password: str = None
    private_key: str = None
    private_key_path: str = None
    private_key_passphrase: str = None
    host_key: list = None
    host_key_algorithms: list = None
    client_version: str = None

@outbound("dns")
@dataclass(kw_only=True)
class Dns(Outbound):
    pass

@outbound("selector")
@dataclass(kw_only=True)
class Selector(Outbound):
    outbounds: list[str]
    default: str = None
    interrupt_exist_connections: bool = None

@outbound("urltest")
@dataclass(kw_only=True)
class Urltest(Outbound):
    outbounds: list[str]
    url: str = None
    interval: str = None
    tolerance: int = None
    idle_timeout: str = None
    interrupt_exist_connections: bool = None
