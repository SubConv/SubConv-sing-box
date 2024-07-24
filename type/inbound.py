from .common import Network, Listen

from typing import Optional, TypeVar
from pydantic import BaseModel

_T = TypeVar('_T')

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
    network: Optional[Network] = None
    override_address: Optional[str] = None
    override_port: Optional[int] = None

@inbound("mixed")
class Mixed(Listen, Inbound):
    users: Optional[list[dict[str, str]]] = None
    set_system_proxy: Optional[bool] = None

@inbound("socks")
class Socks(Listen, Inbound):
    users: Optional[list[dict[str, str]]] = None

@inbound("http")
class Http(Listen, Inbound):
    users: Optional[list[dict[str, str]]] = None
    set_system_proxy: Optional[bool] = None

@inbound("tun")
class Tun(Listen, Inbound):
    listen: Optional[str] = None # `listen` is not required for tun inbound
    interface_name: Optional[str] = None

    # address: list[str]
    inet4_address: list[str]
    inet6_address: list[str]

    mtu: Optional[int] = None
    gso: Optional[bool] = None
    auto_route: Optional[bool] = None
    # iproute2_table_index: Optional[int] = None
    # iproute2_rule_index: Optional[int] = None
    # auto_redirect: Optional[bool] = None
    # auto_redirect_input_mark: Optional[str] = None
    # auto_redirect_output_mark: Optional[str] = None
    strict_route: Optional[bool] = None

    # route_address: Optional[list[str]] = None
    inet4_route_address: Optional[list[str]] = None
    inet6_route_address: Optional[list[str]] = None

    # route_exclude_address: Optional[list[str]] = None
    inet4_route_exclude_address: Optional[list[str]] = None
    inet6_route_exclude_address: Optional[list[str]] = None

    # route_address_set: Optional[list[str]] = None
    # route_exclude_address_set: Optional[list[str]] = None
    endpoint_independent_nat: Optional[bool] = None
    udp_timeout: Optional[str] = None
    stack: Optional[str] = None
    include_interface: Optional[list[str]] = None
    exclude_interface: Optional[list[str]] = None
    include_uid: Optional[list[int]] = None
    include_uid_range: Optional[list[str]] = None
    exclude_uid: Optional[list[int]] = None
    exclude_uid_range: Optional[list[str]] = None
    include_android_user: Optional[list[int]] = None
    include_package: Optional[list[str]] = None
    exclude_package: Optional[list[str]] = None
    platform: Optional[dict] = None
