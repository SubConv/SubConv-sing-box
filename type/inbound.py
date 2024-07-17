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
