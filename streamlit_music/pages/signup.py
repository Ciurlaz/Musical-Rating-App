import streamlit as st
from utils.auth import create_user

def app():
    st.title("Sign Up")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    signup_button = st.button("Sign Up")

    if signup_button:
        if create_user(username, password):
            st.success("User created successfully. Please login.")
        else:
            st.error("User already exists or error in creating user.")
