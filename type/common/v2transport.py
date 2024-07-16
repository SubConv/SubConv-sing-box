
import typing
from dataclasses import dataclass

_T = typing.TypeVar('_T')

def v2transport(type: str):
    def wrapper(cls: _T) -> _T:
        orig_init = cls.__init__
        def __init__(self, **kwargs):
            orig_init(self, type=type, **kwargs)
        cls.__init__ = __init__
        return cls
    return wrapper

@dataclass
class V2transport:
    type: str

@v2transport("tcp")
@dataclass
class Http(V2transport):
    type = "http"
    host: list[str] = None
    path: str = None
    method: str = None
    headers: dict[str, str] = None
    idle_timeout: str = None
    ping_timeout: str = None

@v2transport("websocket")
@dataclass
class Websocket(V2transport):
    type = "websocket"
    path: str = None
    headers: dict[str, str] = None
    max_early_data: int = None
    early_data_header_name: str = None

@v2transport("quic")
@dataclass
class Quic(V2transport):
    type = "quic"
    pass

@v2transport("grpc")
@dataclass
class Grpc(V2transport):
    type = "grpc"
    service_name: str = None
    idle_timeout: str = None
    ping_timeout: str = None
    permit_without_stream: bool = None

@v2transport("httpupgrade")
@dataclass
class Httpupgrade(V2transport):
    type = "httpupgrade"
    host: str = None
    path: str = None
    headers: dict[str, str] = None
