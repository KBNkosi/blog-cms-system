# Monolithic App Rebuild

## 🎯 Purpose

**This is a learning project - an independent rebuild to reinforce core software engineering concepts.**

This project is designed as a hands-on learning experience to understand and practice building production-aligned web applications without unnecessary complexity. It represents a deliberate reconstruction of fundamental patterns and architectures to solidify understanding through practical implementation.

---

## 📋 Project Overview

A **modular monolith** blog application built with FastAPI, demonstrating clean architecture patterns and separation of concerns. The project follows a phase-based development approach, starting with core functionality and progressively adding complexity.

### Current Phase: 🚀 Phase 1 - Content System

**Status:** In Progress  
**Focus:** Core post management with proper validation and API design

---

## 🏗️ Architecture

### System Design
```
Client → API Route → Service Layer → Repository → Database
                          ↓
                    Business Logic
```

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
  - Create posts with validation
  - Retrieve all posts (list view)
  - Get single post by ID
  - Update posts (partial updates)
  - Delete posts
  - Proper error handling (404, validation)
  - Response models for API consistency

### 🔄 In Progress
- **Data Persistence**
  - Database models setup
  - Migration scripts
  - Repository layer implementation

### ⏳ Planned (Future Phases)
- **Authentication System**
  - User registration/login
  - JWT token management
  - Role-based access control
- **Engagement Features**
  - Comments system
  - Like/unlike functionality
  - User bookmarks
- **Discovery & Search**
  - Tag system
  - Full-text search
  - Content feed
- **Production Features**
  - Caching layer
  - Rate limiting
  - Background jobs

---

## 📁 Key Design Principles

### 1. **Separation of Concerns**
- Routes handle HTTP concerns only
- Services contain business logic
- Repositories manage data access

### 2. **Schema-Driven Development**
- Input validation with Pydantic schemas
- Clear separation between input/output models
- Type safety throughout the application

### 3. **Iterative Complexity**
- Start with core functionality
- Add features incrementally
- Maintain clean architecture at each phase

### 4. **Error-First Design**
- Explicit error handling
- Proper HTTP status codes
- Consistent error responses

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Virtual environment (recommended)

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd monolithic-app-rebuild

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

**Architecture Patterns:**
- Modular monolith design
- Repository pattern
- Service layer pattern
- Schema-driven development

---

## 📄 License

This project is for educational purposes. Feel free to use and modify for learning.

---

## 🔮 Future Considerations

- **Microservices Migration:** How to split monolith into services
- **Performance Optimization:** Caching strategies, query optimization
- **Security Enhancements:** Input validation, authentication patterns
- **Scalability Patterns:** Horizontal scaling, load balancing
- **Monitoring:** Logging, metrics, health checks

---

*Built with ❤️ for learning clean software engineering practices*
