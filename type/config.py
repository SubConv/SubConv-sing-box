from .log import Log
from .dns import Dns
from .inbound import Inbound
from .outbound import Outbound
from .route import Route
from .experimental import Experimental

from pydantic import BaseModel, SerializeAsAny
from typing import Optional

class Config(BaseModel):
    log: Optional[Log] = None
    dns: Optional[Dns] = None
    inbounds: Optional[list[SerializeAsAny[Inbound]]] = None
    outbounds: Optional[list[SerializeAsAny[Outbound]]] = None
    route: Optional[Route] = None
    experimental: Optional[Experimental] = None
