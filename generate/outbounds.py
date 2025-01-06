import logging
logger = logging.getLogger(__name__)

from config.config import config_instance
from type.outbound import Outbound, Selector, Urltest, Direct, Block, Dns
from parse import get_nodes

from typing import Optional
import re

def get_outbounds(nodes: list[Outbound]) -> Optional[list[Outbound]]:
    result: list[Outbound] = []

    # Get nodes from the data
    if nodes is None:
        return None

    node_tags = [node.tag for node in nodes]

    for outbound in config_instance.outbounds:
        if outbound.type in ("selector", "urltest"):
            outbounds = outbound.outbounds.copy() if outbound.outbounds is not None else []
            if outbound.regex is not None:
                for node_tag in node_tags:
                    if re.search(outbound.regex, node_tag):
                        outbounds.append(node_tag)
            if len(outbounds) > 0:
                result.append(eval(outbound.type.capitalize())(
                    tag=outbound.tag,
                    outbounds=outbounds
                ))
        elif outbound.type in ("direct", "block", "dns"):
            result.append(eval(outbound.type.capitalize())(
                tag=outbound.tag
            ))
        else:
            logger.warning(f"Unknown outbound type for config: {outbound.type}, skipping")
            continue

    result.extend(nodes)

    # add direct, block, dns outbounds
    result.extend([
        Direct(tag="direct"),
        Block(tag="block"),
        Dns(tag="dns-out")
    ])
    result.append(Selector(tag="Global", outbounds=[node.tag for node in result]))

    # remove non-existent outbounds
    outbound_tags = [outbound.tag for outbound in result]
    for outbound in result:
        if isinstance(outbound, Selector) or isinstance(outbound, Urltest):
            outbound.outbounds = [outbound_tag for outbound_tag in outbound.outbounds if outbound_tag in outbound_tags]

    return result
