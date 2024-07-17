from pydantic import BaseModel

class Log(BaseModel):
    disabled: bool = False
    level: str = "info"
    output: str = None
    timestamp: bool = True
