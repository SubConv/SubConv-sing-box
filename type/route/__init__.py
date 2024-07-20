from .rule import Rule
from .rule_set import Rule_set, Inline, Local, Remote, HeadlessRule

from pydantic import BaseModel, SerializeAsAny

class Route(BaseModel):
    rules: list[Rule]
    rule_set: list[SerializeAsAny[Rule_set]]
    final: str = None
    auto_detect_interface: bool = True
    override_android_vpn: bool = None
    default_interface: str = None
    default_mark: int = None

__all__ = [
    "Rule",
    "Rule_set",
    "Route",
    "Inline",
    "Local",
    "Remote",
    "HeadlessRule"
]