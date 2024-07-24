from .common import Network, Tls, Multiplex, Udp_over_tcp, v2transport

from typing import Optional, TypeVar
from pydantic import BaseModel, SerializeAsAny

_T = TypeVar('_T')

def outbound(type: str):
    def wrapper(cls: _T) -> _T:
        orig_init = cls.__init__
        def __init__(self, **kwargs):
            kwargs["type"] = type
            orig_init(self, **kwargs)
        cls.__init__ = __init__
        return cls
    return wrapper

class Outbound(BaseModel):
    type: str
    tag: str

@outbound("direct")
class Direct(Outbound):
    override_address: Optional[str] = None
    override_port: Optional[int] = None
    proxy_protocol: Optional[int] = None

@outbound("block")
class Block(Outbound):
    pass

@outbound("socks")
class Socks(Outbound):
    server: str
    server_port: int
    version: Optional[int] = None
    username: Optional[str] = None
    password: Optional[str] = None
    network: Optional[Network] = None
    udp_over_tcp: Optional[Udp_over_tcp] = None

@outbound("http")
class Http(Outbound):
    server: str
    server_port: int
    username: Optional[str] = None
    password: Optional[str] = None
    path: Optional[str] = None
    headers: Optional[dict[str, str]] = None
    tls: Optional[Tls] = None

@outbound("shadowsocks")
class Shadowsocks(Outbound):
    server: str
    server_port: int
    method: str
    password: str
    plugin: Optional[str] = None
    plugin_opts: Optional[str] = None
    network: Optional[Network] = None
    udp_over_tcp: Optional[Udp_over_tcp] = None
    multiplex: Optional[Multiplex] = None

@outbound("vmess")
class Vmess(Outbound):
    server: str
    server_port: int
    uuid: str
    security: Optional[str] = None
    alter_id: Optional[int] = None
    global_padding: Optional[bool] = None
    authenticated_length: Optional[bool] = None
    network: Optional[Network] = None
    tls: Optional[Tls] = None
    packet_encoding: Optional[str] = None
    multiplex: Optional[Multiplex] = None
    transport: Optional[SerializeAsAny[v2transport.V2transport]] = None

@outbound("trojan")
class Trojan(Outbound):
    server: str
    server_port: int
    password: str
    network: Optional[Network] = None
    tls: Optional[Tls] = None
    multiplex: Optional[Multiplex] = None
    transport: Optional[SerializeAsAny[v2transport.V2transport]] = None

@outbound("wireguard")
class Wireguard(Outbound):
    server: str
    server_port: int
    local_address: list[str]
    private_key: str
    peer_public_key: str
    system_interface: Optional[bool] = None
    gso: Optional[bool] = None
    interface_name: Optional[str] = None
    pre_shared_key: Optional[str] = None
    reserved: Optional[list] = None
    workers: Optional[int] = None
    mtu: Optional[int] = None
    network: Optional[Network] = None

@outbound("hysteria")
class Hysteria(Outbound):
    server: str
    server_port: int
    up_mbps: int
    down_mbps: int
    tls: Tls
    obfs: Optional[str] = None
    auth: Optional[str] = None
    auth_str: Optional[str] = None
    recv_window_conn: Optional[int] = None
    recv_window: Optional[int] = None
    disable_mtu_discovery: Optional[bool] = None
    network: Optional[Network] = None

@outbound("shadowtls")
class Shadowtls(Outbound):
    server: str
    server_port: int
    tls: Tls
    version: Optional[int] = None
    password: Optional[str] = None

@outbound("vless")
class Vless(Outbound):
    server: str
    server_port: int
    uuid: str
    flow: Optional[str] = None
    network: Optional[Network] = None
    tls: Optional[Tls] = None
    packet_encoding: Optional[str] = None
    multiplex: Optional[Multiplex] = None
    transport: Optional[SerializeAsAny[v2transport.V2transport]] = None

@outbound("tuic")
class Tuic(Outbound):
    server: str
    server_port: int
    uuid: str
    tls: Tls
    password: Optional[str] = None
    congestion_control: Optional[str] = None
    udp_relay_mode: Optional[str] = None
    udp_over_stream: Optional[bool] = None
    zero_rtt_handshake: Optional[bool] = None
    heartbeat: Optional[str] = None
    network: Optional[Network] = None

class Hysteria2_obfs(BaseModel):
    type: str
    password: str

@outbound("hysteria2")
class Hysteria2(Outbound):
    server: str
    server_port: int
    tls: Tls
    up_mbps: Optional[int] = None
    down_mbps: Optional[int] = None
    obfs: Optional[Hysteria2_obfs] = None
    password: Optional[str] = None
    network: Optional[Network] = None
    brutal_debug: Optional[bool] = None

@outbound("tor")
class Tor(Outbound):
    executable_path: Optional[str] = None
    extra_args: Optional[list] = None
    data_directory: Optional[str] = None
    torrc: Optional[dict] = None

@outbound("ssh")
class Ssh(Outbound):
    server: str
    server_port: Optional[int] = None
    user: Optional[str] = None
    password: Optional[str] = None
    private_key: Optional[str] = None
    private_key_path: Optional[str] = None
    private_key_passphrase: Optional[str] = None
    host_key: Optional[list] = None
    host_key_algorithms: Optional[list] = None
    client_version: Optional[str] = None

@outbound("dns")
class Dns(Outbound):
    pass

@outbound("selector")
class Selector(Outbound):
    outbounds: list[str]
    default: Optional[str] = None
    interrupt_exist_connections: Optional[bool] = None

@outbound("urltest")
class Urltest(Outbound):
    outbounds: list[str]
    url: Optional[str] = None
    interval: Optional[str] = None
    tolerance: Optional[int] = None
    idle_timeout: Optional[str] = None
    interrupt_exist_connections: Optional[bool] = None
