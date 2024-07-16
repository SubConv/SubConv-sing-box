
from dataclasses import dataclass

@dataclass
class Cache_file:
    enabled: bool = True
    path: str = None
    cache_id: str = None
    store_fakeip: bool = None
    store_rdrc: bool = None
    rdrc_timeout: str = None

@dataclass
class Clash_api:
    external_controller: str = None
    external_ui: str = None
    external_ui_download_url: str = None
    external_ui_download_detour: str = None
    secret: str = None
    default_mode: str = None

@dataclass
class V2ray_api_stat:
    enabled: bool = None
    inbounds: list[str] = None
    outbounds: list[str] = None
    users: list[str] = None

@dataclass
class V2ray_api:
    listen: str = None
    stats: V2ray_api_stat = None

@dataclass
class Experimental:
    cache_file: Cache_file = None
    clash_api: Clash_api = None
    v2ray_api: V2ray_api = None
