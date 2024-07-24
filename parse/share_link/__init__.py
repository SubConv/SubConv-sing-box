from .converter import ConvertsV2Ray
from type.outbound import Outbound

from typing import Optional


def get_nodes(text: str) -> Optional[list[Outbound]]:
    return ConvertsV2Ray(text)