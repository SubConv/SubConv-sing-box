import logging
logger = logging.getLogger(__name__)

from .default_config import default_config, default_zju_config
from .type import User_config
from type.inbound import Direct, Mixed, Socks, Http, Tun

import json
import os
from typing import Optional
import enum

class Default_config_type(enum.Enum):
    Default = "default"
    ZJU = "zju"

def generate_default_config(type: Default_config_type = Default_config_type.Default):
    try:
        type = Default_config_type(type)
    except ValueError:
        logger.error(f"Invalid default config type: {type}")
        return
    with open("config.json", "w", encoding="utf-8") as f:
        if type == Default_config_type.Default:
            f.write(default_config.model_dump_json(exclude_none=True, indent=2))
        elif type == Default_config_type.ZJU:
            f.write(default_zju_config.model_dump_json(exclude_none=True, indent=2))

def load_config() -> Optional[User_config]:
    if not os.path.exists("config.json"):
        logger.error("config.json not found, please run --help to see how to generate a default config")
        return None
    
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            config_json = json.load(f)
            result = User_config.model_validate(config_json)
            # fix inbounds field
            result.inbounds = [eval(inbound["type"].capitalize())(**inbound) for inbound in config_json["inbounds"]]

            logger.info("config.json loaded")
            return result
    except Exception as e:
        logger.error(f"Failed to load config.json: {e}")
        return None
