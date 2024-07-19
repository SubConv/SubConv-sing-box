from config.config import config_instance
from type.experimental import Experimental

def get_experimental() -> Experimental:
    return config_instance.experimental