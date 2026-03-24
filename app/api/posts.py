from src.schemas.post import Post, PostCreate, PostUpdate, PostResponse
from src.services.post_service import posts_db
from fastapi import APIRouter, HTTPException
from datetime import datetime
from typing import List, Optional

router = APIRouter()

# create a post
@router.post("/posts", tags=["Posts"], status_code=201)
async def create_post(post: PostCreate):
    new_id = max([p["id"] for p in posts_db], default=0) + 1
    new_post ={
        "id": new_id,
        "title": post.title,
        "content":post.content,
        "author_id": 1, # TODO: Get from authenticated user
        "created_at": datetime.now(),
        "updated_at": None
     }

    posts_db.append(new_post)

    return new_post


# update post
@router.put("/posts/{post_id}", tags=["Posts"], response_model=PostResponse)
async def update_post(update_post: PostUpdate, post_id: int):
    for i, post in enumerate( posts_db):
        if post["id"] == post_id:
            if update_post.title is not None:
                posts_db[i]["title"] = update_post.title
            if update_post.content is not None:
                posts_db[i]["content"] = update_post.content

            posts_db[i]["updated_at"] = datetime.now()
            return posts_db[i]
    
    raise HTTPException(status_code=404, detail="Post not found")
            
            

# get all posts
@router.get("/posts", tags=["Posts"], response_model=List[PostResponse])
async def read_posts():
    return posts_db

# get a single post
@router.get("/posts/{post_id}", tags=["Posts"], response_model=PostResponse)
async def get_post(post_id: int):
    for post in posts_db:
        if post["id"] == post_id:
            return post
    HTTPException(status_code=404, detail="Post not found")

# delete a post
@router.delete("/posts/{post_id}", tags=["Posts"], status_code=204)
async def delete_post(post_id: int):
    for i, post in enumerate(posts_db):
        if post["id"] == post_id:
            posts_db.pop(i)
            return
    
    raise HTTPException(status_code=404, detail="Post not found")



