import streamlit as st
from database import SessionLocal
from crud import (
    get_cart_items,
    remove_from_cart,
    update_cart_quantity
)

st.set_page_config(
    page_title="Shopping Cart",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 Shopping Cart")

if "user_id" not in st.session_state:
    st.warning("Please login first.")
    st.stop()

db = SessionLocal()

cart_items = get_cart_items(db, st.session_state.user_id)

if not cart_items:
    st.info("Your cart is empty.")
    db.close()
    st.stop()

grand_total = 0

for item in cart_items:

    st.divider()

    col1, col2 = st.columns([1,3])

    with col1:

        if item.product.image:
            st.image(item.product.image, width=180)

    with col2:

        st.subheader(item.product.name)

        st.write(f"Brand : {item.product.brand}")

        if item.product.category:
            st.write(f"Category : {item.product.category}")

        if item.product.rating:
            st.write(f"⭐ Rating : {item.product.rating}")

        st.write(f"Price : ₹{item.product.price}")

        qty = st.number_input(
            "Quantity",
            min_value=1,
            value=item.quantity,
            key=f"qty_{item.id}"
        )
        if qty != item.quantity:

                update_cart_quantity(
                    db,
                    item.id,
                    qty
                )

                st.rerun()

    subtotal = item.product.price * qty

    grand_total += subtotal

    st.write(f"Subtotal : ₹{subtotal}")

    if st.button(
            "🗑 Remove",
            key=f"remove_{item.id}"
        ):

            remove_from_cart(
                db,
                item.id
            )

            st.success("Removed from cart")

            st.rerun()

st.divider()

st.subheader(f"Grand Total : ₹{grand_total}")

if st.button(
    "Proceed to Checkout",
    use_container_width=True
):
    st.switch_page("pages/checkout.py")

db.close()