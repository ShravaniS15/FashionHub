from sqlalchemy.orm import Session
from models import User, Product, Cart, Wishlist, Order
from models import Order, OrderItem, Cart

# =====================================================
# PRODUCT CRUD
# =====================================================

# Add Product
def add_product(db: Session, **product_data):
    product = Product(**product_data)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


# Get All Products
def get_products(db: Session):
    return db.query(Product).all()


# Get Product by ID
def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


# Update Product
def update_product(db: Session, product_id: int, **updated_data):
    product = get_product_by_id(db, product_id)

    if not product:
        return None

    for key, value in updated_data.items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)
    return product


# Delete Product
def delete_product(db: Session, product_id: int):
    product = get_product_by_id(db, product_id)

    if product:
        db.delete(product)
        db.commit()
        return True

    return False

# =====================================================
# PRODUCTS BY CATEGORY
# =====================================================

def get_products_by_category(db: Session, category: str):
    return db.query(Product).filter(Product.category == category).all()


def get_new_arrivals(db: Session):
    return db.query(Product).order_by(Product.id.desc()).limit(12).all()


def get_sale_products(db: Session):
    return db.query(Product).filter(Product.rating >= 4).all()

# =====================================================
# USER CRUD
# =====================================================

def get_all_users(db: Session):
    return db.query(User).all()


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)

    if user:
        db.delete(user)
        db.commit()
        return True

    return False


# =====================================================
# CART CRUD
# =====================================================

def add_to_cart(db: Session, user_id: int, product_id: int, quantity=1):

    existing = db.query(Cart).filter(
        Cart.user_id == user_id,
        Cart.product_id == product_id
    ).first()

    if existing:
        existing.quantity += quantity
        db.commit()
        return existing

    cart = Cart(
        user_id=user_id,
        product_id=product_id,
        quantity=quantity
    )

    db.add(cart)
    db.commit()
    db.refresh(cart)

    return cart


def get_cart_items(db: Session, user_id: int):
    return db.query(Cart).filter(
        Cart.user_id == user_id
    ).all()

def update_cart_quantity(db: Session, cart_id: int, quantity: int):

    item = db.query(Cart).filter(
        Cart.id == cart_id
    ).first()

    if item:
        item.quantity = quantity
        db.commit()
        db.refresh(item)

    return item

def remove_from_cart(db: Session, cart_id: int):

    item = db.query(Cart).filter(
        Cart.id == cart_id
    ).first()

    if item:
        db.delete(item)
        db.commit()
        return True

    return False


def clear_cart(db: Session, user_id: int):

    db.query(Cart).filter(
        Cart.user_id == user_id
    ).delete(synchronize_session=False)

    db.commit()


# =====================================================
# WISHLIST CRUD
# =====================================================

def add_to_wishlist(db: Session, user_id: int, product_id: int):

    exists = db.query(Wishlist).filter(
        Wishlist.user_id == user_id,
        Wishlist.product_id == product_id
    ).first()

    if exists:
        return exists

    wish = Wishlist(
        user_id=user_id,
        product_id=product_id
    )

    db.add(wish)
    db.commit()
    db.refresh(wish)

    return wish


def get_wishlist(db: Session, user_id: int):

    return db.query(Wishlist).filter(
        Wishlist.user_id == user_id
    ).all()


def remove_from_wishlist(db: Session, wishlist_id: int):

    item = db.query(Wishlist).filter(
        Wishlist.id == wishlist_id
    ).first()

    if item:
        db.delete(item)
        db.commit()
        return True

    return False


# =====================================================
# ORDER CRUD
# =====================================================


def place_order(
    db,
    user_id,
    total,
    payment_method,
    address,
    city,
    state,
    pincode,
    phone
):

    # Create order
    order = Order(
        user_id=user_id,
        total=total,
        payment_method=payment_method,
        address=address,
        city=city,
        state=state,
        pincode=pincode,
        phone=phone,
        status="Placed"
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    # Get cart items
    cart_items = db.query(Cart).filter(Cart.user_id == user_id).all()

    # Save each item into order_items
    for item in cart_items:
        order_item = OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.product.price
        )
        db.add(order_item)

    db.commit()

    return order


def get_orders(db: Session, user_id: int):

    return db.query(Order).filter(
        Order.user_id == user_id
    ).all()


def update_order_status(
    db: Session,
    order_id: int,
    status: str
):

    order = db.query(Order).filter(
        Order.id == order_id
    ).first()

    if not order:
        return None

    order.status = status

    db.commit()
    db.refresh(order)

    return order