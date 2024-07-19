from type.config import Config
from type.outbound import Outbound
from type.experimental import Experimental
from .inbounds import get_inbounds
from .outbounds import get_outbounds
from .route import get_route
from .experimental import get_experimental
from .log import get_log
from .dns import get_dns

import typing

def get_config(nodes: list[Outbound], base_url: str) -> typing.Optional[Config]:
    return Config(
        experimental=get_experimental(),
        log=get_log(),
        dns=get_dns(),
        inbounds=get_inbounds(),
        outbounds=get_outbounds(nodes),
        route=get_route(base_url)
    )