from config.config import config_instance
from type.inbound import Inbound

def get_inbounds() -> list[Inbound]:
    return config_instance.inbounds