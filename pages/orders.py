import streamlit as st
from database import SessionLocal
from crud import get_orders

st.set_page_config(
    page_title="My Orders",
    page_icon="📦",
    layout="wide"
)

st.title("📦 My Orders")

# ----------------------------
# Login Check
# ----------------------------
if "user_id" not in st.session_state:
    st.warning("Please login first.")
    st.stop()

db = SessionLocal()

orders = get_orders(
    db,
    st.session_state.user_id
)

# ----------------------------
# No Orders
# ----------------------------
if not orders:
    st.info("🛍️ You haven't placed any orders yet.")
    db.close()
    st.stop()

# ----------------------------
# Display Orders
# ----------------------------
for order in reversed(orders):

    st.divider()

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader(f"📦 Order #{order.id}")

        st.write(f"💰 **Total Amount:** ₹{order.total:.2f}")
        st.write(f"💳 **Payment Method:** {order.payment_method}")

    with col2:
        st.write(f"📌 **Status:** {order.status}")

        if order.created_at:
            st.write(
                f"📅 **Order Date:** "
                f"{order.created_at.strftime('%d %b %Y, %I:%M %p')}"
            )

    st.markdown("### 🚚 Delivery Details")

    st.write(f"**Address:** {order.address}")
    st.write(f"**City:** {order.city}")
    st.write(f"**State:** {order.state}")
    st.write(f"**PIN Code:** {order.pincode}")
    st.write(f"**Phone:** {order.phone}")

    st.success("Thank you for shopping with FashionHub ❤️")

db.close()