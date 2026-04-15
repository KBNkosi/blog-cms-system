from datetime import datetime
from fastapi import HTTPException


posts_db = [
    {
        "id": 1,
        "title": "Getting Started with FastAPI",
        "slug": "getting-started-with-fastapi",
        "content": (
            "FastAPI is a modern, fast web framework for building APIs with Python. "
            "It's built on top of Starlette and Pydantic, providing automatic validation "
            "and documentation. In this post, we'll explore the basics of setting up a "
            "FastAPI application and creating your first endpoints."
        ),
        "status": "draft",
        "user_id": 1,
        "created_at": datetime(2024, 1, 15, 10, 30),
        "updated_at": None,
        "published_at": None,
    },
    {
        "id": 2,
        "title": "I am there: features every developer should know",
        "slug": "i-am-there:-features-every-developer-should-know",
        "content": (
            "Features that every developer should know. We'll also discuss project "
            "structure and testing strategies."
        ),
        "status": "draft",
        "user_id": 2,
        "created_at": datetime(2024, 1, 20, 14, 45),
        "updated_at": datetime(2024, 1, 21, 9, 15),
        "published_at": None,
    },
    {
        "id": 3,
        "title": "Database Design Patterns",
        "slug": "database-design-patterns",
        "content": (
            "Understanding database design patterns is crucial for building scalable "
            "applications. This post explores normalization, indexing strategies, "
            "relationship modeling, and when to use NoSQL vs SQL databases. We'll also "
            "look at real-world examples and common pitfalls to avoid."
        ),
        "status": "draft",
        "user_id": 1,
        "created_at": datetime(2024, 2, 1, 16, 20),
        "updated_at": None,
        "published_at": None,
    },
]

# create post draft
def create_post_draft(current_user_id:int, draft_data: dict)-> dict:
    new_id = max(post["id"] for post in posts_db) + 1
    new_post = {
        "id": new_id,
        "title": draft_data.get("title"),
        "content": draft_data.get("content"),
        "status": "draft",
        "user_id": current_user_id,
        "created_at": datetime.now(),
        "updated_at": None,
        "published_at": None,
    }

    posts_db.append(new_post)

    return new_post

# Function to get post by id
def get_post_by_id(post_id:int) -> dict:
    for post in posts_db:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=404, detail="post not found")

# Validate post ownership
def validate_post_ownership(user_id:int, post_data:dict) -> None:
    if post_data["user_id"] != user_id:
        raise HTTPException(status_code=400, detail="cannot access another users'post")

#Function to check status of the post
def check_post_status(post) -> None:
  if post["status"] != "draft":
        raise HTTPException(status_code=400, detail="Post is already published")

# Function to get post for the owner
def get_post_for_owner(post_id: int, user_id: int)-> dict:
    post = get_post_by_id(post_id)
    validate_post_ownership(user_id, post)

    return post

# Function to get published post
def get_public_post(slug:str)-> dict:  
   for post in posts_db:
     if post.get("slug") == slug:
        if post.get("status") == "published":
            return post
        else:
            raise HTTPException(status_code=403, detail="post is not public")

   raise HTTPException(status_code=404, detail="post not found")
  

# Function to update post
def update_post(post_id: int, user_id:int, post_data: dict) -> dict:
    post = get_post_by_id(post_id)
    validate_post_ownership(user_id, post)
    check_post_status(post)

    for field in ["title", "content"]:
        if post_data[field] is not None:
            post[field] = post_data[field]

    post["updated_at"] = datetime.now()

    return post


# Function to validate post against publishing rules
def validate_post_publishability(post_data: dict) -> None:
    check_post_status(post_data)
    title = post_data["title"].strip()
    content = post_data["content"].strip()

    if not title:
        raise HTTPException(status_code=400, detail="Title cannot be empty")
    if len(content) < 50:
        raise HTTPException(status_code=400, detail="Content cannot be less than 50 characters long")
        

# Publish Post
def publish_post(current_user_id: int, post_id:int) -> dict:

    post = get_post_by_id(post_id)

    validate_post_ownership(current_user_id, post)    
    
    validate_post_publishability(post)

    post["status"] = "published"
    post["published_at"] = datetime.now()

    return post

