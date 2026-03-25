from datetime import datetime
from fastapi import HTTPException


posts_db = [
    {
        "id": 1,
        "title": "Getting Started with FastAPI",
        "content": "FastAPI is a modern, fast web framework for building APIs with Python. It's built on top of Starlette and Pydantic, providing automatic validation and documentation. In this post, we'll explore the basics of setting up a FastAPI application and creating your first endpoints.",
        "author_id": 1,
        "created_at": datetime(2024, 1, 15, 10, 30),
        "updated_at": None
    },
    {
        "id": 2,
        "title": "Python Best Practices for 2024",
        "content": "As Python continues to evolve, it's important to stay updated with the latest best practices. This post covers type hints, dependency injection, async programming, and modern Python features that every developer should know. We'll also discuss project structure and testing strategies.",
        "author_id": 2,
        "created_at": datetime(2024, 1, 20, 14, 45),
        "updated_at": datetime(2024, 1, 21, 9, 15)
    },
    {
        "id": 3,
        "title": "Database Design Patterns",
        "content": "Understanding database design patterns is crucial for building scalable applications. This post explores normalization, indexing strategies, relationship modeling, and when to use NoSQL vs SQL databases. We'll also look at real-world examples and common pitfalls to avoid.",
        "author_id": 1,
        "created_at": datetime(2024, 2, 1, 16, 20),
        "updated_at": None
    }
]


async def create_post(post):
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

async def update_post(post_data, post_id):
    for i, existing_post in enumerate( posts_db):
        if existing_post["id"] == post_id:
            if post_data.title is not None:
                posts_db[i]["title"] = post_data.title
            if post_data.content is not None:
                posts_db[i]["content"] = post_data.content

            posts_db[i]["updated_at"] = datetime.now()
            return posts_db[i]
    
    raise HTTPException(status_code=404, detail="Post not found")

async def get_all_post():
    return posts_db

async def get_post(post_id):
    for post in posts_db:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post not found")

async def delete_post(post_id):
    for i, post in enumerate(posts_db):
        if post["id"] == post_id:
            posts_db.pop(i)
            return
    
    raise HTTPException(status_code=404, detail="Post not found")
