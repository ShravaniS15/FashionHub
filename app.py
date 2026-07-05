import streamlit as st
from streamlit_option_menu import option_menu

from database import SessionLocal
from crud import get_products

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="FashionHub Store",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Database Connection
db = SessionLocal()

# Load Products
products = get_products(db)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.main{
    background-color:#F8F9FA;
}

.title{
    text-align:center;
    color:#E91E63;
    font-size:50px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:gray;
    font-size:20px;
}

.product-card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 5px 15px rgba(0,0,0,0.1);
    text-align:center;
}

.footer{
    text-align:center;
    color:gray;
    padding:30px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.image(
        "https://img.icons8.com/color/96/shopping-bag.png",
        width=90
    )

    st.title("FashionHub")

    selected = option_menu(
        "Navigation",
        [
            "Home",
            "Men",
            "Women",
            "Kids",
            "Footwear",
            "Accessories",
            "Summer",
            "Winter",
            "New Arrivals",
            "Sale",
            "Wishlist",
            "Cart",
            "Orders",
            "Profile",
            "Login",
            "Signup"
        ],
        icons=[
            "house",
            "person",
            "person",
            "emoji-smile",
            "bootstrap",
            "handbag",
            "sun",
            "snow",
            "stars",
            "tags",
            "heart",
            "cart",
            "box",
            "person-circle",
            "box-arrow-in-right",
            "person-plus"
        ],
        default_index=0
    )

# -----------------------------
# Header
# -----------------------------
st.markdown("<h1 class='title'>🛍 FashionHub Store</h1>", unsafe_allow_html=True)

st.markdown(
    "<p class='subtitle'>Your One Stop Fashion Destination</p>",
    unsafe_allow_html=True
)

# -----------------------------
# Search
# -----------------------------
search = st.text_input(
    "🔍 Search Products"
)

# -----------------------------
# Hero Banner
# -----------------------------
st.image(
    "https://images.unsplash.com/photo-1441986300917-64674bd600d8",
    use_container_width=True
)

# -----------------------------
# Categories
# -----------------------------
st.subheader("🛒 Shop by Category")

col1,col2,col3,col4=st.columns(4)

with col1:
    st.info("👔 Men")

with col2:
    st.info("👗 Women")

with col3:
    st.info("🧒 Kids")

with col4:
    st.info("👟 Footwear")

# -----------------------------
# Featured Collection
# -----------------------------
st.subheader("🔥 Featured Collection")

c1,c2,c3=st.columns(3)

with c1:
    st.image(
        "https://images.unsplash.com/photo-1521572267360-ee0c2909d518",
        use_container_width=True
    )
    st.write("Summer Collection")

with c2:
    st.image(
        "https://images.unsplash.com/photo-1542291026-7eec264c27ff",
        use_container_width=True
    )
    st.write("Trending Sneakers")

with c3:
    st.image(
        "https://images.unsplash.com/photo-1512436991641-6745cdb1723f",
        use_container_width=True
    )
    st.write("Women's Fashion")

# -----------------------------
# Why Choose Us
# -----------------------------
st.subheader("⭐ Why Choose FashionHub?")

a,b,c=st.columns(3)

a.success("🚚 Free Shipping")

b.success("💳 Secure Payments")

c.success("🔄 Easy Returns")

# -----------------------------
# Newsletter
# -----------------------------
st.subheader("📧 Subscribe")

email = st.text_input("Enter your Email")

if st.button("Subscribe"):
    st.success("Thanks for subscribing!")

# -----------------------------
# Footer
# -----------------------------
st.markdown(
"""
<div class='footer'>


© 2026 FashionHub Store

</div>
""",
unsafe_allow_html=True
)