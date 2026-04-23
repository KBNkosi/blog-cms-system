# Blog System Architecture Plan

## 1. Mental Model

> Don't think "I'm building a blog." Think: **I'm building a content platform with multiple domains, and I should start with the core domain first.**

The goal is to design the system around:
- business rules
- state transitions
- ownership
- validation boundaries
- clear layering

---

## 2. Core Domains

A real blog system is not one thing — it's multiple subsystems.

| Domain | Responsibilities |
|--------|------------------|
| **User** | Users, profiles, roles |
| **Auth** | Registration, login, identity verification, access control |
| **Content** | Drafts, publishing, post visibility, slug lifecycle, content validation |
| **Engagement** | Comments, likes, bookmarks |
| **Discovery** | Search, tags, categories, feed |
| **System** | Logging, error handling, rate limiting, background jobs |

---

## 3. Core Domain Focus

### Core Domain: Content

The system starts with the **Content** domain because that is where the main business behavior lives.

Current focus:
- creating drafts
- updating drafts
- publishing posts
- controlling public visibility
- enforcing ownership
- managing slug lifecycle

### Supporting Domain: Auth

Authentication is important, but it supports the content workflow rather than defining it.

It will be introduced after the content rules and data flow are stable.

---

## 4. Architecture Style

**Modular Monolith** — structured internally into clear layers and domains, but deployed as one unit.

```text
/app
  /api              → Routes / controllers
  /services         → Business logic
  /models           → Database models
  /schemas          → Request / response validation
  /repositories     → Data access layer (planned)

  /core             → Config, security, utilities
  /domains
      /auth
      /users
      /posts
      /comments
      /engagement

  /db
  /tests
```

---

## 5. Request Flow

Every request follows this flow:

```
Client → API Route → Service Layer → Repository → Database
                          ↓
                    Business Logic
```

### Current Implementation Emphasis

The service layer is stabilized first, because it contains the core rules:

- ownership checks
- draft vs published state rules
- publish validation
- slug handling
- visibility rules

Only after the rules are stable should the same behavior be wired through routes and persistence.

---

## 6. Core Data Entities

Think in entities, not endpoints.

```
users
posts
comments
likes
tags
post_tags
```

### Current Entity Focus

Right now the main entity is:

**Post**

A user-owned piece of written content that:

- starts as a private draft
- may have incomplete data while in draft
- can be published for public access
- gets a slug derived from title
- uses slug as public identity once published

---

## 7. System Layers

```
┌─────────────────────────────────┐
│          API Layer              │  ← Routes / Controllers
├─────────────────────────────────┤
│        Service Layer            │  ← Business Logic
├─────────────────────────────────┤
│       Repository Layer          │  ← Data Access
├─────────────────────────────────┤
│        Database Layer           │  ← PostgreSQL / SQLite
└─────────────────────────────────┘
```

### Layer Responsibilities

- **API Layer**: request handling and response mapping
- **Service Layer**: business rules and workflows
- **Repository Layer**: persistence logic
- **Database Layer**: storage

---

## 8. Current Content Rules

### Draft Rules

- Drafts may have incomplete data
- title, content, and slug may be null in draft state
- Whitespace-only values are normalized to null
- If a draft has a valid title, a slug is generated from that title
- If the draft title changes, the slug updates while the post is still draft

### Publish Rules

A post can only be published if:

- it is in draft state
- the title is non-empty after normalization
- the content is non-empty after normalization
- the content length is at least 50 characters
- the title is unique among published posts
- the current user owns the post

### Visibility Rules

- Draft posts are private to the owner
- Only published posts are publicly accessible
- Public access uses slug, not post ID

---

## 9. Build Phases

### Phase 1 — Content Workflow ✅

Focus on the core content lifecycle before authentication and persistence complexity.

Implemented / stabilized:

- ✅ Create draft
- ✅ Update draft
- ✅ Publish post
- ✅ Get post for owner
- ✅ Get published post by slug
- ✅ Input normalization
- ✅ Ownership checks
- ✅ Publish validation rules
- ✅ Slug lifecycle handling
- ✅ Service-layer tests with pytest

---

### Phase 2 — Persistence Layer 🔄

Replace in-memory storage with database-backed persistence.

Next goals:

- [ ] SQLAlchemy models
- [ ] Repository layer
- [ ] Database session integration
- [ ] Migration setup

---

### Phase 3 — Auth System

Introduce identity and access control after the content workflow is stable.

Planned:

- [ ] User registration
- [ ] User login
- [ ] JWT token issuance and validation
- [ ] Protected routes
- [ ] Role-based access control

---

### Phase 4 — Engagement

- [ ] Comments
- [ ] Likes
- [ ] Bookmarks

---

### Phase 5 — Discovery

- [ ] Tags and categories
- [ ] Search
- [ ] Filtering and sorting
- [ ] Feed

---

### Phase 6 — System Design

- [ ] Caching
- [ ] Background jobs
- [ ] Rate limiting
- [ ] Logging and monitoring

---

## 10. Why Content Before Auth?

| Start with Auth | Start with Content |
|-----------------|-------------------|
| Build identity/security before the core workflow is understood | Understand the business workflow first |
| Harder to isolate core content rules | Easier to test and refine the main system behavior |
| Increases complexity early | Lets auth slot into a clearer system later |

### Reasoning

For this project, Content is the core domain and Auth is a supporting domain.

That means the better sequence is:

1. define the content workflow
2. stabilize business rules
3. test service logic
4. then add auth and persistence

---

## 11. Technology Stack

| Layer | Technology |
|-------|------------|
| Framework | FastAPI |
| Validation | Pydantic |
| Current storage | In-memory Python structures |
| Database (next) | SQLite → PostgreSQL |
| ORM | SQLAlchemy |
| Auth (planned) | JWT / python-jose |
| Testing | Pytest |
| Caching (later) | Redis |
| Background Jobs (later) | Celery or FastAPI BackgroundTasks |

---

## 12. Key Principles

- **Separation of concerns** — routes do routing, services do logic, repositories do persistence
- **Domain-first thinking** — define entities, rules, and workflows before expanding features
- **State-driven design** — draft and published are not just labels; they define behavior
- **Validation boundaries** — drafts are flexible, publish is strict
- **Testability first** — service logic should be testable before routes and persistence
- **Iterative complexity** — build the foundation first, then add auth, persistence, and system concerns
