import streamlit as st
from database import SessionLocal
from crud import get_user

st.title("👤 Profile")

if "user_id" not in st.session_state:
    st.warning("Please login first")
    st.stop()

db = SessionLocal()

user = get_user(db, st.session_state.user_id)

if "user_id" not in st.session_state or st.session_state.user_id is None:
    st.warning("Please login first")
    st.stop()

st.subheader("Your Profile")

st.write(f"Name: {user.fullname}")
st.write(f"Email: {user.email}")
st.write(f"Phone: {user.phone}")
st.write(f"Address: {user.address}")

db.close()