import typing
from pydantic import BaseModel

_T = typing.TypeVar('_T')

def v2transport(type: str):
    def wrapper(cls: _T) -> _T:
        orig_init = cls.__init__
        def __init__(self, **kwargs):
            kwargs["type"] = type
            orig_init(self, **kwargs)
        cls.__init__ = __init__
        return cls
    return wrapper

class V2transport(BaseModel):
    type: str

@v2transport("tcp")
class Http(V2transport):
    host: list[str] = None
    path: str = None
    method: str = None
    headers: dict[str, str] = None
    idle_timeout: str = None
    ping_timeout: str = None

@v2transport("websocket")
class Websocket(V2transport):
    path: str = None
    headers: dict[str, str] = None
    max_early_data: int = None
    early_data_header_name: str = None

@v2transport("quic")
class Quic(V2transport):
    pass

@v2transport("grpc")
class Grpc(V2transport):
    service_name: str = None
    idle_timeout: str = None
    ping_timeout: str = None
    permit_without_stream: bool = None

@v2transport("httpupgrade")
class Httpupgrade(V2transport):
    host: str = None
    path: str = None
    headers: dict[str, str] = None
