# HTTP Status Codes & Exceptions Guide

## Quick Answer
**Successful post creation:** `201 Created`

---

## HTTP Status Code Categories

### 1. Success Codes (2xx)

#### `200 OK`
- **Purpose:** Request succeeded
- **When to use:** GET, PUT, PATCH, DELETE operations that complete successfully
- **Examples:** 
  - Get a post
  - Update a post
  - Delete a post

#### `201 Created`
- **Purpose:** Resource successfully created
- **When to use:** POST operations that create new resources
- **Examples:**
  - Create a new post
  - Create a new user
- **Response:** Should include the newly created resource

#### `204 No Content`
- **Purpose:** Request succeeded, but no response body
- **When to use:** DELETE operations or updates where no data needs to be returned
- **Examples:**
  - Delete a post
  - Update a post where client already has the updated data

---

### 2. Client Error Codes (4xx)

#### `400 Bad Request`
- **Purpose:** Invalid request from client
- **When to use:** Validation errors, malformed data
- **Examples:**
  - Empty title when publishing
  - Content too short
  - Invalid post data format

#### `401 Unauthorized`
- **Purpose:** Authentication required
- **When to use:** User not logged in or invalid credentials
- **Examples:**
  - Missing authentication token
  - Invalid login credentials

#### `403 Forbidden`
- **Purpose:** Authenticated but not allowed
- **When to use:** User doesn't have permission for specific action
- **Examples:**
  - Trying to edit another user's post
  - Admin-only endpoints accessed by regular user

#### `404 Not Found`
- **Purpose:** Resource doesn't exist
- **When to use:** Requested resource not found
- **Examples:**
  - Post ID doesn't exist
  - User ID doesn't exist

#### `409 Conflict`
- **Purpose:** Request conflicts with current state
- **When to use:** Resource state conflicts with operation
- **Examples:**
  - Trying to publish an already published post
  - Creating duplicate resource with unique constraint

---

### 3. Server Error Codes (5xx)

#### `500 Internal Server Error`
- **Purpose:** Unexpected server error
- **When to use:** Unhandled exceptions, database errors
- **Examples:**
  - Database connection failed
  - Unexpected code exceptions

---

## FastAPI HTTPException Usage

### Basic Exception Structure
```python
from fastapi import HTTPException

raise HTTPException(
    status_code=400,
    detail="Human readable error message"
)
```

### Common Exception Patterns

#### Validation Errors
```python
# 400 Bad Request
raise HTTPException(
    status_code=400,
    detail="Title cannot be empty"
)

raise HTTPException(
    status_code=400,
    detail="Content must be at least 50 characters"
)
```

#### Not Found Errors
```python
# 404 Not Found
raise HTTPException(
    status_code=404,
    detail="Post not found"
)
```

#### Permission Errors
```python
# 403 Forbidden
raise HTTPException(
    status_code=403,
    detail="Cannot access another user's post"
)
```

#### State Conflict Errors
```python
# 409 Conflict
raise HTTPException(
    status_code=409,
    detail="Post is already published"
)
```

---

## Blog CMS Specific Status Codes

### Post Operations

#### Create Post
```python
@router.post("/posts", status_code=201, response_model=PostResponse)
async def create_post(post: PostCreateDraft):
    # Create post logic
    return new_post  # Returns 201 with created post
```

#### Update Post
```python
@router.put("/posts/{post_id}", response_model=PostResponse)
async def update_post(post_id: int, post: PostUpdateDraft):
    # Update logic
    return updated_post  # Returns 200 with updated post
```

#### Delete Post
```python
@router.delete("/posts/{post_id}", status_code=204)
async def delete_post(post_id: int):
    # Delete logic
    return None  # Returns 204 with no content
```

#### Publish Post
```python
@router.patch("/posts/{post_id}/publish", response_model=PostResponse)
async def publish_post(post_id: int):
    # Publish logic
    return published_post  # Returns 200 with published post
```

#### Get Post
```python
@router.get("/posts/{post_id}", response_model=PostResponse)
async def get_post(post_id: int):
    # Get logic
    return post  # Returns 200 with post data
```

---

## Error Response Format

### FastAPI Default Error Response
```json
{
  "detail": "Human readable error message"
}
```

### Custom Error Response (Optional)
```python
from fastapi import HTTPException
from pydantic import BaseModel

class ErrorResponse(BaseModel):
    error: str
    message: str
    details: dict = {}

# Usage
raise HTTPException(
    status_code=400,
    detail={
        "error": "ValidationError",
        "message": "Title cannot be empty",
        "details": {"field": "title", "value": ""}
    }
)
```

---

## Best Practices

### 1. Be Specific with Status Codes
- Use `201` for creation, not `200`
- Use `404` for missing resources, not `400`
- Use `409` for state conflicts, not `400`

### 2. Provide Clear Error Messages
```python
# Bad
raise HTTPException(status_code=400, detail="Error")

# Good
raise HTTPException(status_code=400, detail="Title cannot be empty")
```

### 3. Use Appropriate HTTP Methods
- `POST` for creation
- `GET` for retrieval
- `PUT/PATCH` for updates
- `DELETE` for deletion

### 4. Consistent Error Handling
Create helper functions for common errors:
```python
def raise_not_found(resource: str):
    raise HTTPException(status_code=404, detail=f"{resource} not found")

def raise_validation_error(message: str):
    raise HTTPException(status_code=400, detail=message)
```

### 5. Log Errors for Debugging
```python
import logging

logger = logging.getLogger(__name__)

@router.post("/posts")
async def create_post(post: PostCreateDraft):
    try:
        # Create post logic
        return new_post
    except Exception as e:
        logger.error(f"Failed to create post: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
```

---

## Testing Status Codes

### Using TestClient
```python
from fastapi.testclient import TestClient

def test_create_post():
    response = client.post("/posts", json={"title": "Test", "content": "Test content"})
    assert response.status_code == 201

def test_get_nonexistent_post():
    response = client.get("/posts/999")
    assert response.status_code == 404

def test_publish_empty_title():
    response = client.patch("/posts/1/publish")
    assert response.status_code == 400
    assert response.json()["detail"] == "Title cannot be empty"
```

---

## Summary

- **201 Created** for successful resource creation
- **200 OK** for successful operations that return data
- **204 No Content** for successful operations with no return data
- **400 Bad Request** for validation errors
- **401 Unauthorized** for authentication issues
- **403 Forbidden** for permission issues
- **404 Not Found** for missing resources
- **409 Conflict** for state conflicts
- **500 Internal Server Error** for unexpected server issues

Use these consistently across your API for predictable and RESTful behavior.
