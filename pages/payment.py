import streamlit as st
from database import SessionLocal
from crud import place_order, clear_cart

st.set_page_config(
    page_title="Payment",
    page_icon="💳",
    layout="wide"
)

st.title("💳 Secure Payment")

# -----------------------------
# Login Check
# -----------------------------
if (
    "logged_in" not in st.session_state
    or not st.session_state.logged_in
    or "user_id" not in st.session_state
):
    st.warning("Please login first.")
    st.stop()

# -----------------------------
# Checkout Check
# -----------------------------
if "checkout_data" not in st.session_state:
    st.warning("Please complete checkout first.")
    st.stop()

data = st.session_state.checkout_data

st.subheader(f"💰 Amount to Pay: ₹{data['total']:.2f}")

st.divider()

# -----------------------------
# Payment Method
# -----------------------------
payment = st.radio(
    "Select Payment Method",
    [
        "💵 Cash on Delivery",
        "📱 UPI",
        "💳 Credit Card",
        "💳 Debit Card",
        "🏦 Net Banking"
    ]
)

payment_valid = True

if payment == "📱 UPI":

    upi = st.text_input(
        "UPI ID",
        placeholder="example@upi"
    )

    if upi.strip() == "":
        payment_valid = False

elif payment in ["💳 Credit Card", "💳 Debit Card"]:

    card_number = st.text_input("Card Number", max_chars=16)
    card_name = st.text_input("Card Holder Name")
    expiry = st.text_input("Expiry (MM/YY)")
    cvv = st.text_input("CVV", max_chars=3, type="password")

    if (
        len(card_number) != 16
        or card_name.strip() == ""
        or expiry.strip() == ""
        or len(cvv) != 3
    ):
        payment_valid = False

elif payment == "🏦 Net Banking":

    st.selectbox(
        "Select Bank",
        [
            "State Bank of India",
            "HDFC Bank",
            "ICICI Bank",
            "Axis Bank",
            "Bank of Baroda",
            "Punjab National Bank"
        ]
    )

db = SessionLocal()

if st.button("✅ Pay & Place Order", use_container_width=True):

    if not payment_valid:
        st.error("Please enter valid payment details.")

    else:

        # DEBUG
        st.write("Checkout Data:", data)

        order = place_order(
            db=db,
            user_id=st.session_state.user_id,
            total=data["total"],
            payment_method=payment,
            address=data["address"],
            city=data["city"],
            state=data["state"],
            pincode=data["pincode"],
            phone=data["phone"]
        )

        db.commit()

        clear_cart(db, st.session_state.user_id)

        del st.session_state.checkout_data

        st.success("🎉 Payment Successful!")
        st.balloons()

        st.switch_page("pages/order_success.py")

db.close()