from pydantic import BaseModel
from typing import Optional, List

class SpinResult(BaseModel):
    reels: List[str]
    win: bool
    payout: int
    message: Optional[str] = None