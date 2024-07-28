import streamlit as st
import os

def app():
    st.title("Welcome to the Music Rating App")
    st.write("Select a section from the menu on the left to start.")
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, "../assets/welcome_image.jpg")
    
    if os.path.exists(image_path):
        st.image(image_path)
    else:
        st.warning("Welcome image not found.")
