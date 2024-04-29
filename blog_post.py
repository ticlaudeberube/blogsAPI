from typing import List, Optional
from pydantic import BaseModel

class BlogPost(BaseModel):
    id: Optional[str]
    title: str
    i18n: str
    live: bool
    url: str
    topics: List[str]
    year: int