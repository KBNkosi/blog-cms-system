# Blog System Architecture Plan

## 1. Mental Model

> Don't think "I'm building authentication." Think **"I'm building a content platform system with multiple domains."**

---

## 2. Core Domains

A real blog system is not one thing — it's multiple subsystems:

| Domain | Responsibilities |
|--------|-----------------|
| **User** | Users, Profiles, Roles (admin, author, reader) |
| **Auth** | Login / Register, JWT Tokens, Permissions |
| **Content** | Posts, Drafts, Publishing, Editing |
| **Engagement** | Comments, Likes, Bookmarks |
| **Discovery** | Search, Tags, Categories, Feed |
| **System** | Logging, Error handling, Rate limiting, Background jobs |

---

## 3. Architecture Style

**Modular Monolith** — structured internally like microservices, deployed as one unit.

```
/app
  /api              → Routes (controllers)
  /services         → Business logic
  /models           → Database models
  /schemas          → Request/response validation
  /repositories     → DB access layer

  /core             → Config, security, utils
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

## 4. Request Flow

Every request follows this flow:

```
Client → API Route → Service Layer → Repository → Database
                          ↓
                    Business Logic
```

### Example: `POST /posts`

```
→ Route handles request
→ Service validates business rules
→ Repository saves to DB
→ Response returned
```

> This separation is what makes systems scalable later.

---

## 5. Core Data Entities

Think in **entities**, not endpoints.

```
users
posts
comments
likes
tags
post_tags   ← many-to-many join table
```

---

## 6. System Layers

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

---

## 7. Build Phases

### Phase 1 — Content System *(Start Here)*

> Focus on data flow and structure before adding security concerns.

- [ ] Create post
- [ ] Get all posts (with pagination)
- [ ] Get single post
- [ ] Update post
- [ ] Delete post
- [ ] Basic request validation

---

### Phase 2 — Auth System

> Auth is a cross-cutting concern. Build it once you understand the system.

- [ ] User registration
- [ ] User login
- [ ] JWT token issuance & validation
- [ ] Role-based access control (admin, author, reader)
- [ ] Protected routes

---

### Phase 3 — Engagement

- [ ] Comments (create, read, delete)
- [ ] Likes (toggle)
- [ ] Bookmarks

---

### Phase 4 — Discovery

- [ ] Tags & categories
- [ ] Full-text search
- [ ] Feed (latest / trending posts)
- [ ] Filtering & sorting

---

### Phase 5 — System Design

- [ ] Caching (Redis)
- [ ] Background jobs (emails, notifications)
- [ ] Rate limiting
- [ ] Logging & monitoring

---

## 8. Why Posts Before Auth?

| Start with Auth | Start with Posts |
|-----------------|-----------------|
| Build security without understanding the system | Understand data flow first |
| Auth becomes an over-engineered bottleneck | Auth slots in cleanly later |
| Hard to test business logic in isolation | Easy to test and iterate quickly |

> Auth is not core business logic — it's infrastructure. Defer it intentionally.

---

## 9. Technology Stack

| Layer | Technology |
|-------|-----------|
| Framework | FastAPI (Python) |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Validation | Pydantic |
| Auth | JWT (python-jose) |
| Caching *(Phase 5)* | Redis |
| Background Jobs *(Phase 5)* | Celery or FastAPI BackgroundTasks |

---

## 10. Key Principles

- **Separation of concerns** — routes do routing, services do logic, repos do data access
- **Domain-driven structure** — code is organized by business domain, not technical layer alone
- **Iterative complexity** — start simple, add complexity only when the foundation is solid
- **Testability first** — each layer can be tested independently
