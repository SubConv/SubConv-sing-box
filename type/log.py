
from dataclasses import dataclass

@dataclass(kw_only=True)
class Log:
    disabled: bool = False
    level: str = "info"
    output: str = None
    timestamp: bool = True
