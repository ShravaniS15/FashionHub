from sqlalchemy.orm import Session
from passlib.context import CryptContext
from models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ==========================
# PASSWORD SECURITY
# ==========================

def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# ==========================
# USER QUERIES
# ==========================

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


# ==========================
# REGISTER
# ==========================

def register_user(db: Session, fullname, email, password, phone="", address=""):

    email = email.lower().strip()

    existing = get_user_by_email(db, email)
    if existing:
        return False, "Email already exists"

    if len(password) < 6:
        return False, "Password must be at least 6 characters"

    user = User(
        fullname=fullname.strip(),
        email=email,
        password=hash_password(password),
        phone=phone,
        address=address
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return True, user


# ==========================
# LOGIN
# ==========================

def login_user(db: Session, email, password):

    email = email.lower().strip()

    user = get_user_by_email(db, email)

    if user is None:
        return False, "User not found"

    if not verify_password(password, user.password):
        return False, "Incorrect password"

    return True, user