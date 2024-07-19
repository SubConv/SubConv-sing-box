from type.log import Log
from type.dns import Dns
from type.inbound import Inbound
from type.experimental import Experimental

from pydantic import BaseModel, SerializeAsAny

class User_config_outbound(BaseModel):
    type: str
    tag: str
    regex: str = None
    outbounds: list[str] = None

class User_config_route(BaseModel):
    remote_rule_set: list[list[str]]
    final: str


class User_config(BaseModel):
    log: Log
    dns: Dns
    experimental: Experimental
    inbounds: list[SerializeAsAny[Inbound]]
    outbounds: list[User_config_outbound]
    route: User_config_route
