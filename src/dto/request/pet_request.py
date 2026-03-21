from typing import List, Optional

from pydantic import BaseModel, Field


class PetDto(BaseModel):
    id: Optional[int] = None
    category: Optional[CategoryDto] = None
    name: str
    photo_urls: List[str] = Field(alias="photoUrls")
    tags: Optional[List[TagsDto]] = None
    status: Optional[str] = None

class CategoryDto(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None

class TagsDto(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
