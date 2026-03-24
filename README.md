# Monolithic App Rebuild

## 🎯 Purpose

**This is a learning project - an independent rebuild to reinforce core software engineering concepts.**

This project is designed as a hands-on learning experience to understand and practice building production-aligned web applications without unnecessary complexity. It represents a deliberate reconstruction of fundamental patterns and architectures to solidify understanding through practical implementation.

## 🏗️ What We're Building

A minimal but production-ready monolithic web application with:
- User authentication system
- Clean separation of concerns
- Testable business logic
- Modern Python web stack

## 🛠️ Technology Stack

- **Backend**: FastAPI
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Custom session-based auth
- **Security**: bcrypt for password hashing
- **Testing**: pytest
- **Database Migrations**: Alembic
- **Deployment**: uvicorn

## 📁 Project Structure

```
src/
├── models/           # Database models (SQLAlchemy)
├── services/         # Business logic (testable without framework)
├── api/             # FastAPI endpoints
├── security/        # Password hashing, session management
└── database/        # Database connection & migrations
```

## 🎓 Learning Goals

This project focuses on mastering these core concepts:

1. **Clean Architecture** - Understanding proper separation of concerns
2. **Testable Design** - Writing business logic that's easy to test
3. **Database Design** - Working with ORMs and migrations
4. **API Development** - Building RESTful endpoints
5. **Security Fundamentals** - Implementing authentication safely
6. **Production Thinking** - Building maintainable, scalable code

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Virtual environment (recommended)

### Installation

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   alembic upgrade head
   ```

5. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

### Running Tests

```bash
pytest tests/
```

## 📚 Documentation

- [Minimal Architecture Plan](docs/minimal_architecture_plan.md) - Detailed design decisions and rationale
- [Three Level Context Model](docs/Three_Level_Context_Model_Template.md) - Context mapping framework
- [Learnings](docs/learnings.md) - Key insights and discoveries

## 🎯 Core Philosophy

**Build the simplest thing that works, but make it production-ready.**

- Fewer layers, more direct value
- Abstractions only when they solve real problems
- Learning-focused, not enterprise-focused
- Add complexity only when needed

## 📋 Current Status

This is an active learning project. The implementation follows a phased approach:

- ✅ **Phase 1**: Core Models & Database
- 🔄 **Phase 2**: Business Logic
- ⏳ **Phase 3**: API Layer
- ⏳ **Phase 4**: Integration & Polish

## 🤝 Contributing

This is primarily a personal learning project, but insights and suggestions are welcome! The focus is on understanding and reinforcing fundamental concepts rather than building a production system for external use.

## 📄 License

This project is for educational purposes. Feel free to use it for learning, but it's not intended for production deployment without significant enhancements.

---

**Remember**: The goal is learning, not perfection. Every line of code should reinforce understanding of core software engineering principles.
