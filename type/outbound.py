from .common import Network, Tls, Multiplex, Udp_over_tcp, v2transport

import typing
from dataclasses import dataclass

_T = typing.TypeVar('_T')

def outbound(type: str):
    def wrapper(cls: _T) -> _T:
        orig_init = cls.__init__
        def __init__(self, **kwargs):
            orig_init(self, type=type, **kwargs)
        cls.__init__ = __init__
        return cls
    return wrapper

@dataclass
class Outbound:
    type: str
    tag: str

@outbound("direct")
@dataclass
class Direct(Outbound):
    override_address: str = None
    override_port: int = None
    proxy_protocol: int = None

@outbound("block")
@dataclass
class Block(Outbound):
    pass

@outbound("socks")
@dataclass
class Socks(Outbound):
    server: str
    server_port: int
    version: int = None
    username: str = None
    password: str = None
    network: Network = None
    udp_over_tcp: Udp_over_tcp = None

@outbound("http")
@dataclass
class Http(Outbound):
    server: str
    server_port: int
    username: str = None
    password: str = None
    path: str = None
    headers: dict[str, str] = None
    tls: Tls = None

@outbound("shadowsocks")
@dataclass
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
@dataclass
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
@dataclass
class Trojan(Outbound):
    server: str
    server_port: int
    password: str
    network: Network = None
    tls: Tls = None
    multiplex: Multiplex = None
    transport: v2transport.V2transport = None

@outbound("wireguard")
@dataclass
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
@dataclass
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
@dataclass
class Shadowtls(Outbound):
    server: str
    server_port: int
    tls: Tls
    version: int = None
    password: str = None

@outbound("vless")
@dataclass
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
@dataclass
class Tuic:
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

@dataclass
class Hysteria2_obfs:
    type: str
    password: str

@outbound("hysteria2")
@dataclass
class Hysteria2:
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
@dataclass
class Tor:
    executable_path: str = None
    extra_args: list = None
    data_directory: str = None
    torrc: dict = None

@outbound("ssh")
@dataclass
class Ssh:
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
@dataclass
class Dns:
    pass

@outbound("selector")
@dataclass
class Selector:
    outbounds: list[str]
    default: str = None
    interrupt_exist_connections: bool = None

@outbound("urltest")
@dataclass
class Urltest:
    outbounds: list[str]
    url: str = None
    interval: str = None
    tolerance: int = None
    idle_timeout: str = None
    interrupt_exist_connections: bool = None
