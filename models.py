from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey,
    DateTime,
    Text
)

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from database import Base

# =====================================================
# USERS
# =====================================================

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    fullname = Column(String(100), nullable=False)

    email = Column(String(100), unique=True, nullable=False)

    password = Column(String(255), nullable=False)

    phone = Column(String(20))

    address = Column(Text)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    cart_items = relationship(
        "Cart",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    wishlist_items = relationship(
        "Wishlist",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    orders = relationship(
        "Order",
        back_populates="user",
        cascade="all, delete-orphan"
    )


# =====================================================
# PRODUCTS
# =====================================================

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(150), nullable=False)

    description = Column(Text)

    category = Column(String(50))

    brand = Column(String(50))

    price = Column(Float)

    stock = Column(Integer)

    rating = Column(Float)

    image = Column(String(255))

    cart_items = relationship(
        "Cart",
        back_populates="product",
        cascade="all, delete-orphan"
    )

    wishlist_items = relationship(
        "Wishlist",
        back_populates="product",
        cascade="all, delete-orphan"
    )


# =====================================================
# CART
# =====================================================

class Cart(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    product_id = Column(
        Integer,
        ForeignKey("products.id")
    )

    quantity = Column(Integer, default=1)

    user = relationship(
        "User",
        back_populates="cart_items"
    )

    product = relationship(
        "Product",
        back_populates="cart_items"
    )


# =====================================================
# WISHLIST
# =====================================================

class Wishlist(Base):
    __tablename__ = "wishlist"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    product_id = Column(
        Integer,
        ForeignKey("products.id")
    )

    user = relationship(
        "User",
        back_populates="wishlist_items"
    )

    product = relationship(
        "Product",
        back_populates="wishlist_items"
    )


# =====================================================
# ORDERS
# =====================================================

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    total = Column(Float)

    payment_method = Column(String(50))

    address = Column(Text)

    city = Column(String(100))

    state = Column(String(100))

    pincode = Column(String(10))

    phone = Column(String(20))

    status = Column(String(50), default="Pending")

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    user = relationship(
        "User",
        back_populates="orders"
        
    )
    items = relationship("OrderItem", cascade="all, delete-orphan")

class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)

    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))

    quantity = Column(Integer)
    price = Column(Float)

    order = relationship("Order")
    product = relationship("Product")