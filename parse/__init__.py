from type import outbound
from . import sing_box

import typing


def get_nodes(text: str) -> typing.Optional[list[outbound.Outbound]]:
    return sing_box.get_nodes(text)