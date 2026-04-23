import copy
from datetime import datetime

import pytest
from fastapi import HTTPException

from app.services.post_service import (
    posts_db,
    create_post_draft,
    get_post_by_id,
    get_post_for_owner,
    get_public_post,
    update_post,
    publish_post,
)

# Baseline test data, each test will start from this clean state.
INITIAL_POSTS = [
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


# Reset the shared posts_db before each test.
@pytest.fixture(autouse=True)
def reset_posts_db():
    posts_db.clear()
    posts_db.extend(copy.deepcopy(INITIAL_POSTS))

def test_create_draft_allows_missing_title_and_content():
    draft = create_post_draft(current_user_id=1, draft_data={})

    assert draft["id"] == 4
    assert draft["title"] is None
    assert draft["content"] is None
    assert draft["slug"] is None
    assert draft["status"] == "draft"
    assert draft["user_id"] == 1
    assert draft["created_at"] is not None
    assert draft["updated_at"] is None
    assert draft["published_at"] is None

def test_create_draft_normalizes_whitespace_and_generates_slug():
    draft = create_post_draft(
        current_user_id=1,
        draft_data={
            "title": "  My First Post  ",
            "content": "  This is a valid draft body with enough meaning.  ",
        },
    )

    assert draft["title"] == "My First Post"
    assert draft["content"] == "This is a valid draft body with enough meaning."
    assert draft["slug"] == "my-first-post"

def test_get_post_by_id_returns_post():
    post = get_post_by_id(1)

    assert post["id"] == 1
    assert post["title"] == "Getting Started with FastAPI"

def test_get_post_for_owner_returns_owned_post():
    post = get_post_for_owner(post_id=1, user_id=1)

    assert post["id"] == 1
    assert post["user_id"] == 1

def test_get_post_for_owner_raises_403_for_non_owner():
    with pytest.raises(HTTPException) as exc_info:
        get_post_for_owner(post_id=1, user_id=2)

    assert exc_info.value.status_code == 403
    assert exc_info.value.detail == "cannot access another user's post"

def test_update_post_updates_only_provided_fields():
    original_post = get_post_by_id(1)
    original_content = original_post["content"]

    updated_post = update_post(
        post_id=1,
        user_id=1,
        post_data={"title": "  Updated FastAPI Title  "},
    )

    assert updated_post["title"] == "Updated FastAPI Title"
    assert updated_post["slug"] == "updated-fastapi-title"
    assert updated_post["content"] == original_content
    assert updated_post["updated_at"] is not None


def test_update_post_can_clear_title_and_slug():
    updated_post = update_post(
        post_id=1,
        user_id=1,
        post_data={"title": "   "},
    )

    assert updated_post["title"] is None
    assert updated_post["slug"] is None

def test_update_post_raises_403_for_non_owner():
    with pytest.raises(HTTPException) as exc_info:
        update_post(
            post_id=1,
            user_id=2,
            post_data={"title": "Trying to edit someone else's draft"},
        )

    assert exc_info.value.status_code == 403
    assert exc_info.value.detail == "cannot access another user's post"

def test_update_post_raises_400_if_post_is_not_draft():
    post = get_post_by_id(1)
    post["status"] = "published"

    with pytest.raises(HTTPException) as exc_info:
        update_post(
            post_id=1,
            user_id=1,
            post_data={"title": "Should fail"},
        )

    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "post is not in draft state"

def test_publish_post_successfully_publishes_valid_draft():
    post = get_post_by_id(1)
    post["title"] = "FastAPI Publishing Guide"
    post["slug"] = "fastapi-publishing-guide"
    post["content"] = (
        "This post explains how publishing works in FastAPI applications "
        "with validation, ownership rules, and proper service design."
    )

    published_post = publish_post(current_user_id=1, post_id=1)

    assert published_post["status"] == "published"
    assert published_post["slug"] == "fastapi-publishing-guide"
    assert published_post["published_at"] is not None
    assert published_post["updated_at"] is not None

def test_publish_post_raises_400_for_empty_title():
    post = get_post_by_id(1)
    post["title"] = "   "
    post["content"] = (
        "This content is definitely long enough to pass the length validation."
    )

    with pytest.raises(HTTPException) as exc_info:
        publish_post(current_user_id=1, post_id=1)

    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "title cannot be empty"


def test_publish_post_raises_400_for_short_content():
    post = get_post_by_id(1)
    post["title"] = "A Valid Title"
    post["content"] = "Too short"

    with pytest.raises(HTTPException) as exc_info:
        publish_post(current_user_id=1, post_id=1)

    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "content must be at least 50 characters long"

def test_publish_post_rejects_duplicate_published_title():
    existing_post = get_post_by_id(2)
    existing_post["title"] = "Duplicate Title"
    existing_post["status"] = "published"
    existing_post["slug"] = "duplicate-title"
    existing_post["published_at"] = datetime.now()

    target_post = get_post_by_id(1)
    target_post["title"] = "  Duplicate Title  "
    target_post["content"] = (
        "This content is long enough to satisfy the publishing rules easily."
    )

    with pytest.raises(HTTPException) as exc_info:
        publish_post(current_user_id=1, post_id=1)

    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "a published post with this title already exists"


def test_get_public_post_returns_published_post():
    post = get_post_by_id(1)
    post["status"] = "published"
    post["published_at"] = datetime.now()

    public_post = get_public_post("getting-started-with-fastapi")

    assert public_post["id"] == 1
    assert public_post["status"] == "published"



def test_get_public_post_raises_404_for_draft_post():
    with pytest.raises(HTTPException) as exc_info:
        get_public_post("getting-started-with-fastapi")

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "post not found"