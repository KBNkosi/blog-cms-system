from src.database.connection import SessionLocal
from src.models.user import User, Credential, Session
from datetime import datetime, timedelta

def get_session():
    return SessionLocal()

# Test user creation
def test_user_creation():
    session = get_session()
    try:
        user= User(email="test@example.com")
        session.add(user)
        session.commit()
        print(f"User created with ID: {user.id}")
        return user
    except Exception as e:
        print(f"Error creating user: {e}")
        session.rollback()
        return None
    finally:
        session.close()