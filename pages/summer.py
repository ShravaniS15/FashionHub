import os
import streamlit as st
from database import SessionLocal
from crud import (
    get_products,
    add_to_cart,
    add_to_wishlist
)

st.set_page_config(
    page_title="Summer",
    page_icon="☀️",
    layout="wide"
)

st.title("☀️ Summer Collection")

db = SessionLocal()

products = get_products(db)

category_products = [
    p for p in products if p.category == "Summer"
]

if not category_products:
    st.warning("No Accessories products found.")

else:

    cols = st.columns(3)

    for i, product in enumerate(category_products):

        with cols[i % 3]:

            # Product Image
            if product.image and os.path.exists(product.image):
                st.image(product.image, use_container_width=True)
            else:
                st.image(
                    "https://via.placeholder.com/300x400?text=FashionHub",
                    use_container_width=True
                )

            st.subheader(product.name)

            st.write(f"**Brand:** {product.brand}")

            st.write(f"⭐ {product.rating}")

            st.write(f"### ₹ {product.price}")

            c1, c2 = st.columns(2)

            with c1:

                if st.button(
                    "❤️ Wishlist",
                    key=f"wish_{product.id}"
                ):

                    if "user_id" not in st.session_state:

                        st.warning("Please Login First")

                    else:

                        add_to_wishlist(
                            db,
                            st.session_state.user_id,
                            product.id
                        )

                        st.success("Added to Wishlist")

            with c2:

                if st.button(
                    "🛒 Cart",
                    key=f"cart_{product.id}"
                ):

                    if "user_id" not in st.session_state:

                        st.warning("Please Login First")

                    else:

                        add_to_cart(
                            db,
                            st.session_state.user_id,
                            product.id
                        )

                        st.success("Added to Cart")

db.close()