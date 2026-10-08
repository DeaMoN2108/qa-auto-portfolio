from pydantic import BaseModel
from typing import Optional, List

class Category(BaseModel):
    id: int
    name: str
class Tag(BaseModel):
    id: int
    name: str
class PetModel(BaseModel):
    id: int
    category: Optional[Category] = None
    name: str
    photoUrls: List[str]
    tags: Optional[List[Tag]] = None
    status: str