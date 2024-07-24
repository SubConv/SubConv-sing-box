from .rule import Rule
from .rule_set import Rule_set, Inline, Local, Remote, HeadlessRule

from pydantic import BaseModel, SerializeAsAny
from typing import Optional

class Route(BaseModel):
    rules: list[Rule]
    rule_set: list[SerializeAsAny[Rule_set]]
    final: Optional[str] = None
    auto_detect_interface: bool = True
    override_android_vpn: Optional[bool] = None
    default_interface: Optional[str] = None
    default_mark: Optional[int] = None

__all__ = [
    "Rule",
    "Rule_set",
    "Route",
    "Inline",
    "Local",
    "Remote",
    "HeadlessRule"
]