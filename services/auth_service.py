from sqlalchemy.orm import Session
from models import User
import bcrypt

# ==========================
# PASSWORD HELPERS
# ==========================

def hash_password(password: str):
    return bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")


def verify_password(plain: str, hashed: str):
    return bcrypt.checkpw(
        plain.encode("utf-8"),
        hashed.encode("utf-8")
    )

# ==========================
# USER LOOKUP
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

    if get_user_by_email(db, email):
        return False, "Email already exists", None

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

    return True, "Account created successfully", user

# ==========================
# LOGIN
# ==========================

def login_user(db: Session, email, password):

    email = email.lower().strip()

    user = get_user_by_email(db, email)

    if not user:
        return False, "User not found", None

    if not verify_password(password, user.password):
        return False, "Incorrect password", None

    return True, "Login successful", user