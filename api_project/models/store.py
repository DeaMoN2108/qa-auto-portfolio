from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class OrderModel(BaseModel):
    id: int
    petId: int
    quantity: int
    shipDate: Optional[datetime] = None
    status: str
    complete: bool