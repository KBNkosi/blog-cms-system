# Blog CMS System

## 🎯 Purpose

This project is a deliberate implementation of a backend system designed to reinforce
core software engineering concepts through practical application.

The goal is to build a production-aligned blog platform from first principles, focusing on:
- clear system structure
- separation of concerns
- maintainable architecture
- incremental system design

Rather than building features in isolation, this project approaches development as a system,
where each component fits into a broader architecture.

---

## 📋 Project Overview

A **backend-focused blog platform** built using a **modular monolith architecture**.

The system is designed to simulate how real-world applications evolve — starting with a
core domain and progressively expanding into additional subsystems such as authentication,
engagement, and discovery.

Development follows a **phase-based approach**, ensuring each layer is implemented with
clarity before introducing additional complexity.

---

## 📋 Project Overview

A **backend-focused blog platform** built using a **modular monolith architecture**.

The system is designed to simulate how real-world applications evolve — starting with a
core domain and progressively expanding into additional subsystems such as authentication,
engagement, and discovery.

Development follows a **phase-based approach**, ensuring each layer is implemented with
clarity before introducing additional complexity.

---
## 🚧 Current Status

**Phase:** Content System (Phase 1)  
**Status:** In Progress  

### Current Focus
- Implementing data persistence using SQLAlchemy
- Structuring repository layer for database access
- Ensuring consistency between schemas, services, and models

This phase focuses on making the system fully data-driven before introducing authentication.

---

## 🏗️ Architecture
### Architecture Style: Modular Monolith

The system is structured as a modular monolith — internally organized into clear domains
and layers, while deployed as a single unit.

This approach:
- avoids premature complexity of microservices
- maintains clean separation between components
- allows future scalability without over-engineering early

### System Design
```
Client → API Route → Service Layer → Repository → Database
                          ↓
                    Business Logic
```
| Layer | Responsibility |
|------|----------------|
| **API Layer** | Handles HTTP requests and routing |
| **Service Layer** | Contains business logic and rules |
| **Repository Layer** | Manages data access and persistence |
| **Database Layer** | Stores application data |

Each layer is isolated to ensure maintainability and testability.

### Project Structure
```
/app
  /api              → Routes (controllers)
  /services         → Business logic
  /models           → Database models
  /schemas          → Request/response validation
  /database         → Database configuration & migrations
  /main.py          → Application entry point
/docs               → Project documentation
/tests              → Test suite
```

## 🧠 Key Design Decisions

### Why Modular Monolith?
- Keeps deployment simple while maintaining internal structure
- Avoids early complexity of distributed systems
- Enables gradual evolution into more complex architectures if needed

---

### Why Start with Content Instead of Authentication?
- Content is the core business domain of the system
- Allows validation of data flow and architecture before adding security layers
- Prevents over-engineering authentication too early

---

### Why Service + Repository Pattern?
- Separates business logic from data access
- Improves testability and maintainability
- Prevents tightly coupled code as the system grows

---


### Core Domains
| Domain | Status | Responsibilities |
|--------|--------|-----------------|
| **Content** | ✅ Active | Posts, CRUD operations, validation |
| **Auth** | 🔄 Phase 2 | Users, JWT tokens, permissions |
| **Engagement** | ⏳ Phase 3 | Comments, likes, bookmarks |
| **Discovery** | ⏳ Phase 4 | Search, tags, categories, feed |
| **System** | ⏳ Phase 5 | Caching, logging, monitoring |

---

## 🛠️ Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Framework** | FastAPI | High-performance API framework |
| **Validation** | Pydantic | Data validation and serialization |
| **Database** | SQLite → PostgreSQL | Data persistence (development → production) |
| **ORM** | SQLAlchemy | Database abstraction layer |
| **Migrations** | Alembic | Database version control |
| **Testing** | Pytest | Automated testing framework |

---

## 🚀 Features

### ✅ Implemented (Phase 1)
- **Post Management**  
- Post CRUD operations
- Request validation using Pydantic
- Structured API responses
- Error handling with proper HTTP status codes
- API documentation via FastAPI

### 🔄 In Progress
- **Data Persistence**
- Database models and persistence layer
- Repository implementation
- Migration setup (Alembic)

### ⏳ Planned 
- Authentication system (JWT, role-based access)
- Comments and engagement features
- Search and tagging system
- Caching and performance optimization
- Background jobs and monitoring
---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Virtual environment (recommended)

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd blog-cms-system

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Application
```bash
# Start the development server
uvicorn app.main:app --reload

# Access the API
# Swagger UI: http://localhost:8000/docs
# ReDoc: http://localhost:8000/redoc
```

### Database Setup
```bash
# Run database migrations
alembic upgrade head
```

---

## 📚 API Documentation

### Current Endpoints

#### Posts
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/posts` | Create a new post |
| `GET` | `/posts` | Get all posts |
| `GET` | `/posts/{id}` | Get single post |
| `PUT` | `/posts/{id}` | Update post |
| `DELETE` | `/posts/{id}` | Delete post |

### Request/Response Models

#### PostCreate
```python
{
    "title": "string (1-200 chars)",
    "content": "string (1-5000 chars)"
}
```

#### PostResponse
```python
{
    "id": 1,
    "title": "string",
    "content": "string",
    "author_id": 1,
    "created_at": "2024-01-15T10:30:00",
    "updated_at": null
}
```

---

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test file
pytest tests/test_posts.py
```

---

## 📈 Development Phases

### Phase 1: Content System ✅
- [x] Post CRUD operations
- [x] Schema validation
- [x] Error handling
- [x] API documentation

### Phase 2: Authentication 🔄
- [ ] User models
- [ ] JWT implementation
- [ ] Protected routes
- [ ] Role management

### Phase 3: Engagement ⏳
- [ ] Comments system
- [ ] Like functionality
- [ ] User interactions

### Phase 4: Discovery ⏳
- [ ] Search implementation
- [ ] Tag system
- [ ] Content feed

### Phase 5: Production ⏳
- [ ] Caching layer
- [ ] Rate limiting
- [ ] Monitoring

---

## 🤝 Contributing

This is a learning project. Feel free to:
- Study the code structure
- Suggest improvements
- Report issues
- Ask questions about architecture decisions

---

## 📝 Learning Outcomes

**Key Concepts Practiced:**
- Clean architecture patterns
- RESTful API design
- Data validation with Pydantic
- Database migrations with Alembic
- Error handling strategies
- Separation of concerns
- Type safety in Python

---

## 🔮 Future Considerations

- **Microservices Migration:** How to split a monolith into services
  

## 📄 License

This project is for educational purposes. Feel free to use and modify for learning.

---

