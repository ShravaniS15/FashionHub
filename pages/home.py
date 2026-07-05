import streamlit as st
from database import SessionLocal
from crud import get_products

st.set_page_config(
    page_title="FashionHub Store",
    page_icon="🛍️",
    layout="wide"
)

# Database Connection
db = SessionLocal()

# Fetch all products
products = get_products(db)

# ------------------------
# Check Login
# ------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_name" not in st.session_state:
    st.session_state.user_name = "Guest"

# ------------------------
# Header
# ------------------------
st.title("🛍 FashionHub Store")

st.markdown("### Your One-Stop Fashion Destination")

st.write("---")

# ------------------------
# Welcome Message
# ------------------------
if st.session_state.logged_in:
    st.success(f"Welcome, {st.session_state.user_name} 👋")
else:
    st.info("Welcome Guest! Please Login or Signup.")

# ------------------------
# Search Bar
# ------------------------
search = st.text_input("🔍 Search for products")

st.write("---")

# ------------------------
# Dashboard
# ------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("🛍 Products", "500+")
col2.metric("👥 Customers", "10K+")
col3.metric("📦 Orders", "5K+")
col4.metric("⭐ Rating", "4.9")

st.write("---")

# ------------------------
# Categories
# ------------------------
st.subheader("🛒 Shop by Category")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("👔 Men", use_container_width=True):
        st.switch_page("pages/Men.py")

with col2:
    if st.button("👗 Women", use_container_width=True):
        st.switch_page("pages/Women.py")

with col3:
    if st.button("🧒 Kids", use_container_width=True):
        st.switch_page("pages/Kids.py")

with col4:
    if st.button("👟 Footwear", use_container_width=True):
        st.switch_page("pages/Footwear.py")

col5, col6, col7, col8 = st.columns(4)

with col5:
    if st.button("👜 Accessories", use_container_width=True):
        st.switch_page("pages/Accessories.py")

with col6:
    if st.button("☀️ Summer", use_container_width=True):
        st.switch_page("pages/Summer.py")

with col7:
    if st.button("❄️ Winter", use_container_width=True):
        st.switch_page("pages/Winter.py")

with col8:
    if st.button("🏷️ Sale", use_container_width=True):
        st.switch_page("pages/Sale.py")

st.write("---")

# ------------------------
# Featured Products
# ------------------------
st.subheader("🔥 Featured Products")

col1, col2, col3 = st.columns(3)

with col1:
    st.image(
        "https://images.unsplash.com/photo-1521572267360-ee0c2909d518",
        use_container_width=True
    )
    st.write("Nike Hoodie")
    st.write("⭐⭐⭐⭐⭐")
    st.write("₹1499")
    st.button("Add to Cart", key="p1")

with col2:
    st.image(
        "https://images.unsplash.com/photo-1542291026-7eec264c27ff",
        use_container_width=True
    )
    st.write("Adidas Shoes")
    st.write("⭐⭐⭐⭐")
    st.write("₹2999")
    st.button("Add to Cart", key="p2")

with col3:
    st.image(
        "https://images.unsplash.com/photo-1512436991641-6745cdb1723f",
        use_container_width=True
    )
    st.write("Women's Jacket")
    st.write("⭐⭐⭐⭐⭐")
    st.write("₹2499")
    st.button("Add to Cart", key="p3")

st.write("---")

# ------------------------
# Flash Sale
# ------------------------
st.subheader("🏷 Flash Sale")

st.success("🔥 Up to 70% OFF on Selected Products")

st.write("---")

# ------------------------
# Newsletter
# ------------------------
st.subheader("📧 Newsletter")

email = st.text_input("Enter your Email")

if st.button("Subscribe"):
    st.success("Thanks for subscribing!")

st.write("---")

# ------------------------
# Footer
# ------------------------
st.markdown(
"""
<center>

Made with ❤️ using Streamlit

© 2026 FashionHub Store

</center>
""",
unsafe_allow_html=True
)