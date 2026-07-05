import streamlit as st
from database import SessionLocal
from models import Order
from crud import update_order_status

st.set_page_config(
    page_title="Manage Orders",
    page_icon="📦",
    layout="wide"
)

st.title("📦 Order Management")

db = SessionLocal()

orders = db.query(Order).order_by(Order.id.desc()).all()

if not orders:
    st.info("No orders found.")
    db.close()
    st.stop()

# Available order statuses
status_options = [
    "Placed",
    "Pending",
    "Processing",
    "Shipped",
    "Out for Delivery",
    "Delivered",
    "Cancelled"
]

for order in orders:

    with st.expander(f"Order #{order.id} | ₹{order.total}"):

        st.write(f"User ID: {order.user_id}")
        st.write(f"Payment: {order.payment_method}")
        st.write(f"Status: {order.status}")
        st.write(f"Date: {order.created_at}")

        # Prevent ValueError if status is unexpected
        current_index = (
            status_options.index(order.status)
            if order.status in status_options
            else 0
        )

        new_status = st.selectbox(
            "Update Status",
            status_options,
            index=current_index,
            key=f"status_{order.id}"
        )

        if st.button("Update", key=f"update_{order.id}"):

            update_order_status(db, order.id, new_status)
            st.success("Status updated successfully!")
            st.rerun()

db.close()