from datetime import datetime
from fastapi import HTTPException
from slugify import slugify

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
        "slug": "i-am-there-features-every-developer-should-know",
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

# function to normalize empty strings and whitespaces
def normalize_text(value: str | None) -> str | None:
    if value is None:
        return None

    cleaned = value.strip()
    return cleaned if cleaned else None


# function to generate slug from title
def generate_slug_from_title(title: str | None) -> str | None:
    if title is None:
        return None
    
    return slugify(title)

# function to ensure title is unique before publishing
def ensure_title_is_unique_for_publish(title, current_post_id):
    normalized_title = normalize_text(title)

    if normalized_title is None:
        return

    for post in posts_db:
        if post["id"] == current_post_id:
            continue

        if post["status"] != "published":
            continue

        existing_title = normalize_text(post.get("title"))
        if existing_title is None:
            continue

        if existing_title.lower() == normalized_title.lower():
            raise HTTPException(status_code=400, detail="a published post with this title already exists")

# create post draft
def create_post_draft(current_user_id:int, draft_data: dict)-> dict:
    new_id = max((post["id"] for post in posts_db), default=0) + 1
    clean_title = normalize_text(draft_data.get("title"))
    clean_content = normalize_text(draft_data.get("content"))
    
    new_post = {
        "id": new_id,
        "title": clean_title,
        "slug": generate_slug_from_title(clean_title),
        "content": clean_content,
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

# Function to validate post ownership
def validate_post_ownership(user_id:int, post_data:dict) -> None:
    if post_data["user_id"] != user_id:
        raise HTTPException(status_code=403, detail="cannot access another user's post")

#Function to check post status is draft
def ensure_post_is_draft(post) -> None:
  if post["status"] != "draft":
        raise HTTPException(status_code=400, detail="post is not in draft state")

# Function to get post for the owner
def get_post_for_owner(post_id: int, user_id: int)-> dict:
    post = get_post_by_id(post_id)
    validate_post_ownership(user_id, post)
    return post

# Function to get published post
def get_public_post(slug:str)-> dict:  
   for post in posts_db:
     if post.get("slug") == slug and post.get("status") == "published":
        return post

   raise HTTPException(status_code=404, detail="post not found")
  

# Function to update post
def update_post(post_id: int, user_id:int, post_data: dict) -> dict:
    post = get_post_by_id(post_id)
    validate_post_ownership(user_id, post)
    ensure_post_is_draft(post)

    title_was_provided = "title" in post_data

    for field in ["title", "content"]:
        if field in post_data:
            post[field] = normalize_text(post_data[field])
    
    if title_was_provided:
        post["slug"] = generate_slug_from_title(post["title"])

    post["updated_at"] = datetime.now()
    return post


# Function to validate post against publishing rules
def validate_post_publishability(post_data: dict) -> None:
    title = normalize_text(post_data.get("title")) 
    content = normalize_text(post_data.get("content"))

    if not title:
        raise HTTPException(status_code=400, detail="title cannot be empty")

    if not content:
         raise HTTPException(status_code=400, detail="content cannot be empty")

    if len(content) < 50:
        raise HTTPException(status_code=400, detail="content must be at least 50 characters long")
        

# Publish Post
def publish_post(current_user_id: int, post_id:int) -> dict:
    post = get_post_by_id(post_id)
    validate_post_ownership(current_user_id, post)
    ensure_post_is_draft(post)    
    validate_post_publishability(post)
    ensure_title_is_unique_for_publish(post["title"], post["id"])
    
    # Finalize slug from the validated, normalized title.
    post["slug"] = generate_slug_from_title(post["title"])
    post["status"] = "published"
    post["updated_at"] = datetime.now()
    post["published_at"] = datetime.now()

    return post

