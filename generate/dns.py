from config.config import config_instance
from type.dns import Dns

def get_dns() -> Dns:
    return config_instance.dns
