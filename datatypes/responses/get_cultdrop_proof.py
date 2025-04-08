from typing import List, Optional

from pydantic import BaseModel


class CultDropProofResponse(BaseModel):
    address: Optional[str]
    amount: Optional[int]
    proofs: Optional[List[str]]
    message: Optional[str]


