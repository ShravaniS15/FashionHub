from sqlalchemy.orm import Session
from models import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ==========================
# PASSWORD HELPERS
# ==========================
def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str):
    return pwd_context.verify(plain, hashed)


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