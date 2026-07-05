import streamlit as st

# ======================================================
# WEBSITE CONFIGURATION
# ======================================================

APP_NAME = "FashionHub Store"
APP_ICON = "🛍️"
APP_LAYOUT = "wide"

# ======================================================
# COMPANY DETAILS
# ======================================================

COMPANY_NAME = "FashionHub"
COMPANY_EMAIL = "support@fashionhub.com"
COMPANY_PHONE = "+91 9876543210"

# ======================================================
# CURRENCY
# ======================================================

CURRENCY = "₹"

# ======================================================
# DEFAULT USER PROFILE IMAGE
# ======================================================

DEFAULT_PROFILE_IMAGE = "assets/default_profile.png"

# ======================================================
# DEFAULT PRODUCT IMAGE
# ======================================================

DEFAULT_PRODUCT_IMAGE = "assets/no_image.png"

# ======================================================
# CATEGORIES
# ======================================================

CATEGORIES = [
    "Men",
    "Women",
    "Kids",
    "Footwear",
    "Accessories",
    "Summer",
    "Winter",
    "New Arrivals",
    "Sale"
]

# ======================================================
# PAYMENT METHODS
# ======================================================

PAYMENT_METHODS = [
    "Cash on Delivery",
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking"
]

# ======================================================
# ORDER STATUS
# ======================================================

ORDER_STATUS = [
    "Pending",
    "Processing",
    "Shipped",
    "Delivered",
    "Cancelled"
]

# ======================================================
# ADMIN EMAIL
# ======================================================

ADMIN_EMAIL = "admin@fashionhub.com"

# ======================================================
# SESSION STATE INITIALIZATION
# ======================================================

def initialize_session():
    """
    Initialize Streamlit session variables.
    """

    defaults = {
        "logged_in": False,
        "user_id": None,
        "user_name": "",
        "user_email": "",
        "cart_count": 0,
        "wishlist_count": 0,
        "is_admin": False
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value