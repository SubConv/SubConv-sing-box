from config.config import config_instance
from type.inbound import Inbound

def get_inbounds(tun: bool) -> list[Inbound]:
    inbound = config_instance.inbounds
    if not tun:
        inbound = [i for i in inbound if i.type != "tun"]
    return inbound
