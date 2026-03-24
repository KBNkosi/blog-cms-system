# Blog System — Beginner to Junior Build Plan

> **How to use this document**
> Work through each phase in order. Do not skip phases.
> Each phase has three sections: **Learn first**, **Then build**, and **You're ready when...**
> Only move to the next phase when you can tick every checkbox.

---

## Overview

| Phase | Name | Focus | Est. Study Time |
|-------|------|-------|-----------------|
| 0 | Foundation | Python + Tools Setup | 1–2 weeks |
| 1 | Content System | Post CRUD + Data Flow | 2–3 weeks |
| 2 | Database Layer | SQL + SQLAlchemy | 2–3 weeks |
| 3 | Auth System | JWT + Protected Routes | 2–3 weeks |
| 4 | Engagement | Comments + Likes | 1–2 weeks |
| 5 | Discovery | Search + Tags + Pagination | 1–2 weeks |
| 6 | System Design | Caching + Jobs + Rate Limiting | 2–4 weeks |

---

## Phase 0 — Foundation: Python + Tools Setup

> Before writing any system code, you need your environment and mental model solid.

### Concepts to Learn

**Python (strengthen your basics)**
- Functions, return values, and scope
- Dictionaries and lists (you'll use these constantly)
- Classes and basic OOP (what is `self`? what is `__init__`?)
- Error handling: `try`, `except`, `raise`
- Modules and imports (`from x import y`)
- Virtual environments (what they are and why they matter)

**Tools**
- What is a terminal / command line?
- Git basics: `init`, `add`, `commit`, `push`, `pull`, branching
- What is an API? What is REST? What is HTTP?
- HTTP methods: `GET`, `POST`, `PUT`, `DELETE`
- What is JSON?
- What is a status code? (200, 201, 400, 404, 500)

### What to Google / Study
- `"Python OOP for beginners"`
- `"Python virtual environments explained"`
- `"What is a REST API explained simply"`
- `"HTTP methods explained GET POST PUT DELETE"`
- `"Git for beginners tutorial"`
- `"JSON explained for beginners"`

### Recommended Resources
- **Python OOP**: [realpython.com/python3-object-oriented-programming](https://realpython.com/python3-object-oriented-programming/)
- **Git**: [learngitbranching.js.org](https://learngitbranching.js.org/) (interactive)
- **REST APIs**: [restfulapi.net](https://restfulapi.net/)
- **HTTP status codes**: [httpstatuses.io](https://httpstatuses.io/)

### Build Checklist

- [ ] Python 3.11+ installed
- [ ] Can create and activate a virtual environment
- [ ] pip installed and working
- [ ] Git installed — can init a repo, commit, and push to GitHub
- [ ] Can explain what a GET request is vs a POST request
- [ ] Can explain what JSON is
- [ ] Can write a Python class with `__init__` and a method

### ✅ You're ready for Phase 1 when...
You can explain REST and HTTP to someone else in plain English, and your Git workflow is automatic.

---

## Phase 1 — Content System: Post CRUD + Data Flow

> Build the core of the system: create, read, update, and delete blog posts.
> **No database yet. No auth yet.** Just pure data flow.

### Concepts to Learn

**FastAPI**
- What is FastAPI and why use it?
- Decorators: what `@app.get()` and `@app.post()` mean
- Path parameters: `/posts/{id}`
- Query parameters: `/posts?page=1`
- Request body: how the client sends data to you
- Response model: how you control what data you send back
- Running a dev server: `uvicorn`

**Pydantic**
- What is data validation?
- Creating a Pydantic model (schema)
- The difference between input schema and output schema
- What happens when validation fails?

**Project Structure**
- What is a router? Why split routes into files?
- What is a service layer? Why separate it from routes?
- The difference between a route (what URL?) and a service (what logic?)

### What to Google / Study
- `"FastAPI tutorial official docs"`
- `"FastAPI path parameters vs query parameters"`
- `"Pydantic models tutorial"`
- `"FastAPI request body explained"`
- `"What is a service layer in web development"`
- `"Python type hints for beginners"`

### Recommended Resources
- **FastAPI official docs**: [fastapi.tiangolo.com](https://fastapi.tiangolo.com/) — start with the tutorial
- **Pydantic**: [docs.pydantic.dev](https://docs.pydantic.dev/)

### What to Build

Start with posts stored in a **Python list in memory** (no database yet).

```
POST   /posts          → Create a new post
GET    /posts          → Get all posts
GET    /posts/{id}     → Get one post by ID
PUT    /posts/{id}     → Update a post
DELETE /posts/{id}     → Delete a post
```

**Folder structure for this phase:**

```
/app
  /api
    posts.py       ← routes only
  /services
    post_service.py  ← logic only
  /schemas
    post.py        ← Pydantic models
  main.py
```

### Build Checklist

- [ ] FastAPI app running locally with `uvicorn`
- [ ] Can create a post via `POST /posts`
- [ ] Can retrieve all posts via `GET /posts`
- [ ] Can retrieve one post by ID via `GET /posts/{id}`
- [ ] Returns 404 if post not found
- [ ] Can update a post via `PUT /posts/{id}`
- [ ] Can delete a post via `DELETE /posts/{id}`
- [ ] Routes are in a separate file from main.py
- [ ] Business logic is in a service file, not the route
- [ ] Tested every endpoint using FastAPI's built-in `/docs` UI

### ✅ You're ready for Phase 2 when...
You can add a new field to a post (e.g., `published: bool`) without breaking anything, just by following the existing pattern.

---

## Phase 2 — Database Layer: SQL + SQLAlchemy

> Replace the in-memory list with a real database. This is the most important phase.

### Concepts to Learn

**SQL (the language)**
- What is a relational database?
- Tables, rows, and columns
- Primary keys and foreign keys
- Basic SQL: `SELECT`, `INSERT`, `UPDATE`, `DELETE`
- `WHERE` clause for filtering
- `JOIN` for combining tables
- `ORDER BY` and `LIMIT`
- Indexes: what they are and why they matter

**SQLAlchemy (the Python tool)**
- What is an ORM? Why use one?
- Defining a model (a Python class that maps to a table)
- Creating a session (how you talk to the database)
- CRUD operations with SQLAlchemy
- What is `Base.metadata.create_all()`?

**Alembic (database migrations)**
- What is a migration? Why not just delete and recreate tables?
- `alembic init`, `alembic revision`, `alembic upgrade`

**Repository Pattern**
- What is a repository layer?
- Why separate DB access from business logic?

### What to Google / Study
- `"SQL basics tutorial for beginners"`
- `"What is an ORM explained simply"`
- `"SQLAlchemy tutorial FastAPI"`
- `"Alembic migrations tutorial"`
- `"FastAPI SQLAlchemy full example"`
- `"Repository pattern explained Python"`
- `"Primary key vs foreign key explained"`

### Recommended Resources
- **SQLAlchemy + FastAPI**: [fastapi.tiangolo.com/tutorial/sql-databases](https://fastapi.tiangolo.com/tutorial/sql-databases/)
- **SQL basics**: [sqlbolt.com](https://sqlbolt.com/) (interactive, free)
- **Alembic**: [alembic.sqlalchemy.org/en/latest/tutorial.html](https://alembic.sqlalchemy.org/en/latest/tutorial.html)

### What to Build

Migrate your Phase 1 posts from an in-memory list to a **SQLite database** (simple, no server needed), then later swap to PostgreSQL.

**New folder additions:**

```
/app
  /models
    post.py        ← SQLAlchemy model
  /repositories
    post_repo.py   ← all DB queries live here
  /db
    database.py    ← DB connection setup
  /migrations      ← Alembic lives here
```

### Build Checklist

- [ ] Can explain what a primary key is
- [ ] Can write a basic SQL SELECT with a WHERE clause by hand
- [ ] SQLite database connected and working
- [ ] Posts table created via SQLAlchemy model
- [ ] All 5 CRUD endpoints now read/write from the database
- [ ] Repository layer handles all DB queries (services never import the DB directly)
- [ ] At least one Alembic migration created and applied
- [ ] Can add a new column to the posts table using a migration (not by deleting the DB)

### ✅ You're ready for Phase 3 when...
You can add a `users` table and link it to `posts` with a foreign key without being told how.

---

## Phase 3 — Auth System: JWT + Protected Routes

> Now that you understand the system, add identity and security.

### Concepts to Learn

**Authentication vs Authorization**
- Authentication = who are you? (login)
- Authorization = what are you allowed to do? (permissions)
- These are different things — never confuse them

**Password Security**
- Why you NEVER store plain-text passwords
- What is hashing? What is `bcrypt`?
- What is a salt?

**JWT (JSON Web Tokens)**
- What is a token-based auth system?
- Structure of a JWT: header, payload, signature
- Access tokens vs refresh tokens
- How the client stores and sends tokens (Authorization header)
- Token expiry

**FastAPI Auth Patterns**
- `OAuth2PasswordBearer`
- Dependency injection in FastAPI (`Depends`)
- How to protect a route

**Roles and Permissions**
- Role-based access control (RBAC)
- Admin vs author vs reader

### What to Google / Study
- `"JWT explained simply"`
- `"bcrypt password hashing Python"`
- `"FastAPI authentication tutorial JWT"`
- `"OAuth2PasswordBearer FastAPI example"`
- `"FastAPI Depends dependency injection explained"`
- `"RBAC role based access control explained"`
- `"What is a refresh token"`

### Recommended Resources
- **FastAPI auth official tutorial**: [fastapi.tiangolo.com/tutorial/security](https://fastapi.tiangolo.com/tutorial/security/)
- **JWT intro**: [jwt.io/introduction](https://jwt.io/introduction/)

### What to Build

```
POST  /auth/register   → Create a user account
POST  /auth/login      → Returns a JWT token
GET   /users/me        → Returns current user (protected)
```

Then protect your post routes:
- Anyone can `GET /posts` (public)
- Only logged-in users can `POST /posts` (authenticated)
- Only the post author can `PUT` or `DELETE` their own post (authorized)

### Build Checklist

- [ ] Can explain the difference between authentication and authorization
- [ ] Users table created with hashed passwords (never plain text)
- [ ] `POST /auth/register` creates a user
- [ ] `POST /auth/login` returns a valid JWT
- [ ] `GET /users/me` returns the logged-in user's profile
- [ ] Creating a post requires a valid JWT
- [ ] A user cannot delete another user's post (returns 403)
- [ ] Token expiry is set (e.g., 30 minutes)

### ✅ You're ready for Phase 4 when...
You can add a new protected route by copying the auth pattern without looking up how.

---

## Phase 4 — Engagement: Comments + Likes

> Add the social layer. This phase is mostly applying what you already know.

### Concepts to Learn

**Relational Data**
- One-to-many relationships (one post, many comments)
- Many-to-many relationships (users can like many posts; posts can be liked by many users)
- Join tables (e.g., `likes` table: `user_id` + `post_id`)
- Cascade deletes: what happens to comments when a post is deleted?

**API Design**
- Nested resource URLs: `/posts/{id}/comments`
- Idempotency: liking a post twice should not create two likes
- Toggle patterns: like = insert, unlike = delete

### What to Google / Study
- `"One to many relationship SQLAlchemy example"`
- `"Many to many relationship SQLAlchemy"`
- `"REST API nested resources best practice"`
- `"Cascade delete SQLAlchemy"`
- `"Idempotent API design explained"`

### What to Build

**Comments:**
```
POST   /posts/{id}/comments    → Add a comment
GET    /posts/{id}/comments    → Get all comments for a post
DELETE /comments/{id}          → Delete your own comment
```

**Likes:**
```
POST   /posts/{id}/like        → Like a post (toggle)
GET    /posts/{id}/likes       → Get like count
```

### Build Checklist

- [ ] Can explain one-to-many vs many-to-many with a real example
- [ ] Comments table created and linked to both `posts` and `users`
- [ ] Can add and retrieve comments for a post
- [ ] Deleting a post also deletes its comments (cascade)
- [ ] Likes table created as a join table
- [ ] Liking twice does not create duplicate rows (upsert or check first)
- [ ] Like count returned on post responses

### ✅ You're ready for Phase 5 when...
You can design a `bookmarks` table and its endpoints from scratch, without guidance.

---

## Phase 5 — Discovery: Search + Tags + Pagination

> Make the content findable.

### Concepts to Learn

**Pagination**
- Why you never return all rows from a database at once
- Offset-based pagination: `LIMIT` and `OFFSET` in SQL
- Page + page_size pattern
- Returning metadata: total count, current page, total pages

**Tags (Many-to-Many)**
- The `tags` table and the `post_tags` join table
- How to attach multiple tags to a post
- How to filter posts by tag

**Search**
- Basic SQL `LIKE` search: `WHERE title LIKE '%keyword%'`
- Why LIKE is slow on large datasets (and when that's fine)
- Introduction to full-text search concepts

### What to Google / Study
- `"Pagination REST API best practice"`
- `"SQLAlchemy limit offset pagination"`
- `"Many to many tags SQLAlchemy example"`
- `"SQL LIKE search tutorial"`
- `"FastAPI query parameters filtering"`

### What to Build

```
GET  /posts?page=1&page_size=10          → Paginated posts
GET  /posts?search=python                → Search posts by title/body
GET  /posts?tag=tutorial                 → Filter posts by tag
POST /posts/{id}/tags                    → Add tags to a post
GET  /tags                               → List all tags
```

### Build Checklist

- [ ] `GET /posts` never returns all posts — always paginated
- [ ] Response includes: `data`, `total`, `page`, `page_size`
- [ ] Tags table and post_tags join table created
- [ ] Posts can have multiple tags
- [ ] Can filter posts by tag via query parameter
- [ ] Can search posts by keyword in title or body
- [ ] All query params are optional (no param = default behaviour)

### ✅ You're ready for Phase 6 when...
Your API handles 100+ seeded posts and still responds cleanly with pagination.

---

## Phase 6 — System Design: Caching + Jobs + Rate Limiting

> This is where you cross from beginner/junior into mid-level thinking.

### Concepts to Learn

**Caching (Redis)**
- What is caching and why does it matter?
- What is Redis?
- Cache-aside pattern: check cache → if miss, hit DB → store in cache
- Cache invalidation: when to clear the cache
- TTL (time to live)

**Background Jobs**
- What is a background job? When do you need one?
- Examples: sending a welcome email, generating a thumbnail, sending notifications
- FastAPI `BackgroundTasks` (simple)
- Celery + Redis (production-grade)

**Rate Limiting**
- What is rate limiting and why does it matter?
- Protecting your API from abuse
- `slowapi` library for FastAPI

**Logging & Monitoring**
- Structured logging (JSON logs)
- Log levels: DEBUG, INFO, WARNING, ERROR
- What to log and what not to log (never log passwords or tokens)

### What to Google / Study
- `"Redis caching explained simply"`
- `"Cache-aside pattern explained"`
- `"FastAPI BackgroundTasks tutorial"`
- `"Celery Redis FastAPI tutorial"`
- `"Rate limiting FastAPI slowapi"`
- `"Python logging tutorial structured"`
- `"What is cache invalidation"`

### Recommended Resources
- **Redis intro**: [redis.io/docs/get-started](https://redis.io/docs/get-started/)
- **Celery**: [docs.celeryq.dev/en/stable/getting-started/introduction.html](https://docs.celeryq.dev/en/stable/getting-started/introduction.html)
- **slowapi**: [github.com/laurentS/slowapi](https://github.com/laurentS/slowapi)

### What to Build

- [ ] Cache `GET /posts` responses in Redis (TTL: 60 seconds)
- [ ] Invalidate cache when a post is created or updated
- [ ] Send a (fake) welcome email in the background on register
- [ ] Rate limit `POST /auth/login` to 5 requests per minute
- [ ] Add structured logging to all routes (request method, path, status, duration)

### Build Checklist

- [ ] Can explain what a cache hit and cache miss are
- [ ] Redis installed and connected
- [ ] At least one endpoint reads from cache before hitting DB
- [ ] Background task runs after register (does not block the response)
- [ ] Login endpoint is rate limited
- [ ] Logs write to file with timestamp, level, and message
- [ ] No sensitive data appears in logs

### ✅ You're done with the build plan when...
You can describe every layer of your system — from a client request hitting your API all the way to the database and back — without looking at any notes.

---

## Master Progress Tracker

```
Phase 0 — Foundation          [ ] Complete
Phase 1 — Content System      [ ] Complete
Phase 2 — Database Layer      [ ] Complete
Phase 3 — Auth System         [ ] Complete
Phase 4 — Engagement          [ ] Complete
Phase 5 — Discovery           [ ] Complete
Phase 6 — System Design       [ ] Complete
```

---

## Golden Rules for This Journey

1. **Never copy-paste code you don't understand.** Type it. Break it. Fix it.
2. **Read error messages carefully.** They almost always tell you exactly what's wrong.
3. **Build first, optimise later.** Make it work, then make it clean.
4. **Commit to Git at the end of every phase.** Your future self will thank you.
5. **If you're stuck for more than 30 minutes, Google the exact error message.**
6. **You don't need to know everything before you start.** Learn what the next step requires.
