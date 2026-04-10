# Blog CMS – Backend Design (V1)

## 1. System Purpose
A blog CMS that allows users to create, manage, and publish written content.

Users can:
- create drafts
- update drafts
- publish posts
- read published posts

---

## 2. Actor

### User
A single entity that can:
- create and manage their own posts
- read published posts

---

## 3. Core Entities (V1)

### User
Represents a registered user of the platform.

### Post
A user-owned piece of written content that:
- starts as a private draft
- can be published for public viewing

---

## 4. Relationships

- A user can have many posts
- Each post belongs to exactly one user

---

## 5. Post Model (Database Schema)

Fields:

- id: integer (primary key)
- title: string (nullable)
- content: text (nullable)
- status: string (default = "draft")
- user_id: foreign key → users.id
- created_at: datetime
- updated_at: datetime
- published_at: datetime (nullable)

---

## 6. Post States

- draft
- published

---

## 7. State Transitions

- draft → published
- draft → deleted (hard delete)
- published → deleted (hard delete)

Note:
- Published posts cannot revert back to draft (V1 simplification)

---

## 8. Core Rules

- Only authenticated users can create and manage posts
- Every post must belong to a user
- Drafts can exist with incomplete data
- A post can only be published if:
  - title is non-empty
  - content length ≥ 50 characters
- Only published posts are publicly visible
- Only the owner can edit or delete a post

---

## 9. Visibility Rules

- Draft posts:
  - Only accessible by the owner

- Published posts:
  - Accessible by any visitor (public)

---

## 10. Delete Policy

- Hard delete is used in V1
- Deleted posts are permanently removed from the system

---

## 11. API Input Schemas (Pydantic)

### PostCreateDraft
- title: optional string
- content: optional string

### PostUpdateDraft
- title: optional string
- content: optional string

### PostResponse
- id
- title
- content
- status
- user_id
- created_at
- updated_at
- published_at

---

## 12. Core Service Methods

### create_draft(current_user, data)
- assign user_id from authenticated user
- set title/content if provided
- set status = "draft"
- set created_at
- save post

---

### update_draft(post_id, current_user, data)
- fetch post by id
- check post exists
- check current user owns the post
- check status == "draft"
- update title/content if provided
- set updated_at
- save post

---

### publish_post(post_id, current_user)
- fetch post by id
- check post exists
- check current user owns the post
- check status == "draft"
- validate title is non-empty
- validate content length ≥ 50
- set status = "published"
- set published_at
- set updated_at
- save post

---

### get_post_for_owner(post_id, current_user)
- fetch post by id
- check post exists
- check current user owns the post
- return post

---

### get_public_post(post_id)
- fetch post by id
- check post exists
- check status == "published"
- return post

---

## 13. Edge Cases

### Ownership / Permission
- User cannot access another user's draft
- User cannot update or delete another user's post
- User cannot publish another user's draft

### State Errors
- Cannot publish an already published post
- Cannot update a post using draft logic if it is already published

### Missing Resource
- If post does not exist, return error and terminate operation

### Validation Errors
- Cannot publish post with empty title
- Cannot publish post with content < 50 characters

---

## 14. V1 Scope Decisions

Included:
- User + Post system
- Draft → Publish lifecycle
- Public read access

Excluded:
- Comments
- Likes / reactions
- Notifications
- Sharing
- View tracking
- Revisions/version history

Reason:
Keep system focused on core content workflow and reduce complexity.

---

## 15. Open Questions (Future Iteration)

- Should published posts be allowed to revert to draft?
- Should admin roles be introduced with broader permissions?
- Should soft delete be implemented instead of hard delete?
- Should public posts use slugs instead of IDs?
- Should versioning/revisions be supported?
