from app.schemas.post import PostCreateDraft, PostUpdateDraft, PostResponse
from app.services.post_service import publish_post, create_post_draft
from fastapi import APIRouter
from typing import List

router = APIRouter()            
            
# Create post draft
@router.post("/posts", tags=["Posts"],  response_model=PostResponse, status_code=201,)
def create_post_draft_route(post_data: PostCreateDraft):
    # For testing: hardcoded user ID
    current_user_id = 5 # Test user
    post_data_dict = post_data.model_dump()
    new_post = create_post_draft(current_user_id, post_data_dict)

    return new_post

 
# Publish post route
@router.patch("/posts/{post_id}/publish", tags=["Posts"], response_model=PostResponse)
async def publish_post_route(post_id:int):
    # For testing: hardcoded user ID
    current_user_id = 1 # Test user 

    post = publish_post(current_user_id, post_id)
    return post



