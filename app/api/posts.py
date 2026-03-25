from app.schemas.post import PostCreate, PostUpdate, PostResponse
from app.services.post_service import create_post, update_post, get_all_post, get_post, delete_post
from fastapi import APIRouter
from typing import List

router = APIRouter()

# create a post
@router.post("/posts", tags=["Posts"], status_code=201)
async def create_post_route(post: PostCreate):   
  new_post = await create_post(post)
  return new_post
   

# update post
@router.put("/posts/{post_id}", tags=["Posts"], response_model=PostResponse)
async def update_post_route(post: PostUpdate, post_id: int):    
    updated_post = await update_post(post, post_id)
    return updated_post
            
            
# get all posts
@router.get("/posts", tags=["Posts"], response_model=List[PostResponse])
async def read_posts_route():
    return await get_all_post()

# get a single post
@router.get("/posts/{post_id}", tags=["Posts"], response_model=PostResponse)
async def get_post_route(post_id: int):
    post = await get_post(post_id)
    return post
    
    
# delete a post
@router.delete("/posts/{post_id}", tags=["Posts"], status_code=204)
async def delete_post(post_id: int):
  await delete_post(post_id)
  return 



