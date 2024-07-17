from .log import Log
from .dns import Dns
from .inbound import Inbound
from .outbound import Outbound
from .route import Route
from .experimental import Experimental

from dataclasses import dataclass

@dataclass(kw_only=True)
class Config:
    log: Log = None
    dns: Dns = None
    inbounds: list[Inbound] = None
    outbounds: list[Outbound] = None
    route: Route = None
    experimental: Experimental = None
