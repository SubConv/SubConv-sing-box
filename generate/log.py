from config.config import config_instance
from type.log import Log

def get_log() -> Log:
    return config_instance.log
