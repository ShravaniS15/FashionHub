import os
import pandas as pd
import plotly.express as px
import streamlit as st

from database import SessionLocal

from crud import (
    add_product,
    get_products,
    delete_product,
    update_product,
    update_order_status
)

from models import (
    Product,
    Order,
    OrderItem
)

st.set_page_config(
    page_title="Admin Dashboard",
    page_icon="🛠️",
    layout="wide"
)

st.title("🛠️ FashionHub Admin Dashboard")

# ==========================
# ADMIN LOGIN (ADD THIS HERE)
# ==========================

if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

if not st.session_state.admin_logged_in:

    st.subheader("Admin Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            st.session_state.admin_logged_in = True
            st.success("Welcome Admin 👋")
            st.rerun()
        else:
            st.error("Invalid credentials")

    st.stop()

db = SessionLocal()

products = get_products(db)

# ==========================
# Dashboard Statistics
# ==========================

total_products = len(products)

total_stock = sum(p.stock for p in products)

avg_rating = (
    sum(p.rating for p in products) / total_products
    if total_products else 0
)

c1, c2, c3 = st.columns(3)

c1.metric("Products", total_products)
c2.metric("Stock", total_stock)
c3.metric("Average Rating", f"{avg_rating:.1f}")

st.divider()

# ==========================
# Add Product
# ==========================

st.header("➕ Add Product")

with st.form("add_product"):

    name = st.text_input("Product Name")

    description = st.text_area("Description")

    category = st.selectbox(
        "Category",
        [
            "Men",
            "Women",
            "Kids",
            "Footwear",
            "Accessories",
            "Summer",
            "Winter",
            "Sale",
            "New Arrivals"
        ]
    )

    brand = st.text_input("Brand")

    price = st.number_input("Price", min_value=0.0)

    stock = st.number_input("Stock", min_value=0)

    rating = st.slider("Rating", 0.0, 5.0, 4.5)

    uploaded_image = st.file_uploader(
    "Upload Product Image",
    type=["png", "jpg", "jpeg", "jfif", "webp"]
)

    submit = st.form_submit_button("Add Product")


if submit:

    image_path = ""

    if uploaded_image is not None:

        folder = f"images/{category.lower().replace(' ', '')}"
        os.makedirs(folder, exist_ok=True)

        image_path = os.path.join(folder, uploaded_image.name)

        with open(image_path, "wb") as f:
            f.write(uploaded_image.getbuffer())

    add_product(
        db,
        name=name,
        description=description,
        category=category,
        brand=brand,
        price=price,
        stock=stock,
        rating=rating,
        image=image_path
    )

    st.success("✅ Product Added Successfully")
    st.rerun()

# ==========================
# Search
# ==========================

search = st.text_input("🔍 Search Product")

if search:

    products = [
        p for p in products
        if search.lower() in p.name.lower()
    ]
st.divider()

# ==========================
# Product List
# ==========================

st.header("📦 Product Management")

for product in products:

    with st.expander(f"{product.name} - ₹{product.price:.2f}"):

        if product.image:
            st.image(product.image)

        st.write(f"**Category:** {product.category}")
        st.write(f"**Brand:** {product.brand}")
        st.write(f"**Stock:** {product.stock}")
        st.write(f"**Rating:** ⭐ {product.rating}")

        st.divider()

        st.subheader("Edit Product")

        new_price = st.number_input(
            "Price",
            value=float(product.price),
            key=f"price{product.id}"
        )

        new_stock = st.number_input(
            "Stock",
            value=int(product.stock),
            key=f"stock{product.id}"
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "💾 Update",
                key=f"update{product.id}"
            ):

                update_product(
                    db,
                    product.id,
                    price=new_price,
                    stock=new_stock
                )

                st.success("Updated Successfully")

                st.rerun()

        with col2:

            if st.button(
                "🗑 Delete",
                key=f"delete{product.id}"
            ):

                delete_product(
                    db,
                    product.id
                )

                st.success("Deleted Successfully")

                st.rerun()

from models import Order
from crud import update_order_status

st.divider()

st.header("📦 Order Management")

import plotly.express as px
from models import OrderItem, Product

orders = db.query(Order).order_by(Order.id.desc()).all()

for order in orders:

    with st.expander(f"Order #{order.id} | ₹{order.total}"):

        st.write(f"User ID: {order.user_id}")
        st.write(f"Payment: {order.payment_method}")
        st.write(f"Current Status: {order.status}")
        st.write(f"Date: {order.created_at}")

        new_status = st.selectbox(
            "Update Status",
            ["Pending", "Processing", "Shipped", "Delivered"],
            index=["Pending", "Processing", "Shipped", "Delivered"].index(order.status),
            key=f"status_{order.id}"
        )

        if st.button("Update Status", key=f"update_status_{order.id}"):

            update_order_status(db, order.id, new_status)

            st.success("Order status updated")
            st.rerun()

st.divider()

st.header("📊 Analytics Dashboard")

orders = db.query(Order).all()
order_items = db.query(OrderItem).all()
products = db.query(Product).all()

# ==========================
# KPIs
# ==========================
total_orders = len(orders)
total_revenue = sum(o.total for o in orders)

col1, col2 = st.columns(2)
col1.metric("Total Orders", total_orders)
col2.metric("Total Revenue", f"₹{total_revenue:.2f}")

st.divider()

# ==========================
# TOP PRODUCTS
# ==========================
product_sales = {}

for item in order_items:
    product_sales[item.product_id] = product_sales.get(item.product_id, 0) + item.quantity

top_products = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)

top_data = []

for pid, qty in top_products[:5]:
    product = db.query(Product).filter(Product.id == pid).first()
    if product:
        top_data.append({"Product": product.name, "Quantity": qty})

if top_data:
    df = pd.DataFrame(top_data)
    fig = px.bar(df, x="Product", y="Quantity", title="Top Selling Products")
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================
# CATEGORY SALES
# ==========================
category_sales = {}

for item in order_items:
    product = db.query(Product).filter(Product.id == item.product_id).first()
    if product:
        category_sales[product.category] = category_sales.get(product.category, 0) + item.quantity

cat_df = pd.DataFrame({
    "Category": list(category_sales.keys()),
    "Sales": list(category_sales.values())
})

if not cat_df.empty:
    fig2 = px.pie(cat_df, names="Category", values="Sales", title="Category-wise Sales")
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# ==========================
# REVENUE TREND
# ==========================
trend_data = []

for o in orders:
    trend_data.append({
        "Date": o.created_at.date(),
        "Revenue": o.total
    })

if trend_data:
    df2 = pd.DataFrame(trend_data)
    df2 = df2.groupby("Date").sum().reset_index()

    fig3 = px.line(df2, x="Date", y="Revenue", title="Revenue Trend")
    st.plotly_chart(fig3, use_container_width=True)

           
db.close()