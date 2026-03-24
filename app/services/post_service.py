from datetime import datetime

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