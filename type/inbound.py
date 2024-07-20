from .common import Network, Listen

import typing
from pydantic import BaseModel

_T = typing.TypeVar('_T')

def inbound(type: str):
    """
    inbound decorator

    init listen fields for inbound
    """
    def wrapper(cls: _T) -> _T:
        orig_init = cls.__init__
        def __init__(self, **kwargs):
            kwargs["type"] = type
            orig_init(self, **kwargs)
        cls.__init__ = __init__
        return cls
    return wrapper


class Inbound(BaseModel):
    type: str
    tag: str

@inbound("direct")
class Direct(Listen, Inbound):
    network: Network = None
    override_address: str = None
    override_port: int = None

@inbound("mixed")
class Mixed(Listen, Inbound):
    users: list[dict[str, str]] = None
    set_system_proxy: bool = None

@inbound("socks")
class Socks(Listen, Inbound):
    users: list[dict[str, str]] = None

@inbound("http")
class Http(Listen, Inbound):
    users: list[dict[str, str]] = None
    set_system_proxy: bool = None

@inbound("tun")
class Tun(Listen, Inbound):
    listen: str = None # `listen` is not required for tun inbound
    interface_name: str = None

    # address: list[str]
    inet4_address: list[str]
    inet6_address: list[str]

    mtu: int = None
    gso: bool = None
    auto_route: bool = None
    # iproute2_table_index: int = None
    # iproute2_rule_index: int = None
    # auto_redirect: bool = None
    # auto_redirect_input_mark: str = None
    # auto_redirect_output_mark: str = None
    strict_route: bool = None

    # route_address: list[str] = None
    inet4_route_address: list[str] = None
    inet6_route_address: list[str] = None

    # route_exclude_address: list[str] = None
    inet4_route_exclude_address: list[str] = None
    inet6_route_exclude_address: list[str] = None

    # route_address_set: list[str] = None
    # route_exclude_address_set: list[str] = None
    endpoint_independent_nat: bool = None
    udp_timeout: str = None
    stack: str = None
    include_interface: list[str] = None
    exclude_interface: list[str] = None
    include_uid: list[int] = None
    include_uid_range: list[str] = None
    exclude_uid: list[int] = None
    exclude_uid_range: list[str] = None
    include_android_user: list[int] = None
    include_package: list[str] = None
    exclude_package: list[str] = None
    platform: dict = None
