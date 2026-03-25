from datetime import datetime
from pydantic import BaseModel, Field

class PostBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    content: str = Field(..., min_length=1, max_length=5000)
    

class PostCreate(PostBase):
    pass
    

class PostUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    content: str | None = Field(default=None, min_length=1, max_length=5000)

class Post(PostBase):
    id: int
    author_id: int
    created_at: datetime
    updated_at: datetime | None

class PostResponse(Post):
    pass

   

