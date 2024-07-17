from .rule import Rule
from .rule_set import Rule_set

from pydantic import BaseModel, SerializeAsAny

class Route(BaseModel):
    rules: list[Rule]
    rule_set: list[SerializeAsAny[Rule_set]]
    final: str = None
    auto_detect_interface: bool = None
    override_android_vpn: bool = None
    default_interface: str = None
    default_mark: int = None

__all__ = [
    Route
]