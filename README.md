# Blog CMS System

## 🎯 Purpose

A backend-focused Blog CMS built to practice **system design through implementation**, not just feature building.

The project focuses on:
- defining clear domain rules
- enforcing state transitions
- separating flexible and strict validation boundaries
- building a system that is consistent and testable

---

## 📋 Overview

A **backend system for managing blog posts** with a focus on the **draft → publish lifecycle**.

Instead of treating posts as simple CRUD resources, the system is designed around:
- ownership rules
- state transitions
- validation boundaries
- public vs private access

---

## 🚧 Current Status

**Phase:** Content System (Service Layer Stabilized)

### ✅ Completed
- Draft → Publish workflow
- Slug lifecycle implementation
- Input normalization
- Ownership and permission enforcement
- Public vs private access rules
- Service-layer test coverage using pytest

### 🔄 Next
- Database integration (SQLAlchemy)
- Authentication system

---

## 🏗️ Architecture

### Architecture Style: Modular Monolith

The system is structured as a modular monolith, with clear separation between layers while remaining a single deployable unit.

### System Flow
```
Client → API Route → Service Layer → Repository → Database
                          ↓
                    Business Logic
```

| Layer | Responsibility |
|------|----------------|
| **API Layer** | Handles HTTP requests |
| **Service Layer** | Business logic and rules |
| **Repository Layer** | Data access (planned) |
| **Database Layer** | Persistence (planned) |

---

## 🧠 Core Design Decisions

### Draft vs Publish Separation
The system distinguishes between flexible draft behavior and strict publish rules.

- Drafts allow incomplete data (nullable title/content)
- Publishing enforces validation:
  - title must exist
  - content must be ≥ 50 characters
  - title must be unique among published posts

---

### Slug Lifecycle
Slug is treated as a **public identifier**:

- Generated from title during draft creation/update
- Updated when draft title changes
- Finalized at publish time
- Treated as stable after publishing (V1)

---

### Input Normalization
User input is normalized before validation:

- Leading/trailing whitespace is removed
- Empty strings are converted to `null`
- Prevents inconsistent data states

---

### Service-First Design
Business logic is implemented in the service layer before routes:

- Ownership validation
- State enforcement (draft vs published)
- Publish rules

This allows logic to be tested independently of HTTP or database layers.

---

### Public vs Private Access
- Draft posts are private to the owner
- Only published posts are publicly accessible
- Public access is based on `slug`, not `id`

---

## 🚀 Features (Implemented)

- Draft system with incomplete data support
- Draft update workflow with slug synchronization
- Publish workflow with strict validation rules
- Slug-based public access
- Ownership and permission enforcement
- Service-layer test coverage using pytest

---

## 📚 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/posts/drafts` | Create draft |
| PATCH | `/posts/{id}` | Update draft |
| PATCH | `/posts/{id}/publish` | Publish post |
| GET | `/posts/{id}` | Get post (owner) |
| GET | `/posts/public/{slug}` | Get published post |

---

## 🛠️ Technology Stack

| Layer | Technology |
|------|-----------|
| Framework | FastAPI |
| Validation | Pydantic |
| Testing | Pytest |
| Database (planned) | SQLite → PostgreSQL |
| ORM (planned) | SQLAlchemy |
| Migrations (planned) | Alembic |

---

## 🧪 Testing

```bash
pytest
```

Tests focus on:

- draft creation and updates
- publish validation rules
- ownership enforcement
- public vs private access behavior

---

## 📈 Development Phases

### Phase 1: Content System ✅
- Draft → Publish workflow
- Validation rules
- Slug lifecycle
- Service-layer testing

### Phase 2: Authentication 🔄
- User identity
- Protected routes
- Access control

### Phase 3+: Future Expansion
- Engagement (comments, likes)
- Discovery (search, tags)
- System concerns (caching, logging)

---

## 🔮 Future Considerations

- Editing published posts with slug stability or redirect strategy
- Pagination and filtering
- Role-based access control
- Performance optimization

---

## 📄 License

MIT License, open for learning and professional development.

