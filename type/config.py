from .log import Log
from .dns import Dns
from .inbound import Inbound
from .outbound import Outbound
from .route import Route
from .experimental import Experimental

from pydantic import BaseModel, SerializeAsAny

class Config(BaseModel):
    log: Log = None
    dns: Dns = None
    inbounds: list[SerializeAsAny[Inbound]] = None
    outbounds: list[SerializeAsAny[Outbound]] = None
    route: Route = None
    experimental: Experimental = None
