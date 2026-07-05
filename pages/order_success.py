import streamlit as st

st.set_page_config(
    page_title="Order Successful",
    page_icon="🎉",
    layout="centered"
)

st.title("🎉 Order Placed Successfully!")

st.success("Thank you for shopping with FashionHub!")

st.balloons()

st.markdown("---")

st.markdown("### ✅ Your order has been confirmed.")

st.write("📦 Your order is being processed.")

st.write("🚚 Estimated Delivery: 3 - 5 Business Days")

st.write("📧 A confirmation email will be sent shortly.")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    if st.button(
        "🛍 Continue Shopping",
        use_container_width=True
    ):
        st.switch_page("Home.py")

with col2:
    if st.button(
        "📦 View My Orders",
        use_container_width=True
    ):
        st.switch_page("pages/orders.py")