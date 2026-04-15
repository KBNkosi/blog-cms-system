from datetime import datetime
from pydantic import BaseModel, Field

class PostCreateDraft(BaseModel):
    title: str | None
    content: str | None 
    

class PostUpdateDraft(PostCreateDraft):
    pass
    

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    status: str
    user_id: int
    created_at: datetime
    updated_at: datetime | None
    published_at: datetime | None



   

