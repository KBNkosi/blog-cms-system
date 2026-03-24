from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import mapped_column,Mapped, DeclarativeBase, relationship


# declarative base class
class Base(DeclarativeBase):
    pass



class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now() )
    credential: Mapped["Credential"] = relationship(back_populates = "user")
    sessions: Mapped[list["Session"]] = relationship(back_populates="user")

class Credential(Base):
    __tablename__ = "credentials"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)
    user: Mapped["User"] = relationship(back_populates="credential")

class Session(Base):
    __tablename__ ="sessions"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    session_token: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    expires_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True))
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    user: Mapped["User"] = relationship(back_populates="sessions")
    

    