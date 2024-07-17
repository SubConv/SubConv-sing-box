from .common import Network, Listen

import typing
from dataclasses import dataclass

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


@dataclass(kw_only=True)
class Inbound():
    type: str
    tag: str

@inbound("direct")
@dataclass(kw_only=True)
class Direct(Listen, Inbound):
    network: Network = None
    override_address: str = None
    override_port: int = None

@inbound("mixed")
@dataclass(kw_only=True)
class Mixed(Listen, Inbound):
    users: list[dict[str, str]] = None
    set_system_proxy: bool = None

@inbound("socks")
@dataclass(kw_only=True)
class Socks(Listen, Inbound):
    users: list[dict[str, str]] = None

@inbound("http")
@dataclass(kw_only=True)
class Http(Listen, Inbound):
    users: list[dict[str, str]] = None
    set_system_proxy: bool = None
