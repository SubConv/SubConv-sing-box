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
            orig_init(self, type=type, **kwargs)
        cls.__init__ = __init__
        return cls
    return wrapper


@dataclass
class Inbound():
    type: str
    tag: str

@inbound("direct")
@dataclass
class Direct(Listen, Inbound):
    network: Network = None
    override_address: str = None
    override_port: int = None

@inbound("mixed")
@dataclass
class Mixed(Listen, Inbound):
    users: list[dict[str, str]] = None
    set_system_proxy: bool = None

@inbound("socks")
@dataclass
class Socks(Listen, Inbound):
    users: list[dict[str, str]] = None

@inbound("http")
@dataclass
class Http(Listen, Inbound):
    users: list[dict[str, str]] = None
    set_system_proxy: bool = None
