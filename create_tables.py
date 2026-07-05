from database import engine, Base

# Import all models so SQLAlchemy knows about them
from models import User, Product, Cart, Wishlist, Order

print("Creating tables...")

Base.metadata.create_all(bind=engine)

print("✅ Tables created successfully!")