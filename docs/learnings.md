# Learnings - Monolithic App Rebuild

## Phase 1: SQLAlchemy Models & Database

### SQLAlchemy ORM Fundamentals
- **Modern SQLAlchemy 2.0 syntax**: Using `Mapped[T]` and `mapped_column()` instead of legacy Column syntax
- **Declarative Base**: All models inherit from [Base(DeclarativeBase)](cci:2://file:///c:/VS%20CODE/VSCODE/Projects/monolithic-app-rebuild/src/models/user.py:4:0-5:8) - this is SQLAlchemy's entry point
- **Table naming conventions**: Using plural names like `"users"` vs singular `"user"`

### Database Design Principles
- **Constraints ensure data integrity**: `unique=True`, `nullable=False` prevent bad data at database level
- **Database-generated timestamps**: `server_default=func.now()` runs in database, not Python

### Database Connection Setup

**🔹 SQLAlchemy Engine**
- **What it does**: Creates database connection and manages communication
- **Connection URL**: `"sqlite:///blog.db"` creates SQLite file
- **Echo=True**: Shows SQL in console (great for debugging!)
- **Behind the scenes**: Manages dialect + connection pool + DBAPI automatically

**🔹 Session Factory Pattern**
- **What it does**: Creates database sessions for operations
- **sessionmaker()**: Factory that makes Session objects
- **bind=engine**: Connects sessions to your database
- **expire_on_commit=False**: Objects stay accessible after commit

**🔹 How They Work Together**
```
Your Code → SessionLocal() → Session → Engine → Database
           (sessionmaker)   (ORM)    (Connection)
```

**🔹 Real Usage Pattern**
```python
# Get a session from factory
session = SessionLocal()
try:
    # Use session for database operations
    user = session.query(User).first()
    session.commit()
finally:
    # Always close session
    session.close()
```

### Production Best Practices
- **Single source of truth**: Database handles timestamps, prevents clock drift between servers
- **Timezone awareness**: Always use `DateTime(timezone=True)` for consistent timestamps
- **String length limits**: `String(255)` for emails - RFC compliant and prevents abuse

### Database Indexing Simplified

**🔹 Unique Constraints (`unique=True`)**
- **What it does**: Prevents duplicate values in a column
- **Bonus benefit**: Automatically creates an index for fast lookups
- **When to use**: Fields that must be unique (email, session_token, user_id in credentials)
- **Example**: No two users can have the same email address

**🔹 Indexes (`index=True`)**
- **What it does**: Makes searches faster on frequently queried fields
- **No constraints**: Allows duplicate values
- **When to use**: Non-unique fields you search often
- **Example**: Fast lookups on user_id in sessions table

**🔹 Key Rule**
- If `unique=True` → You get an index automatically
- If not unique → Add `index=True` for performance
- Don't use both together - it's redundant!

### Engineering Decisions Made
- **Why server_default > default**: Database timestamps work across multiple servers/timezones
- **Audit trail value**: `created_at` enables analytics, security investigations, user support
- **Type annotations**: `Mapped[int]` gives IDE support and catches bugs early

### Database Relationships & Constraints
**🔹 One-to-One Relationships (User ↔ Credential)**
- **What it means**: Each user has exactly one credential
- **How it works**: `unique=True` on foreign key prevents multiple credentials per user
- **Example**: User can only have one password

**🔹 One-to-Many Relationships (User → Sessions)**
- **What it means**: One user can have multiple sessions
- **How it works**: No unique constraint on foreign key allows multiple sessions
- **Example**: User can be logged in on phone, laptop, tablet

**🔹 Foreign Key Constraints**
- **What they do**: Link tables together at database level
- **How they work**: `ForeignKey("users.id")` connects sessions to users
- **Why important**: Prevents orphaned records (session without user)

**🔹 Relationship Navigation**
- **What it does**: `back_populates` lets you navigate both ways
- **Example**: `user.sessions` and `session.user` both work
- **Benefit**: Easy to access related data

### Database Constraint Enforcement
- **Database-Level vs Application-Level**: `unique=True` prevents duplicates even with race conditions
- **Unique Constraint Benefits**: Prevents multiple credentials per user, creates automatic index
- **Referential Integrity**: Foreign keys prevent orphaned records (credential without user)
- **Atomic Operations**: Database constraints can't be bypassed by application bugs

### SQLAlchemy Relationship Patterns
- **Relationship Definition**: `relationship("ModelName", back_populates="field_name")`
- **Type Annotations**: `Mapped["Credential"]` enables IDE support and type checking
- **Bidirectional Navigation**: `user.credential` and `credential.user` both work
- **Collection vs Single Object**: One-to-many returns list, one-to-one returns single object

### Security & Data Design
- **Password Hash Storage**: `String(255)` for bcrypt hashes, never plain passwords
- **Session Token Requirements**: Need unique, indexed tokens for authentication
- **Audit Trail Continuation**: All models have `created_at` for tracking
- **Constraint-Driven Design**: Let database enforce business rules, not just application

## Key Engineering Insights

**Why This Matters:**
- **Data Integrity**: Constraints prevent invalid data even if application code has bugs
- **Performance**: Proper indexing makes authentication queries fast
- **Security**: Database-level enforcement prevents security bypasses
- **Maintainability**: Clear relationships make code predictable and testable

**🔹 Real-World Impact**
- **Without indexes**: Database scans entire table (slow)
- **With indexes**: Database jumps directly to matching rows (fast)
- **Unique constraints**: Prevent data corruption and speed up lookups