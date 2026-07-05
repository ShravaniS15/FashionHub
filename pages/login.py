import streamlit as st
from database import SessionLocal
from services.auth_service import login_user

st.set_page_config(
    page_title="Login",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Login to FashionHub")
st.markdown("Welcome back! Please login to continue.")

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_id" not in st.session_state:
    st.session_state.user_id = None

if "user_name" not in st.session_state:
    st.session_state.user_name = ""

if "user_email" not in st.session_state:
    st.session_state.user_email = ""

with st.form("login_form"):
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    login = st.form_submit_button("Login")

if login:

    db = SessionLocal()

    success, message, user = login_user(db, email, password)

    db.close()

    if success:
        st.session_state.logged_in = True
        st.session_state.user_id = user.id
        st.session_state.user_name = user.fullname
        st.session_state.user_email = user.email

        st.success(f"Welcome {user.fullname} 🎉")
        st.write(st.session_state)
        st.switch_page("pages/Home.py")

    else:
        st.error(message)