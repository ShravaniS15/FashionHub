import streamlit as st
import pandas as pd
import plotly.express as px
from database import SessionLocal
from models import Order, OrderItem, Product

st.set_page_config(
    page_title="Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 FashionHub Analytics Dashboard")

db = SessionLocal()

# ==========================
# LOAD DATA
# ==========================
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
        top_data.append({
            "Product": product.name,
            "Quantity Sold": qty
        })

if top_data:
    df = pd.DataFrame(top_data)
    fig = px.bar(df, x="Product", y="Quantity Sold", title="Top Selling Products")
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================
# CATEGORY ANALYSIS
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
# ORDER TREND
# ==========================
order_data = []

for o in orders:
    order_data.append({
        "Date": o.created_at.date(),
        "Revenue": o.total
    })

if order_data:
    df2 = pd.DataFrame(order_data)
    df2 = df2.groupby("Date").sum().reset_index()

    fig3 = px.line(df2, x="Date", y="Revenue", title="Revenue Trend")
    st.plotly_chart(fig3, use_container_width=True)

db.close()