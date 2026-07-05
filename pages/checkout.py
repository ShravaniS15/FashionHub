import streamlit as st
from database import SessionLocal
from crud import get_cart_items

st.set_page_config(
    page_title="Checkout",
    page_icon="💳",
    layout="wide"
)

st.title("💳 Checkout")
st.success("You are on the Checkout page")

# ----------------------------
# Login Check
# ----------------------------
if (
    "logged_in" not in st.session_state
    or not st.session_state.logged_in
    or "user_id" not in st.session_state
    or st.session_state.user_id is None
):
    st.warning("Please login first.")
    st.stop()

# ----------------------------
# Connect Database
# ----------------------------
db = SessionLocal()

# ----------------------------
# Get Cart Items
# ----------------------------
cart = get_cart_items(db, st.session_state.user_id)

if not cart:
    st.warning("🛒 Your cart is empty.")
    db.close()
    st.stop()

# ----------------------------
# Order Summary
# ----------------------------
total = 0

st.subheader("🛍️ Order Summary")

for item in cart:

    subtotal = item.product.price * item.quantity
    total += subtotal

    col1, col2 = st.columns([3, 1])

    with col1:
        st.write(f"**{item.product.name}**")
        st.caption(f"Quantity: {item.quantity}")

    with col2:
        st.write(f"₹{subtotal:.2f}")

st.divider()

st.subheader(f"💰 Total Amount: ₹{total:.2f}")

# ----------------------------
# Delivery Details
# ----------------------------
st.subheader("🚚 Delivery Details")

address = st.text_area(
    "Delivery Address",
    placeholder="Enter your complete address"
)

col1, col2 = st.columns(2)

with col1:
    city = st.text_input("City")
    pincode = st.text_input("PIN Code")

with col2:
    state = st.text_input("State")
    phone = st.text_input("Phone Number")

# ----------------------------
# Continue to Payment
# ----------------------------
if st.button(
    "Continue to Payment ➜",
    use_container_width=True
):

    if any(
    value.strip() == ""
    for value in [address, city, state, pincode, phone]
):
        st.error("Please fill all delivery details.")

else:

    st.session_state.checkout_data = {
        "total": total,
        "address": address.strip(),
        "city": city.strip(),
        "state": state.strip(),
        "pincode": pincode.strip(),
        "phone": phone.strip()
    }

    db.close()

    #st.switch_page("pages/checkout.py")
    st.switch_page("pages/payment.py")

db.close()