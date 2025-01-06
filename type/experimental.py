from pydantic import BaseModel
from typing import Optional

class Cache_file(BaseModel):
    enabled: bool = True
    path: Optional[str] = None
    cache_id: Optional[str] = None
    store_fakeip: Optional[bool] = None
    store_rdrc: Optional[bool] = None
    rdrc_timeout: Optional[str] = None

class Clash_api(BaseModel):
    external_controller: Optional[str] = None
    external_ui: Optional[str] = None
    external_ui_download_url: Optional[str] = None
    external_ui_download_detour: Optional[str] = None
    secret: Optional[str] = None
    default_mode: Optional[str] = None
    access_control_allow_origin: Optional[list[str]] = None
    access_control_allow_private_network: Optional[bool] = None

class V2ray_api_stat(BaseModel):
    enabled: Optional[bool] = None
    inbounds: Optional[list[str]] = None
    outbounds: Optional[list[str]] = None
    users: Optional[list[str]] = None

class V2ray_api(BaseModel):
    listen: Optional[str] = None
    stats: Optional[V2ray_api_stat] = None

class Experimental(BaseModel):
    cache_file: Optional[Cache_file] = None
    clash_api: Optional[Clash_api] = None
    v2ray_api: Optional[V2ray_api] = None
