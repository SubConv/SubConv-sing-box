
from dataclasses import dataclass

@dataclass
class Log:
    disabled: bool = False
    level: str = "info"
    output: str = None
    timestamp: bool = True
