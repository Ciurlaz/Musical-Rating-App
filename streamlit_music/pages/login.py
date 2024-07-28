import streamlit as st
from utils.auth import authenticate_user

def app():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        if authenticate_user(username, password):
            st.session_state.authenticated = True
            st.session_state.user_id = username  # Assumiamo che l'username sia unico
            return True
        else:
            st.error("Invalid username or password")
    return False
