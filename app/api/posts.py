from fastapi import APIRouter
from app.schemas.post import PostCreateDraft, PostUpdateDraft, PostResponse
from app.services.post_service import (
  publish_post,
  create_post_draft,
  update_post, 
  get_post_for_owner,
  get_public_post
)
 
router = APIRouter()

# Temporary hardcoded test user until authentication is added
TEST_USER_ID = 1

            
# Create post draft
@router.post("/posts/drafts", tags=["Posts"],  response_model=PostResponse, status_code=201,)
def create_post_draft_route(post_data: PostCreateDraft):
    post_data_dict = post_data.model_dump()
    new_post = create_post_draft(TEST_USER_ID, post_data_dict)
    return new_post

# Get post for owner
@router.get("/posts/{post_id}", tags=["Posts"], response_model=PostResponse, status_code=200)
def get_post_for_owner_route(post_id:int):
    post = get_post_for_owner(post_id, TEST_USER_ID)
    return post

# search public post
@router.get("/posts/public/{slug}", tags=["Posts"], response_model=PostResponse, status_code=200)
def search_public_post_route(slug: str): 
    post = get_public_post(slug)
    return post

    

# Update post
@router.patch("/posts/{post_id}", tags=["Posts"], response_model=PostResponse, status_code=200)
def update_post_route(post_id: int, post_data:PostUpdateDraft):
    post_data_dict = post_data.model_dump(exclude_unset=True)
    updated_post = update_post(post_id, TEST_USER_ID, post_data_dict)
    return updated_post

 
# Publish post route
@router.patch("/posts/{post_id}/publish", tags=["Posts"], response_model=PostResponse)
def publish_post_route(post_id:int):
    post = publish_post(TEST_USER_ID, post_id)
    return post



