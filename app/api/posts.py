from app.schemas.post import PostCreateDraft, PostUpdateDraft, PostResponse
from app.services.post_service import publish_post, create_post_draft, update_post, get_post_for_owner, get_public_post
from fastapi import APIRouter
from slugify import slugify

router = APIRouter()

            
# Create post draft
@router.post("/posts", tags=["Posts"],  response_model=PostResponse, status_code=201,)
def create_post_draft_route(post_data: PostCreateDraft):
    # For testing: hardcoded user ID
    current_user_id = 5 # Test user
    post_data_dict = post_data.model_dump()
    new_post = create_post_draft(current_user_id, post_data_dict)

    return new_post

# Get post for owner
@router.get("/posts/{post_id: int}", tags=["Posts"], response_model=PostResponse, status_code=200)
def get_post_for_owner_route(post_id:int):
    # For testing: hardcoded user ID
    current_user_id = 1 # Test user 
    post = get_post_for_owner(post_id, current_user_id)

    return post

# search public post
@router.get("/posts/search", tags=["Posts"], response_model=PostResponse, status_code=200)
def search_public_post_route(q: str):
    print(f"search query: {q}")
    target_slug = slugify(q)
    print(f"generated slug: {target_slug}")
    
    post = get_public_post(target_slug)

    print(f"found post: {post}")

    return post

    

# Update post
@router.put("/posts/{post_id}", tags=["Posts"], response_model=PostResponse, status_code=200)
def update_post_route(post_id: int, post_data:PostUpdateDraft):
    # For testing: hardcoded user ID
    current_user_id = 1 # Test user 
    post_data_dict = post_data.model_dump()
    updated_post = update_post(post_id, current_user_id, post_data_dict)

    return updated_post

 
# Publish post route
@router.patch("/posts/{post_id}/publish", tags=["Posts"], response_model=PostResponse)
def publish_post_route(post_id:int):
    # For testing: hardcoded user ID
    current_user_id = 1 # Test user 

    post = publish_post(current_user_id, post_id)
    return post



