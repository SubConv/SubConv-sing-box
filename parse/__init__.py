from type import outbound
from . import sing_box
from . import share_link

from typing import Optional


def get_nodes(text: str) -> Optional[list[outbound.Outbound]]:
    return sing_box.get_nodes(text) or share_link.get_nodes(text)
