from sqlalchemy.orm import Session
from app.models.db_user import UserDB
from app.security import hash_password

def create_user(db: Session, username: str, password: str):
    # ✅ CHECK IF USER EXISTS
    existing_user = db.query(UserDB).filter(UserDB.username == username).first()
    if existing_user:
        return None

    user = UserDB(
        username=username,
        hashed_password=hash_password(password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(UserDB).filter(UserDB.username == username).first()
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user
