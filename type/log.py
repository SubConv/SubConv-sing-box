from pydantic import BaseModel
from typing import Optional

class Log(BaseModel):
    disabled: bool = False
    level: str = "info"
    output: Optional[str] = None
    timestamp: Optional[bool] = None
