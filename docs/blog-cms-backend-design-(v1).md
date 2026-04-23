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
- slug: string (nullable)
- status: string (default = "draft")
- user_id: foreign key → users.id
- created_at: datetime
- updated_at: datetime (nullable)
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

### Ownership and Access
- Only authenticated users can create and manage posts
- Every post must belong to a user
- Only the owner can edit or delete a post
- Only published posts are publicly visible

### Draft Rules
- Drafts can exist with incomplete data
- `title`, `content`, and `slug` may be `null` while a post is still a draft
- Whitespace-only `title` or `content` values are normalized to `null`
- If a draft has a valid title, a slug is generated from that title
- If a draft title changes, the slug is regenerated while the post is still in draft state
- If a draft title becomes empty after normalization, the slug becomes `null`

### Publish Rules
A post can only be published if:
- title is non-empty after normalization
- content is non-empty after normalization
- content length is at least 50 characters
- status is currently `draft`
- the title is unique among published posts

### Slug Rules
- Slug is derived from the normalized title
- Slug may exist during the draft phase
- Slug is finalized at publish time
- In V1, published posts are not editable. If published post editing is added later, the slug should remain stable by default and should not automatically change when the title is updated.

---

## 9. Visibility Rules

### Draft Posts
- Only accessible by the owner

### Published Posts
- Accessible by any visitor (public)

### Public Access Behavior
- Public queries should only return published posts
- Draft posts should not be exposed through the public access flow

---

## 10. Delete Policy

- Hard delete is used in V1
- Deleted posts are permanently removed from the system

---

## 11. Data Normalization Rules

Before validation or persistence:
- Leading and trailing whitespace is removed from `title` and `content`
- Empty strings and whitespace-only strings are converted to `null`

Examples:
- `"  FastAPI Guide  "` → `"FastAPI Guide"`
- `"   "` → `null`
- `""` → `null`

Purpose:
- keep stored data consistent
- avoid treating `""`, `"   "`, and `null` as different meanings of "empty"

---

## 12. API Input Schemas (Pydantic)

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
- slug
- status
- user_id
- created_at
- updated_at
- published_at

---

## 13. Core Service Methods

### create_draft(current_user, data)
- assign user_id from authenticated user
- normalize title/content
- generate slug if title exists
- set status = "draft"
- set created_at
- save post

---

### update_draft(post_id, current_user, data)
- fetch post by id
- check post exists
- check current user owns the post
- check status == "draft"
- normalize updated fields
- update title/content if provided
- regenerate slug if title changes
- set slug = `null` if title becomes empty after normalization
- set updated_at
- save post

---

### publish_post(post_id, current_user)
- fetch post by id
- check post exists
- check current user owns the post
- check status == "draft"
- validate title is non-empty after normalization
- validate content is non-empty after normalization
- validate content length ≥ 50
- validate title uniqueness among published posts
- finalize slug from title
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

### get_public_post(slug)
- fetch post by slug
- return post only if status == "published"
- otherwise treat as not publicly available

---

## 14. Edge Cases

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
- Cannot publish post with empty content
- Cannot publish post with content < 50 characters
- Cannot publish post if another published post already has the same normalized title

### Slug / Title Lifecycle
- Draft may have `slug = null` if title is missing
- Draft slug changes when draft title changes
- Published slug is treated as stable in V1

---

## 15. V1 Scope Decisions

Included:
- User + Post system
- Draft → Publish lifecycle
- Public read access
- Slug generation and stabilization
- Title uniqueness enforced at publish time

Excluded:
- Comments
- Likes / reactions
- Notifications
- Sharing
- View tracking
- Revisions/version history
- Published post editing
- Slug history / redirects

Reason:
Keep system focused on core content workflow and reduce complexity.

---

## 16. Open Questions (Future Iteration)

- Should published posts be allowed to revert to draft?
- Should admin roles be introduced with broader permissions?
- Should published posts be editable?
- If published titles change later, should slugs stay fixed or support redirects?
- Should uniqueness be enforced on title, slug, or both in later versions?
- Should versioning/revisions be supported?
