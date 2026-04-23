from datetime import datetime
from pydantic import BaseModel

class PostCreateDraft(BaseModel):
    title: str | None
    content: str | None 
    

class PostUpdateDraft(PostCreateDraft):
    pass
    

class PostResponse(BaseModel):
    id: int
    title: str | None
    content: str | None
    slug: str | None
    status: str
    user_id: int
    created_at: datetime
    updated_at: datetime | None
    published_at: datetime | None



   

