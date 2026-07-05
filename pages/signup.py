import streamlit as st
from database import SessionLocal
from services.auth_service import register_user

st.set_page_config(
    page_title="Signup",
    page_icon="📝",
    layout="centered"
)

st.title("📝 Create Your FashionHub Account")
st.markdown("Create an account to start shopping.")

with st.form("signup_form"):

    fullname = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    address = st.text_area("Address")

    password = st.text_input(
        "Password",
        type="password"
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password"
    )

    submit = st.form_submit_button("Create Account")


if submit:

    if fullname == "":
        st.error("Please enter your name.")

    elif email == "":
        st.error("Please enter your email.")

    elif password == "":
        st.error("Please enter a password.")

    elif password != confirm_password:
        st.error("Passwords do not match.")

    else:

        db = SessionLocal()

        success, message, user = register_user(
            db=db,
            fullname=fullname,
            email=email,
            password=password,
            phone=phone,
            address=address
        )

        db.close()

        if success:

            st.success(message)
            st.balloons()

            st.session_state.logged_in = True
            st.session_state.user_id = user.id
            st.session_state.user_name = user.fullname
            st.session_state.user_email = user.email

            st.switch_page("pages/Home.py")

        else:

            st.error(message)