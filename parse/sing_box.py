"""

"""
import logging
logger = logging.getLogger(__name__)

from type import outbound
from type.common import v2transport

import json
import typing


def get_nodes(text: str) -> typing.Optional[list[outbound.Outbound]]:
    result = []

    try:
        text_json = json.loads(text)
        outbounds = text_json["outbounds"]
        for item in outbounds:
            if item["type"] not in ("direct", "block", "dns", "selector", "urltest"):
                # use correct outbound class
                node = eval(f"outbound.{item['type'].capitalize()}")(**item)
                # fix transport field
                if "transport" in item:
                    node.transport = eval(f"v2transport.{item['transport']['type'].capitalize()}")(**item["transport"])
                result.append(node)
    except Exception as e:
        logger.debug(f"get_outbounds: {e} with text: {text}")
        return None

    return result



