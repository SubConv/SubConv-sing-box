from .rule import Rule
from .rule_set import Rule_set

from dataclasses import dataclass

@dataclass(kw_only=True)
class Route:
    rules: list[Rule]
    rule_set: list[Rule_set]
    final: str = None
    auto_detect_interface: bool = None
    override_android_vpn: bool = None
    default_interface: str = None
    default_mark: int = None

__all__ = [
    Route
]